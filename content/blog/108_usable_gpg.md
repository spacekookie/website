Title: Usable GPG with WKD
Category: Blog
Tags: gpg, security, usability
Date: 2019-07-02

With the recent [SKS keyserver vulnerability][sks],
people have been <strike>arguing</strike> reasonably talking on the GnuPG mailing list
about how to proceed with keyservers, public key exchanges
and the GPG ecosystem as a whole.

[sks]: https://gist.github.com/rjhansen/67ab921ffb4084c865b3618d6955275f

As part of this [WKD] was mentioned.
It stands for "Web Key Directory" and is a standard 
for making a users public key available via their e-mail provider
or server with the domain that corresponds to their e-mail address.
There's several clients (such as [Enigmail] in Thunderbird)
that will use this standard to automatically fetch a user's public key,
when writing an e-mail to them.

[WKD]: https://wiki.gnupg.org/WKD
[Enigmail]: https://www.enigmail.net/index.php/en/

As an example: my e-mails are hosted with [mailbox.org],
but I use my own website as an e-mail alias.
This means that I can make my public key available via my website,
and clients using WKS could then get it automatically.

[mailbox.org]: https://mailbox.org

If you don't have your own domain and use a webhoster instead,
you might still be able to use this.
There's a [list of supported hosters][list] that you should check out.

[list]: https://wiki.gnupg.org/WKD#Mail_Service_Providers_offering_WKD 

## Setting this up

(**Note:** in newer versions of `gpg` the tool `gpg-wks-client` is included,
which can handle setting up the folder structure for you automatically).

There's two ways of making your public keys accessable this way:
the advanced and the direct way.
This post will only talk about the latter, because I find it easier.

You need to create a `.well-known/openpgpkey` directory on your server.
In this directory, place a `policy` file.
This can be zero-length, but is used to check for WKD capability.
Next, create a `hu` folder inside it
(no idea what this stands for...)

Next, take the prefix of your e-mail address
(i.e. in `kookie@spacekookie.de`, this would be `kookie`),
hash it with SHA-1 and then encode the output with z-base-32.
You can use [this][cryptii] convenient encoding website.

[cryptii]: https://cryptii.com/pipes/z-base-32

The resulting folder structure should look something like this:

```
$ tree .well-known/ 
.well-known/
└── openpgpkey
    ├── hu
    │   └── nzn5f4t6k15893omwk19pgzfztowwkhs
    └── policy
```

You need to make sure that this folder is accessable through your webserver
(this either involves including it in a static site or configuring nginx correctly).
But fundamentally, that's it!

You can test if it works by setting a new `GNUPGHOME` and running this:

```
$ env GNUPGHOME=$(mktemp -d) gpg --locate-keys <your-email-here>
```

And that's it! Clients like Enigmail, KMail or GpgOL for Outlook
will now automatically fetch your public key for any message they send.

