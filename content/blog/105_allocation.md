Title: Allocations are good, actually
Category: Blog
Tags: Rust, programming
Date: 2019-04-07

Something that you can often hear in the Rust community,
especially from people who were previously C or C++ developers,
is the adage "allocations are slow".

The other day a friend asked me how to create a consecutive list of numbers.
I pointed her at `(0..).take(x).collect()` which can be made into a `Vec<_>`,
with a number of her choice.
It did made me think however about how this could be done
much nicer in a allocation-free manner.

It lead me to come up with the following code which creates a `[_; _]` slice,
depending on which integer representation and length you choose.

```rust
(0..)
  .zip(0..x)
  .fold([0; x], |mut acc, (step, i)| {
    acc[i] = step;
    acc
  })
```

So with this in mind, I wanted to run some comparisons.
I chose the numbers so that 32768 consecutive numbers would be generated.
I compiled the example with both `Debug` and `Release` mode.
(All of these measurements are done with `rustc 1.33.0 (2aa4c46cf 2019-02-28)`)

Let's start with the non-allocating version.

```console
$ time target/debug/playground
target/debug/playground  1.45s user 0.00s system 99% cpu 1.457 total
$ time target/release/playground
target/release/playground  0.27s user 0.00s system 99% cpu 0.270 total
```

Cool! So as you can see, the `Release` profile is over 500% faster.
And performance-wise this is quite reasonable.

Let's see how an allocating implementation stacks up to it.
The code used here is the following.

```rust
let vec: Vec<u32> = (0..)
  .take(1024 * 32)
  .collect();
```

So how fast is this gonna be?

```console
$ time target/debug/playground
target/debug/playground  0.01s user 0.00s system 93% cpu 0.010 total
$ time target/release/playground
target/release/playground  0.00s user 0.00s system 85% cpu 0.005 total
```

What? ...it's faster?!

Well, I guess this does to show that it's not as simple as saying "allocations are bad".
Avoiding allocations at all cost can slow you down.

Thanks for coming to my TED talk!

*. . .*

## Yes but *why*?

Okay maybe you're more curious than that and want to understand what's going on here.
So come along, let's read some assembly!

Let's focus mostly on the release profile here,
because `Debug` generates a lot of code that makes it harder to understand.
So we have two code snippets that we should throw into [godbolt] to see what rustc does.

[godbolt]: https://rust.godbolt.org/

```rust
// This doesn't allocate
const length: usize = 1024 * 32;
pub fn slice() -> [u32; length] {
    (0..)
        .zip(0..length)
        .fold([0; length], |mut acc, (num, idx)| {
        acc[idx] = num;
        acc
    })
}

// This does
pub fn vec() -> Vec<u32> {
    (0..).take(1024 * 32).collect()
}
```

Let's have a look at the assembly that the `vec()` function generates.

<skip>

```gas
.LCPI0_0:
        .long   0
        .long   1
        .long   2
        .long   3

# ... snip ...

example::vec:
        push    rbx
        mov     rbx, rdi
        mov     edi, 131072
        mov     esi, 4
        call    qword ptr [rip + __rust_alloc@GOTPCREL]
        test    rax, rax
        je      .LBB0_4
        movdqa  xmm0, xmmword ptr [rip + .LCPI0_0]
        mov     ecx, 28
        movdqa  xmm8, xmmword ptr [rip + .LCPI0_1]
        movdqa  xmm9, xmmword ptr [rip + .LCPI0_2]
        movdqa  xmm10, xmmword ptr [rip + .LCPI0_3]
        movdqa  xmm4, xmmword ptr [rip + .LCPI0_4]
        movdqa  xmm5, xmmword ptr [rip + .LCPI0_5]
        movdqa  xmm6, xmmword ptr [rip + .LCPI0_6]
        movdqa  xmm7, xmmword ptr [rip + .LCPI0_7]
        movdqa  xmm1, xmmword ptr [rip + .LCPI0_8]
.LBB0_2:
        movdqa  xmm2, xmm0
        paddd   xmm2, xmm8
        # ... snip ...
        ret
.LBB0_4:
        mov     edi, 131072
        mov     esi, 4
        call    qword ptr [rip + _ZN5alloc5alloc18...@GOTPCREL]
        ud2
```

(full code dump [here](https://pastebin.com/zDXi7qtt))

</skip>

As you can see this uses the "Move Aligned Packed Integer Values" instructions in x86_64.
From some `x86` docs:

> Moves 128, 256 or 512 bits of packed doubleword/quadword integer values from the source operand (the second operand) to the destination operand (the first operand).

Basically the LLVM can figure out that our numbers are predictable
and can allocate them in a way that is batchable.

We will already see how the non-alloc code is going to be slower:
because the code that assigns numbers is less unterstandable to a compiler
(i.e. assigning values to an array sequencially) this will not end up being batched.

That's not to say that alloc code is going to be this fast on every platform
(RISC instruction sets lack many vectoring techniques)
and this doesn't even take embedded targets into account.

But there you have it.

LLVM is magic...

... and saying "allocations are bad" really isn't telling the whole story.
