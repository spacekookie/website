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

## License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

