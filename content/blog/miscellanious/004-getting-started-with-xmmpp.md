Title: Getting started with XMPP/ Jabber
Category: Blog
Date: 2015-11-24 12:14
Tags: Dev Diary

So after having spoken to a friend the other day and trying to get him to start using XMPP (aka as Jabber) instead of facebook messenger I realised that even while I thought it was trivial to set up other people might disagree with me. So here a little guide :)

Now...this isn't just a step-by-step instruction of what to do. In fact this article is more about getting you to understand XMPP than registered with a specific server. XMPP (formerly known as Jabber, just so you know why some people use the terms interchangably) is a chat protocol, not a chat service. It is based on XML and was originally created for near instantanious message delivery (chats). However since then it has been extended to also be able to VoIP and video (more or less good, that all depends on your client).
So XMPP is a protocol that anyone can just use. However...when I say "get started with XMPP" I don't mean set up your own servers and chat system. I mean Jabber, which is still the name of a chat service.


### A network instead of a server

The current open Jabber infrastructure is built around a bunch of servers (actually quite a **lot** of servers) that can communicate with each other. While inside the network it doesn't matter what server someone is registered with. As long as both people are part of the network they can chat with each other. And that's that. (Cryptographically and version wise it becomes a bit more complicated than that. But for the end user, that's what it boils down to).

There is a list of servers in the Jabber network (also called directory) available [here](https://xmpp.net/directory.php). As you can see there are quite a few servers out there that will allow you to register. Now...when picking a server please make note of a few things.

  - Check the software has had updates in at least the last year. You don't want to trust your private chats to outdated software, especially because that will usually mean that the server admin can't be bothered to update to newer versions of plugins and protocols.
  - Check that the server passes both "Server to Server" and "Client to Client" security tests. (Both in the green).
  - You like the domain. You don't want to have a domain "@kinkymotherfucker.com" if you don't like it :D


### Register with a server

So let's asume you've found a server you like. Scolling through the list I would probably register at [blah.im](https://blah.im). Note that you will have to import an SSL certificate. You will have to if you don't have the CA [Cert Root certificate installed](https://www.google.com/search?q=What+is+CA+Cert&ie=utf-8&oe=utf-8#q=What+is+CACert).

But you will also notice that the server doesn't actually have anything on it's website. To register on servers in a lot of cases you will need a jabber client to do it for you. I am using Pidgin and will thus also demonstrate it with that client. Pidgin is free open source software and runs on almost any platform. But feel free to use a different client if you find one you like more. The features should all just be transferable.

To install Pidgin please go to their website and follow download and installation instructions for your platform. For mine (Fedora) it's as simple as typing `dnf install pidgin`. I will assume you managed to install it and we 
move on :)

In Pidgin navigate to accounts and Manage your accounts.

![Pidgin Manage Accounts](/images/jabber/pidgin1.png  "Manage accounts")

In the opening window click on **add** and then select XMPP from the list of possible accounts to add.
Fill in your desired username, the server you want to register with and a passphrase. You can leave the resource blank. Also make sure you tick the box "Create this new Account on the Server".

Servers provide different ways to register. Some just have a registration webpage, some have an API that pidgin can talk to. Some make pidgin open a browser window and guide you to their registration site. This is something unique to the server you choose to register on.

In the case of the *blah.im* server pidgin opens a new website where I can register my nickname (which I will not do because I already have an account I like to use). Check your input with the example picture below.

![Creating new Account](/images/jabber/pidgin2.png "Create new account")

And that's that. You should be registered and ready to log in and chat with other people who also use Jabber/ XMPP, no matter what server they're on.


### Encryption via Jabber (OTR)

Jabber by itself can be secured via SSL and several transport layer security measures but that makes it no more secure than any other service. The server provider can still read all messages and log them without you ever knowing it.

Because of that a lot of people use separate encryption with Jabber called "Off the Record", short "OTR".

What OTR does is encrypt messages on your computer, sends them to your friend and then locally on their computer decrypts them again. This has however two drawbacks.

  1. Both you and your friend need to be online to chat with each other over OTR. You can't send them an offline message and let the server cache it until they come back online to read it.
  2. OTR does not support multiple devices. That means you can't start chatting on your PC, have to leave and pick up the conversation on your phone. You will need to start a new conversation. And a lot of mobile clients don't properly support OTR because they shut down the session when you lock your screen.

To address both these issues there is a new crypto protocol called "Axolotl" which fixes both of these issues. Axolotl is however a generic protocol and can be used with literally anything. To adapt it to XMPP and integrate it into the already existing infrastructure of servers there is a second protocol called "OMEMO" which implements Axolotl for XMPP. It is however still very new and *very* few clients support it at this time. In fact, the only Jabber client I know of is **Conversations** on Android.

But let's assume the downsides of OTR don't bother you (they don't bother most people). How would you go about using it? OTR in Pidgin is a plugin that needs to be enabled. Depending on what platform you install it to you might have to install the plugin yourself which can be more or less work. (On Fedora it's just `dnf install pidgin-otr`)

But [you can figure that out yourself, I hope.](http://lmgtfy.com/?q=Install+Pidgin+OTR+plugin).

*Waits for you to install the plugin*

Good, now what needs to happen. First you need to active the plugin and generate yourself a key. Go to **Tools** and then **Plugins**, search for the OTR plugin and enable it. Then go to it's configuration page.

<img class="dual" src="/images/jabber/pidgin3.png" align="left"><img class="dual" src="/images/jabber/pidgin4.png" align="right">

You will need to generate a key. A key in this case means a private key, if you're already somewhat familiar with cryptographic concepts. It's a key that is unique to you, should be protected, private and *never* shared with anyone. It is thus called your **private key**.

When clicking the button to generate a key Pidgin will make one for you and save it somewhere on your filesystem. It allows you to encrypt and decrypt data (chats, files, etc.) that people send to you.
Afterwards a key fingerprint will show up and the generate button will be greyed out.

A key fingerprint is sort of a signature. It can identify you as you. So if someone sees your fingerprint they can be sure they're talking to the right person (if they've verified the fingerprint via another medium, e.g. meeting in person). But the fingerprint doesn't expose any secure information about your key.

You can also change some basic information about how OTR should work on your system. I won't go over these for now.
![OTR Configuration](/images/jabber/pidgin5.png "OTR Config") 

And that's it. You're done. You can initiate new private conversations with people via the **OTR** submenu in the chat screen. And know that everything you say to the person in that session is secure. And here is the best thing: OTR provides something known as "forward secrecy". That means that if at some point someone steals your laptop or phone and you loose your private key that doesn't mean that, even if someone logged every single piece of encryted text going over the network between you and a certain person and has all the information needed to theoretically decrypt your messages, they can't!

Because while you chat with OTR the key continously changes. So if you ever loose your key, you don't have to worry about old chats becoming public or visible for others to see.

(As long as you don't log them in cleartext of course).

![Let's go off the record](/images/jabber/pidgin6.png "Let's go OTR") 

#### Happy chattin'

~ Kate