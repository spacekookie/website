Title: 01. Encryption 101: Basics
Date: 2013-07-26 20:31
Category: Data Privacy
Tags: Guides
Slug: 01-encryption-101-basics
Status: published

If you haven't lived under a rock for the past few weeks you'll have
heard about the NSA and PRISM essentially spying spying on the entire
world. Now, I will write an article about why this is actually upsetting
and there are good reasons to protect ones privacy even if you have
"nothing to hide". In this tutorial I want to show you that encrypting
your communications and computers is a good way to protect yourself but
hardly the only thing you can do. And even if you encrypt everything in
your life you will leave behind a lot of meta data on the internet.
Enough to reconstruct what you were doing, what you think, who you would
vote for etc.

In this series I want to show you a little bit how you can protect
yourself. However, in this first post I want to explain you the basics
of cryptography. I won't go into detail about mathematical constructs,
you can read that on Wikipedia. But as an average person you won't need
that. Let's begin.

There are different ways how to encrypt things. The two big ways I want
to talk about now is **symmetric** and **asymmetric** encryption.

Let's look at symmetric encryption first:

![tutorial\_encryption\_symmetric](http://www.spacekookie.de/wp-content/uploads/2013/07/Screen-Shot-2013-07-26-at-22.13.29.png)

In symmetric encryption the user creates a key. That key is then being
used to encrypt but also decrypt a file. This makes the process of
encryption and decryption very fast, however also creates the problem
that the key needs to be transferred safely. If somebody got hold of the
key they could encrypt and decrypt files that they might not be able to.
Symmetric encryption is great for hard drive and large chunks of data.

However this isn't very practical in communication with others. You want
others to be able to encrypt messages sending to you but be the only one
that can decrypt them again. This is the basic idea of asymmetric
encryption. The following schematic will explain.

![tutorial\_encryption\_assymetric](http://www.spacekookie.de/wp-content/uploads/2013/07/Screen-Shot-2013-07-26-at-22.14.54.png)

There is a pair of keys: one public, one private. The public key is
being used to encrypt a file. In practise this is the key that you send
out to other people. They encrypt the messages they send to you and then
send them to you.  
The private key is the one you keep to yourself (private) and under no
circumstances send to any computer or device. Only transport it on
offline drives like USB sticks, SD cards or external hard drives. This
is the key that will allow you to decrypt messages sent to you.

If you use asymmetric encryption in your communication you can encrypt
messages for others with their public keys and decrypt messages others
sent you with your private key.

 

In following tutorials I will quickly show you how to encrypt messages
using PGP on Mac OS X, Windows and Linux, how to encrypt your hard drive
on Mac and Windows and also how to use encrypted instant messaging
services. After that I will show you ways to stay anonymous on the
internet and leave behind fewer clues about who you are and what you
were doing. Even if you have nothing to hide that doesn't mean that you
need to invite everybody into your private life!

P.S. This tutorial series was inspired by my brothers short descriptions
about security [here](http://www.leandersabel.de/itsecurity/).
