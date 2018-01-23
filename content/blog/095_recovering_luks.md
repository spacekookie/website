Title: Recovering a destroyed LUKs container
Category: Blog
Date: 2015-11-19 11:41
Tags: /dev/diary, data recovery, linux

So...funny thing happened to me the other day. And by funny I mean not funny. Actually I mean quite the oposite of funny. I booted my laptop after shutting it shut down for the first time after several weeks of activity and...nothing.

I stared at my plymouth boot screen while nothing prompted me to type in my passphrase to decrypt my harddrive and the first thought through my mind was:

> Fuck...I don't have a backup.

# How to debug

Now...not to worry, after some time I was dropped into a recovery console where I could ask very simple questions like what kernel modules were present and what Systemd had been up to. And at first I thought the problem was clear: `Module failed to load: vboxdrv` and other messages populated my screen – all about VirtualBox kernel modules.

So the problem was clear. I had fucked up something when installing a new kernel or VirtualBox or anything else. So I blacklisted the modules and moved on...just...that it didn't. The problem persisted. Thinking that I had fucked something up when dealing with the GRUB config or the GRUB recovery console I got my trusty Fedora 22 live-USB out and booted off that.

# How not to panic

Looking at the partitioning on the disk I realised that my 256GB SSD was only 500MB full (which was rightfully detected as an `ext4` formatted volume. The rest of my drive was marked as `unpartitioned space`. 😱

Now...here is where things get and got interesting. But first let's have a look at my setup.

```
sda (the actual drive)
├── sda1 (ext4, mounted as /boot, contains my kernel)
└── sda2 (LUKS Encrypted Volume, contains subvolumes)
   ├── vc-root (RootFS)
   ├── vc-home (HomeFS)
   └── vc-swap (guess c:)
```

So as you can see my boot drive is outside the LUKS container and unencrypted which was why I even got the chance to enter a recovery console. The rest of my system is encrypted. And seeing that only sda1 was being picked up it meant that the partition table on my disk must have had been destroyed to the point that it no longer knew sda2.

Knowing this didn't help very much though and it took me a few hours to fix this.

# Restoring the Partition Table

So the main problem was that my partition table was broken. I don't want to start speculating as to why this happened. Maybe my SSD just lost a few blocks, maybe it was bombarded by solar radiation or maybe (just maybe) I was obducted by aliens in the night, refused to give out my master passphrase in my sleep and because of frustration of not being able to get to my data they deleted some junks from my partition table just to spite me.

Either way, a combination of two applications saved my life and hopefully will save yours.

`testdisk` and `cfdisk`

At first, make sure you have backups ;) And don't blame me if you fuck it up. Also you need to know EXACTLY what your layout is to restore this. Otherwise BAD THINGS WILL HAPPEN *waves hand around warning-ly*

Run `testdisk` on your drive, enter through the screens, let it do a deep search and just say yes to everything it wants to do. This restored the LUKS header for me again at which point my computer at least started seeing the encryption container again. Didn't mean I could log in because keyfiles couldn't be found (they're not in the header apparently).

After that, I ran `cfdisk`. What this program does (or can do) is rebuild your partition table. After letting testdisk have it's go it found my LUKS header and completely destroyed my ext4 bootpartition. So in my case this is what it looked like.
![cfdisk before it saved us](/images/cf_disk1.png  "cfdisk before")

What you will want to do is hit NEW, select the correct size of your partitions. Depending on how running testdisk went for you it might have found different parititions, all of them or none. Please! For the love of god, make sure you get your sectors right. Becase if you don't it will seriously damage your system and might make it completely unusable.
In my caseit was easy, I filled in my boot partition, marked it as bootable and set it's type correctly, also fixed the type error where before sda2 was being picked up as an LVM and not a LUKS container (this is obviously from my running system). And this is what I ended up with.
![ ](/images/cf_disk.png  "cfdisk after")

Make sure you write your changes, exit and reboot. And if you did everything right, you will have a working system again.
And that's that. I hope this article will be of use to someone at some point. And remember: make backups!

Cheers o/