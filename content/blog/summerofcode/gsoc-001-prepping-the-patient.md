Title: First steps...baby steps
Category: OldBlog
Date: 2016-06-02 19:56
Tags: GSoC2016

So it's been almost two months, the community bonding period has passed, blog posts were written, talks held and slowly but surely I'm working myself into the qaul.net codebase.

It's always weird joining a larger project and seeing established build setups, code conventions or generally things where your first thought is "I would have done that differently...". But it's really fun.

I'm currently working myself into [mbed.tls](https://tls.mbed.org/) which is the crypto library which was chosen to power the cryptographic backend for libqaul (which powers qaul.net).

That includes some code that will probably not make it into a later version of my branch: the debugger.

### The De-bugger?!

![Debugger Pro 2016](/images/gsoc/01_debugger.png "Debugger")

Well...debuger might be a bit of a strong word, it's basically a way to develop core functions of qaul.net without having to start a GUI, going through NetworkManager dialup or oslr bootup.

There I am currently busy writing a wrapper around a new namespace added to libqaul: `qcry` (short for qaul crypto) and properly integrate all the mbed.tls sources into the library so they can be accessed by libqaul. The idea being that I don't have to leave vim and the terminal to develop on the core cryptographic components such as:

 - Key generation
 - Identify generation (with private key fingerprints)
 - Identity verification
 - ???

Only in the last step of the last bulletin do I actually have to involve the GUI of qaul.net. And until that point I wish to not come in contact with it (if avoidable).

So most of next week will be getting to know mbed-tls as I have never worked with it before. But hey...can't be worse than the gcrypt documentation¹ :')

Hope to read you soon with more updates (probably rants).

Kate o/

---

¹I am sure I will eat my words in 4 weeks
