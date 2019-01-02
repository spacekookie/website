Title: `home-manager`. Or: how not to yakhave
Category: Blog
Tags: /dev/diary, reflections, programming, nix
Status: Draft
Date: 2018-12-07

Don't expect the bait-and-switch titles to remain forever.
I just thought it was fitting for this one too 😉.

## Some background

Ever since I started venturing into computer programming and
using more and more tools that used `dotfiles`, I've been
frustrated at the lack of good tools when it came to synchronising
these files.

And that's not for lack of options.
Either I disagree fundamentally with what I want a sync tool to do
or nobody had come at the problem from the same angle as me before.
This is not to bash on other projects or solutions.
I know many people who are very happy with
either keeping their dotfiles in a large git repo, symlinking manually,
making `~` a git repo or using various tools that automate the symlink
process.

The problem I had was that not all my computers were the same.
As in, I didn't neccessarily want the same configs on all of them.
Because this is where it becomes complicated.

I had been thinking about writing a tool to do the things I wanted to do before.
Thinking back to my post about failure and limiting scope, I never started it.
While making a lot of drawing board attempts, I never wrote a single line of code
because I could tell that it would lead me down a dark path.

Reading about people on reddit from time to time who started their own
"ansible but for dotfiles" projects that never went anywhere,
I felt like I was doing the right thing by not even starting.

So nothing happened for a while. Until recently.

## Enter: nix

In case you don't know it, `nix` is a functional programming language
and pure package-manager for unix systems.
Yes, that includes MacOS and whatnot.
There is a linux distribution built around it called [NixOS] which utilises
`nix` as a package manager and configuration language heavily.

[NixOS]: https://nixos.org/nixos

So what does pure-packaging really even mean?
Have you ever had the situation where you upgraded your system
and half way through something failed and now you ended up with a broken system
because some of the packages had already changed while others had not?

Yea, that's what people would call "impure packaging".

With `nix` on the other hand this cannot happen,
since packages are atomic, meaning that after something is built,
it can't be changed again. Doing an update? New package.
Changing a small config? New package.
It means that not only can failing upgrades be seemlessly be rolled back
but also that two different versions of the same library
can easily be installed at the same time.

Yes, that's right: no more "DLL hell"!

Well okay so why am I fangirling about `nix` here?
Apart from the fact that I've been dabbling with NixOS quite a bit recently,
wanting to replace all my [Arch] installs with NixOS...

[Arch]: https://archlinux.org

## Enter: home-manager

You already saw it in the title of this post, but I wanted to re-introduce it.
What exactly is `home-manager`? 

It's `nix`, but for your userspace!
Not only does it not require root permissions,
meaning you can install packages just for you locally
(well okay, `nix` can do this as well but...besides the point).

More importantly, `home-manager` adds modules and utilities to manage userspace configurations.
Everything is sourced from `~/.config/nixpkgs/` (you can move that IIRC)
which is then used to generate all your configuration files.

Config files are kept in the nix store (which is usually located at `/nix`)
and then symlinked to their destination.

Right. Now I can practically hear you all saying:
"but didn't you say you didn't like tools that just symlinked stuff?"

Well..yes, and no. Obviously symlinking a config is much nicer than having to copy them around.
What I disliked about tools that symlink configs to places from some other place
was that I was still responsible for manage that "other place".

With `nix`, I never touch the store directly. In fact you don't ever do that!
Instead I edit the `home.nix` configuration (or sub-configs when it gets too complicated)
that then take some inputs, define the outputs and `nix` makes sure that the configs
are then where they need to be.

It gives me a single source of truth, but the best thing is
that it's not a dumb source of truth: nix is a programming language!
What that means is that I can dynamically adjust some config contents
according to what system I'm running on, while not having to worry about
keeping it all sane.

I'm really happy I didn't write my own "ansible but for dotfiles"
and I think I'd recommend nobody do that
(I mean...unless that's your kink - I don't judge!).
But I'm even more happy of having been introduced to `nix`
and `home-manager` in particular.

I'd much rather help write some re-usable modules,
that other people can also take advantage of,
than reinventing the wheel from scratch. Again.
