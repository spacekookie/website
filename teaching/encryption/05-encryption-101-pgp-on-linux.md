Title: 05. Encryption 101: PGP on Linux
Date: 2015-10-27 09:00
Category: Data Privacy
Tags: Guides
Published: false
Slug: 05-encryption-101-pgp-on-linux
Status: published

It's only been around a million years since I last wrote about this stuff :) Back when I started this series I was still using OSX and obviously focused very heavily on Mac, iOS and the likes and could barely get myself to write a little tutorial about e-mail encryption for Windows (only because friends nagged me about it).

But that's all different now. I've been almost exclusively using Linux for the last year (maybe 1 1/2 years) and I thought I'd give the PGP toolchain on Linux also called Gnu Privacy Guard (GPG) some love. So shall we begin?

### Setting up GPG with Thunderbird

So most people will be using a mail client - I use Thunderbird because *reasons* - so let's focus on that for now. And to be honest...that's kinda boring. Please have a look at my guide on how to set up Thunderbird with Enigmail on Windows because on Linux (because of Thunderbird) it works pretty much the same way.

**The jist**

`sudo $package_manager install thunderbird`

With

Fedora 22+							`dnf`
Fedora 21 and earlier		`yum`

Ubuntu 									`apt-get`
New Debian stuff				`apt`

Arch										`pacman` or `yaourt`

You get the idea...

Install the Enigmail plugin like described [here](http://spacekookie.de/data-privacy/04-encryption-101-pgp-on-windows/)!

### Getting to know the CLI

`gpg2` is a command that is installed on basically any modern Linux Distribution. And it comes with a plethora of options. It can do signing, message encryption with RSA, symmetric ciphers, hashing and compression.

Let's start with creating a new key. Like you might have read in the other tutorials GPG/ PGP uses asymetric encryption which means that you need a key-pair to use it. One key is public, for everybody to have and use, the other one is private, only for you to decrypt messages.

`gpg2 --gen-key` drops you into a nice interactive program that helps you generate a keypair and automatically adds it to your personal keychain. For all the other commands in this post to make sense you should have a keypair around to try everything out for yourself.

After you have a keypair you can go and list your keychain.

```
 ❤ (idenna) ~> gpg2 --list-keys 
/home/spacekookie/.gnupg/pubring.gpg
------------------------------------
pub   rsa4096/0022A74E 2014-08-16 [expires: 2020-08-16]
uid         [ultimate] spacekookie (Hack the planet!) <spacekookie@c-base.org>
sub   rsa4096/FEAAFEA5 2014-08-16 [expires: 2020-08-16]
sub   rsa4096/3B1D08AC 2014-10-30 [expires: 2016-10-29]

```

You can of course also just get the fingerprint off a certain key. For that you either need your e-mail address or your key ID.

```
 ❤ (idenna) ~> gpg2 --fingerprint 0022A74E
pub   rsa4096/0022A74E 2014-08-16 [expires: 2020-08-16]
      Key fingerprint = 6B93 6393 9583 E61C 9AD7  16AE 64EF 9E1B 0022 A74E
uid         [ultimate] Katharina Sabel (Personal) <katharina.sabel@mailbox.org>
uid         [ultimate] spacekookie (Hack the planet!) <spacekookie@c-base.org>
sub   rsa4096/FEAAFEA5 2014-08-16 [expires: 2020-08-16]
sub   rsa4096/3B1D08AC 2014-10-30 [expires: 2016-10-29]
```

I usually end up using my fingerprint ID just because it's shorter to type. And I actually have quite a nice one to remember C:

### Import & Export

We can also export keys from our keychain.

```
gpg2 --export 0022A74E
\(j�ڀ���sO�έ5'�bQ�6
                  �U\�1���~ꢟSSÜu��-���䡘<|�1����Gd{�&K�c<�.
                                                             ?��r�&,s��
                                                                        :�\����ـo�T'e��kT��g�����g�p.
U���d)�V��?Sk��0w���o��6� �%�i�N�M��$%ڶr_2q���
                                                   o~��'��0��p)���5�k]��F�L�ks���ؙ��z��J�Pt}?�*�
 �'6���q�8�f�]�m8m�s:ӕ�pԾz�?�ϴ|��f�B<ѹ�#�m�Gߞ���q5���Y�sAIV<��.^$ޘ���f}�/�?��(��B�
������%0068b��dAK>��                                                                {'���n�
                        �c���JT�qz����
                                        �NM���U9��UP�諤wĸ��ds�CW_�)�s���Qc����iË�(���!�lv���� ��
```

But you'll notice that's in binary. To get something more human readable you can pad it in ASCII Armour with `-a` for something more managable.

```
❤ (idenna) ~> gpg2 -a --export 0022A74E
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v2

mQINBFPvZQMBEADMRx7NgsAUBPHR4V5rNvANXChqs9qA+oqvc0/Izq01J+xiUcEM
31VcGKoxxv3Bfuqin1OPkFPDnHUOxecti5H15KGYPHylMdbD5M4UR2R7uiZLoGM8
yi4LP8GjcsAmBSxzA4H0DI83OqJc+YX5tNmAb+VUcggPJw4BZaO8a1SYDt5npRWA
DqPL72f2cC4Luhj4XngN5xim5if7myiqK9mY6FJhmJKzBxwD+mPgd+GMp2kCmQc5
JeKkQRmagN+b2Q1VEpL51WQpoFao4T9Ta5eqMHf7vZtvF4S2Nt4dILklu2n1TqtN
mq0kJdq2cl8yBXEWqp8T1AxvfsYU2CfnnzDh33Ap5BKstRc1imsHXdbFRuZMgmtz
```

The same way you can import keys either from a server 
```
gpg2 --keyserver gpg.mit.edu --recv 0022A74E
``` 

or if you received an e-mail with someone elses key (or you nicked it off their website *hint hint*) you can import them as well 

```
gpg2 --import 0022A74E.asc
```
and it'll show up in your keychain.

### Signatures

You can of course also sign messages with your private key to let people know that it was really you who sent a message. Maybe a public statement or a blackmailing threat. Whatever floats your boat.

```
gpg2 --clearsign file.txt

```

It will result in a file like you can find [here](https://spacekookie.de/pgp/spacekookie-on-the-tubes.txt).
You can of course also sign keys or not have clear signed messages but only signatures for specific messages with `--detach-sign` and `sign-key`.

### Encryption

Of course the primary idea of GPG is to provide e-mail/ message encryption. It's fairely straight forward with
```
gpg2 -a --encrypt message.txt

```

You can combine that command with a signature and even remove the ASCII Armour if you want the binary output of the file.
And that's that. You can send that to someone now. Or print it out and hang it on your wall or whatever.

---

I don't think most people will ever care about using GPG as a commandline tool but I think it's important that people understand how to, if they ever end up in a situation where they do. I also hope that this post has been somewhat useful to you. And wish you happy message encrypting :)

~Kate