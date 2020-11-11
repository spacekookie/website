Title: That's the wrong abstraction layer
Category: Blog
Date: 2020-11-11
Tags: /dev/diary

I'm writing this post mostly to my future self, not any specific
project or piece of code I've seen other people write.  That's not to
say that I don't think this is something that probably applies to many
projects.  Sometimes it's easy to lose sight of what we're doing, and
it's good to be reminded.

So to start at the beginning: I've been working on [supergit], a Rust
library to parse git repositories.  It's built on top of `libgit2`
(and the `git2` rust bindings), and aims to create a more Rustic
interface and type fascade for git repositories.  It also aims to
solve issues such as: rename detection, path-history, and subtree
management.  I'm writing this library for [octopus], which will
eventually host my monorepo.

[supergit]: https://git.spacekookie.de/kookienomicon/tree/apps/servers/octopus/supergit?h=main
[octopus]: https://git.spacekookie.de/kookienomicon/tree/apps/servers/octopus/?h=main

In `supergit` the main workflow is around iterating things, seeing as
git is an acyclical graph, and iterators are a decent way to view this
datastructure.  But git graphs can get pretty big.  I wanted the
iterator to be configurable in a way that allows someone to write a
tool that searches a whole repository history, while also making it
possible to step through a history 20 commits at a time (to implement
history pagination on a website, for example).

Looking at the current API, this is how you would implement the
latter, for a `main` branch:

```rust
use supergit::Repository;

fn main() {
    let path = ... // get your repository path somehow
    let repo = Repository::open(path).unwrap();
    
    let main = repo.get_branch("main").unwrap();
    let iter = main.get(20);
    
    iter.for_each(|c| {
        println!("{}: {}", c.commit().id_str(), c.commit().summary());
    });
}
```

That's easy enough, right?  But wait, why am I calling `.commit()` on
`c`.  Isn't it already a commit?  Well...sort of.  In `supergit`, this
type is a `BranchCommit`, because this is where things get
complicated.


## Sort of like a tree, but not really

In git, rarely is a branch just a history of single commits.  Maybe
this is how some people think about their history, but it certainly
has never been the case for any of the repositories that I work on.
Basically the second you have more than one contributor, it's very
common for a history to have merge-commits in it.

So how do we deal with that in an iterator?  The design I chose was to
wrap a `Commit` object in another type, which can convey this state.
`BranchCommit` is an enum and has three variants: `Commit` (maybe I
should rename that to `Simple` or something?), `Merge`, and `Octopus`
(if you don't know what an octopus merge is, don't worry about it.
Most people don't and they're very rare and weird).

What `Merge` and `Octopus` contain are new `Branch` handles (the type
returned by `get_branch()`), meaning that for every split it's now up
to the user to decide whether they want to continue first-parent
(i.e. only ever follow the main branch line, ignoring the history of
merged branches), or if they want to enumerate the histories as well.
Most importantly: for every branch merge, you get to re-decide what
your iterator strategy should be: infinate, limited by number, or
limited up to a certain commit-hash.

So far so good I thought, this is an okay enough interface for me to
work with.  But this is where some problems appeared.


## File histories (and git internals)

*(a slight de-tour through git - feel free to skip)*

The main reason why I'm writing this more Rustic wrapper around
`libgit2` is to make it easier to determine what the history of a file
has been.  This is pretty simple to find out via the git CLI (`git log
-- <your file here>`), but not something that `libgit2` exposes,
because that's not how git stores data.

To git, all data is stored in a key-value store indexed by a SHA1
(soon to be SHA256 I think?) hash reference.  That applies to files,
full file trees, and commits as well.  Say we have a file `acab.txt`,
we commit it and it gets the ID
`da39a3ee5e6b4b0d3255bfef95601890afd80709` (the file ID, not the
commit ID!), but then we open it and write `ACAB` in it, and commit
that again.  Now the file ID is
`99f069b8a0cbe4c9485a14fe50775d0f71deb4e7`.  Both these files are
saved in the git object store, because after all you might want to go
back to the older version.

But here's the thing: from the actual commits we can get two things:
the file tree at the time of commit, and the commit parents.  To
figure out what actually _changed_ in the commit, you have to diff it
against it's parents, which is exactly what `git show` does if you
give it a reference to a commit.

What this means is that if you want to have a library that grabs the
history of a path, well you'll have to go through all commits, and
check the tree for changes at that specific path.  Furthermore, that
won't actually let you know if a file has simply been renamed, only
that it has changed.  Further logic is required to figure out if the
file is the same, but just has a different name.

And all of this is something that `supergit` implements, behind a nice
Rustic API (I hope...).


## Bloated abstractions

So I wrote a function that would, for a branch iterator, step along it
and check the history of a path, by diffing each commit with it's
parents, and tracking a path via the delta information in the diff.
But this is where I ran into problems.  Because my iterator design
always chose the first-parent to step through.  Other branches were
ignored, and because the function accepted an iterator and stepped it
internally, there was no way for my `file_history()` function to
figure out the exact behaviour the user wanted.

My first instinct was to implement branching in the `BranchIter`
itself; allowing it to branch off, essentially pushing commits it
would have to get back to onto a stack, and resuming from a previous
position.  That turned out to be a really [bad idea][badidea].

[badidea]: https://git.spacekookie.de/kookienomicon/commit/apps/servers/octopus/supergit?h=main&id=0728c2f325e2eaac2c3b834260a8d0a97afaff63

It took me about an hour of banging my head against this abstraction
before I realised that it wasn't meant to be.  Sometimes systems are
self-contained, and adding more functionality takes a considerable
amount of effort, and begs the question, if it's really the right
choice to make.  Why add more functionality to an abstraction that
works fine on it's own?

Instead, embrace composition, and add another layer on top, that can
use the previous.  You end up with a much more managable design, and
data can flow from one layer to the next.  Make sure that your
interfaces are flexible enough to be re-used, but don't think that
just because a component _could_ technically be responsible for some
work, that it really has to implement this work.

And that's it basically.  Thanks for reading my ramblings about git
and one of my side-projects.  I hope I managed to make you think about
the way you build systems a bit, and maybe next time you are in a
situation similar to this one, don't be like me :)
