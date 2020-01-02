# fun memory violations

This is my website, running at https://spacekookie.de.  It's built
with Pelican and uses my own theme, called `crumbs` (because
kookies...).

The theme itself is pretty easy, only implementing the bits that I
need, and using some components to deduplicate template code.

There's a ["permadraft"] folder of articles that never quite made it.
Some of them are farely fleshed out but either the time to publish
them passed or I otherwise thought it'd be a bad idea ot put them on
the blog.

Their HTML pages are still being built and published, but not included
in any index page (like `blog`).  If you can find one, feel free to
hot-link to it.

## How to build

The easiest way to build the website is with [nix].  Simply run
`nix-shell` in this directory to install require dependencies.  Then
you can use `make` to get access to a whole bunch of website commands,
such as `build`, or `devserver`.  The dev server is hosted on port
8000.

**Manual install**

If you don't use nix, you need to install `python3` and `pip`.  The
python dependencies are `pelican`, `markdown` and `webassets`.  Please
for the love of god use a `virtualenv` 😬.

```bash
pip install pelican markdown webassets
pelican content
make devserver
```

## How to contribute

This repository has recently moved from Github to [sourcehut].  And
while I will still (infrequently) mirror the repository to github, I
don't want to accept contributions there anymore.

I have a [meta issue tracker][tracker], where you can post issues
about any of my projects, [in theory, without requiring
registration][bug].  Alternatively, you can send me a patch via e-mail
either to my personal address, or to my [public-inbox].

["permadraft"]: /~spacekookie/website/tree/master/content/permadraft
[nix]: https://nixos.org/nix
[sourcehut]: https://git.sr.ht/~spacekookie/website
[tracker]: https://todo.sr.ht/~spacekookie/meta
[bug]: https://todo.sr.ht/~sircmpwn/todo.sr.ht/103
[public-inbox]: https://lists.sr.ht/~spacekookie/public-inbox

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

