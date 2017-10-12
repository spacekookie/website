Title: 02. Encryption 101: PGP on Mac
Date: 2013-10-16 16:26
Category: Data Privacy
Tags: Guides
Slug: 02-encryption-101-pgp-on-mac
Status: published

Hello Internet,

I started this series about encryption a few weeks ago but then kinda
ran out of time to actually do something with it so now I want to
continue it. Essentially this is about PGP and email encryption. This
tutorial is being inspired by my brothers (much shorter) article about
the whole thing:
<http://www.leandersabel.de/itsecurity/e-mail-encryption/>)

What is PGP, you might ask? Well, it's a good question. PGP stands for
Pretty Good Privacy and uses an asymmetrical encryption concept that you
should have learned about in the [last blog
post](http://www.spacekookie.de/01-encryption-101-basics/ "01. Encryption 101: Basics")in
this series. If you haven't...shame on you!

I want to focus on installing this email encryption on Mac Computers
first. This is compatible for several versions back.

The asymetric email encryption is based on a zero knowlege principle:
you send data through the web and except for the recipient of that data
NOBODY will be able to know what it is. Due to that the encryption needs
to happen on your device (in this case a Mac computer) and be decrypted
on an end device again (for example a Windows computer).

It doesn't really matter what e-mail provider you use as you will be
downloading the mails anyways. The easiest way to do that on a Mac is
with the pre-installed *Mail* program. If you haven't already get your
Mail to download mail from your account. If you've done this already you
can skip ahead to **[Encrypting your Mail](#encryption).**

**Setting up Mail with your account** {style="text-align: justify;"}
-------------------------------------

Open Mail and click on Mail --\> Preferences

[![mailpgp1](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp1.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp1.png)

In the upcoming window click on Accounts and then select the "+" sign on
the bottom
[![mailpgp2\_1](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp2_1.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp2_1.png)Another
window will pop up where you need to enter the apropriate information.
For large e-mail providers like gmail, yahoo, hotmail, etc. this is
quite trivial. If you are using a different webhoster you might have to
**check their FAQs for server information!**

**[![mailpgp3](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp3.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/mailpgp3.png)**After
this is done you should be able to download the e-mails from your
account to your computer. You may start a celebratory dance now!

Next up:

<a name="encryption"></a>

**Encrypting your Mail  
** {style="text-align: justify;"}
-----------------------

Now that your emails are being downloaded to your computer we can set
you up with the encryption software. The one that is the easiest to use
is called GPG, standing for *GNU Privacy Guard* (with GNU being a linux
distribution). The software comes in an easy to install package that can
be found at: [https://gpgtools.org](https://gpgtools.org/) Just scroll
down to the download button and download the suite to your computer.
Double click the .dmg file you downloaded and wait for the following
window to pop up:

[![gpginstall1](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall1.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall1.png)

This should be trivial but double click install :) Another window will
come up. Be sure to select the right harddrive. It should be installed
on the harddrive that also contains your operating system. In my case
the Harddrive is called *TARDIS* (It's bigger on the inside).

[![gpginstall2](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall2.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall2.png)

When the installation is complete eject the installation drive by
dragging it onto the trash. It's not needed anymore. Open GPG (by either
searching for it in your Applications folder or using spotlight in the
top right corner)

[![gpginstall3](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall3.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall3.png)

When you open GPG for the first time it will look somewhat like this for
you: (Except you won't have any keys in it).

[![gpfinstall4](http://www.spacekookie.de/wp-content/uploads/2013/10/gpfinstall4.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/gpfinstall4.png)

Enter your name, your email adress and check the "Upload public key
after generation" to make it easier for people to be able to find your
key. This means that they will be able to send you e-mails encrypted. If
you don't want that, don't tick it. I recomend it for regular users
because it makes exchanging keys easier. Press **Generate key**
to…generate the key (duh). During the generation process move your mouse
as much as possible and even type random letters on your keyboard.

[![gpginstall5.png](http://www.spacekookie.de/wp-content/uploads/2013/10/Screen-Shot-2013-10-16-at-17.40.57.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/Screen-Shot-2013-10-16-at-17.40.57.png)When
a window comes up and promts you to enter a password do that so.
**Choose a strong password as it will be the foundation of your e-mail
encryption**. The longer and more complicated, the better. The
application will then take your passphrase and the random input from
mouse and keyboard to generate a pair of keys: one private, one public.

If you checked it accordingly the public key will be uploaded to the MGU
servers for other people to find. The public key is used to encrypt
emails. Other people that have your public key can thus send you a
message that is encrypted. To decrypt the messages you need your private
key **that should under no circumstances be sent via the internet or any
network!**

If you need to move your private key to a second computer for use do so
on a USB drive or local, external harddrive. **DO NOT STORE YOUR PRIVATE
KEY IN A CLOUD SERVICE**

[![gpginstall6](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall6.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/gpginstall6.png)

The "sec" indicates that there is a secure (private) key. The "pub"
stands for a public key. The two combined make a key pair which you
should only have one of. So far you should be set to communicate so
let's move onto the next topic:

 {style="text-align: justify;"}

**Sending encrypted Mail** {style="text-align: justify;"}
--------------------------

Now that this is all set up, what can you do with this? First of all,
this encryption only works if the other person you're communicating with
is also using a PGP system (no matter what implimentation or operating
system).

First of all be sure to restart your Mail application after you
installed GPG. Otherwise the plugin won't start. Go ahead and compose a
new email. This is what it should look like now:

[![mailtest1](http://www.spacekookie.de/wp-content/uploads/2013/10/mailtest1.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/mailtest1.png)

The green space on the top right indicates that OpenPGP is active with
the selected email adress. The little tick in the middle confirmes that
a signature will be attached to the mail. You can disable to sign your
emails by clicking on the tick.

If you then enter an email adress of somebody that you own the public
key from (in my case let me write a mail to my brother Leander) things
will change a bit:

[![mailtest2](http://www.spacekookie.de/wp-content/uploads/2013/10/mailtest2.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/mailtest2.png)

The lock icon will become active and you will be able to lock it. The
lock indicates that the email will be encrypted. As the picture also
indicates the subject of a message is not being encrypted, **only the
content (including attachments).** Oh and please note that sending
attachments of multiple gigabytes might take a while to encrypt :)

If I send this message now, let's see what it looks like for the NSA:

``` {.lang:default .decode:true}
-----BEGIN PGP MESSAGE-----
Comment: GPGTools - http://gpgtools.org

hQIMA9/TMwACUeWZARAAoDigWvXjH8xzx4WdBUbs3aZPpJvpVoIsCVe594j9rfJu
ATQUvHF7qLUYazr2+aP+eHInuhjhgZSFyFemcmnvHI/H2XrucPp1jNhdCH8vLWo9
xvftXRXE0s6jzuaB9qSLRqQ1lHPfpdXkHz05qplP4PBDIpVBMolN9vmQWpg+/ZyW
AI8Ji/GNaT6GfCEV2h/ZXKGtRqwipWy8Wd4n+tiH4MnUaWDlFSxeUdn2LNVXTfyY
vrbaeAvfFCSwI40JVbP1E5eevD1bVgXFQ8aFsBS1GpjCY/DbmegE/qRuWmYymVim
l+vzL3Fw3cKkMVUurf6I/Hgh/hXo/sJh2fgdXaabE6NrkQanHPMxjL6/UiTL9a1D
lYEBl+TGPo6UmQhUH0G5kmPezop9Isu6Ql6xZq0SfaSR4p8QXUH8/SaE4lmiUL2O
CgEn3CFncXcpCniO+2SX/f+JAPBb7SJRbKC1E81UzNwll0tOfKTflaylyWTC18Lo
La/eMXBy/U6s91ZtfTImLdSGZI2ZffrVCmnGcK6DpLAbJCWUbsdRtmJyATDj5X1+
8jaCJU5Hhd2LybqXCtabMBXncbBSc10dAbptmVbIoNt3RAUSnUtjo62e6CPnxIIW
+GTGuD4NYReAB9JLRiuKYH5kJG0rwaokXRg9J1m2aH2r2zjyGB3zV5cJ+cI/rDOF
AQwD1U6FkjYiVDQBB/42b2VMDl8jcnOhcdWYRy+HCBw20fEKY1wOaqfLr0Rz34+A
bW3JfRjixTjteF6R+lU+XVcKeEoP7P7XDPFKsjOhx8sdICvc9nRc9KNDQKWULZaF
W+9dMhZma1WFasQLqgCLnFbron9LpQ3n5DuJ59jCk8EVgCX3WPClN9MnCMzZghOY
kphb68WKSswDJBQZsE0iw3r3mhj6jfOkyzH3/gGhle3N0BsNqVNaDsKEdHV8LN+s
qDBAMBRjEuPViXA+OVYzxfRAaEhAAPJVySKQAp+rwQt+BG0lVgO/1qzQn748UEEK
9/ZwZz4HHiKAqIHcazZGWF6amc7oFHUfJSlnWLMt0ukByKhRAf1K45TMwnJlzxmO
0jhU2DefcGfuR27i+6FbimhWeUFtbkBUdFa2ZKyTBQDGKABqi4XKW2ObCF+bHBkl
PKYEhTmcvf9Y0ejnPRb77Kng79fRlvTjpuEmMHk/rIcVL8WICO9LamxgFCMWVxU/
olHJNNVDPr9mjmlbKmAc6YTZ0POx9+mq09VIhmzoWqj9V+QcgDX+7XZO1qANdjnt
2bA2jn7neg8VTaROiWBKEuZCFB1FnzoO6yiLYsTBzzmHxiAD0pJuSnCk0EDQzIHy
b1e5yzMWnfQKeiWQkDEvFtaLzBA/f7VGVet9INnIfhDQogT+DTPn2EEe6CUYiOem
rlribmNx8uVzTSoiGrmLnEPRF1Cic+M3gRXj7835R/VMlYUo4Ii3uiZ6iIx4OlPF
4cP18BpA/GM0EIk1GjVV91oqtV9T5wL8fH8bdWdPJMpuKE11rPNJADLUD2G7KqLW
ezYDY5qqqvrMWregEApyo9fUevu1mO2QyphtsIbmeBd7WCExY5Xmnr8haHDdONVR
CBTUwDgCBHOa+iJynx7jbrVL24R36uMrqMCxV3xWtZl3afUYWtIhdQh/7s/c4r0w
9s6Qu3Z6Xy6Upyjx+FVk3PMeoA6hEHlMYUb6fCnMMH3c5Qiymu9fZU7X/WA9RCaT
DGppgD2l16PMJmBIen9uZcAsu7gOg+HSVEAPLduT09AHNzLBAiQ0VXdE42+PT38+
hLaVuaBgKzRMNGU/qHvo30R7on0YJsaDFusmtqgW3Rpgv+W/VIMN3FD33r28irnl
jFS0JOw6OQAmxBabBacjKl0jnlItbxAPgkBiVQTgdIDAhH1MvnfJwGGyppI87cXf
0aLjtxwLHzXKSeEJSjJl08+EUAfSyXItxLoyGWpxgJV/TMU6iRGYlzrSszZ0SbJ9
AWYtOlUmQuNmP9JqgCnjiLZOz+q7nQYykmtvnCcWKkAPMxNootieQ9wwL1iAdr/z
qJNMy4CS6/L22o/yiUw=
=hOZe
-----END PGP MESSAGE-----
```

Yea...not very much :) The longer your key (and message obviously) the
more and longer jibberish the message will be. And the best thing? It is
mathematically impossible to reverse engineer the message by generating
random keys. Because for each encrypted message there is a key that can
make the original message into any other message. Literally the message
I just sent my brother could be translated into Shakespeares Hamlet with
the right key.

A little note: What you see above is what you will see in your mail
inbox if you access your mails without the Mail program or GPG
installed. So be sure to follow the tutorial again for any computer you
might use this on. In my opinion this is the best part, as copanies like
Google or Microsoft that store your emails will have no idea what you're
sending things about.

 {style="text-align: justify;"}

<a name="exporting"></a>

 {style="text-align: justify;"}

**A few last pointers** {style="text-align: justify;"}
-----------------------

Right clicking onto your key pair in GPG will get you a context menu
with which you will be able to do a variety of things. Now an
explanation for the most important ones:

1.  Export: saves the key as a text file to a location on your computer.
    You can either export your public key or the pair (public and
    private). Use this to move your private key to a new computer.
2.  Send public key to key server: If you have made changes to your key
    or haven't checked the option before you can upload your key to a
    public server for people to find you.
3.  Update a public key from the keyserver in case you accidentally
    deleted it. You can't update your private key. **You loose it, it's
    gone!**
4.  Show info: displays all kinds of information about the key. You will
    be able to add a new e-mail adress to the key, in case you want to
    send encrypted emails from multiple adresses or change the
    expiration date of the key, etc.

One last important thing: What if you want to import a key to your GPG
keychain? Take my public key for example:

``` {.lang:default .decode:true}
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG/MacGPG2 v2.0.19 (Darwin)

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
kM773MWawwH7Z3VRQLYT/oweYc6Pd1A=
=NBpw
-----END PGP PUBLIC KEY BLOCK-----
```

(Downloadable here:
<http://spacekookie.de/pgp/katharina-sabel-public.asc>)

First open a text editor of your choosing. In my case I will use the
standard Mac **Text Edit.** Now you need to copy and paste the key
(From --BEGIN-- to --END--) and paste it into your text
editor.[![importkeymac1](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac1.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac1.png)

Looks kinda scary, I know. Hang in there. Now save the file with CMD +
S. In the following popup you need to select to save the file locally
and not on Apples iCloud servers. They can be great but not for this!

[![importkeymac2](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac2.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac2.png)

Give the file a random name (it's not really important) and save it.
Next up close the Text Editor and navigate to your saved file. Right
click on it to bring up the context menu and choose **Get Info**

[![importkeymac3](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac3.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac3.png)In
the upcoming window then search for the name field and change the
extention from .rtf to **.asc**

.RTF is a file format for text files and great for stuff. But we want
the GPG application to recognize all the jibberish as a key and for that
we need to change the extention to .asc

When your computer prompts you if you're sure you agree and change the
extention to **.ASC**

[![importkeymac4](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac4.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac4.png)

Now we're almost done. Go to your GPG application, click the IMPORT
button in the top left and navigate to your key.asc file on your
computer you just created. Press open and see the magic happen as the
key is being added to your keychain.

[![importkeymac5](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac5.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkeymac5.png)

Now...there is a much easier way to import new keys and that's why I
kind of insisted on your uploading your public key to a keyserver. If
you go to your GPG application, select **Key** (in the menu bar on top
of the screen) and then **Search for key** you will be promted with a
little window:

[![importkrymac6](http://www.spacekookie.de/wp-content/uploads/2013/10/importkrymac6.png)](http://www.spacekookie.de/wp-content/uploads/2013/10/importkrymac6.png)In
that window you can search for an email adress or parts of it to find a
key. To find my public key simply search for katharina.sabel.

I kinda fucked up my keys a few months ago so I have two keys on the
server. Select the one that was created last (\~August 2013) to add the
key to your keychain. You won't have to deal with any of the hassle
including file formats, copy pasting, etc. It's all done.

Feel free to hit me up with a random message to
sabel.katharina@gmail.com. Be sure to encrypt it, just to test things
out. And I hope that this tutorial will encourage you to encourage more
of your family and friends to use encryption. If not for transmitting
sensible documents like contracts, bills or whatever just to piss off
the NSA :)

Have a lovely day,

\~Kate
