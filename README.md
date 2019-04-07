# fun memory violations

This is my website, running at [spacekookie.de](https://spacekookie.de).
It's built with Pelican and my own theme called `crumbs` (because kookies...).

To understand the theme, you need to understand jinja because it's not very linear.
Every sub-component is structured as such and then included.
Sometimes parameters are given to the sub-component to distinguish between different page behaviour.

If you have questions, just ask :)

There's a ["permadraft"] folder of articles that never quite made it.
Some of them are farely fleshed out but either the time to publish them passed
or I otherwise thought it'd be a bad idea ot put them on the blog.

["permadraft"]: https://github.com/spacekookie/website/tree/master/content/permadraft

Their HTML pages are still being built, but not included in any index.
Feel free to hot-link to them if you like!

## How to build

You need to have python3 (not sure if it works with python2...) installed.
Then you can build the website as follows...

```bash
pip install pelican markdown webassets
pelican content
make devserver
# The server is hosted on port 8000
```

There's also a [nix] package over at [kookiepkgs] if you want to see the reproducible build.

[nix]: https://nixos.org/nix
[kookiepkgs]: https://github.com/spacekookie/kookiepkgs/blob/master/pkgs/spacekookie-de/default.nix