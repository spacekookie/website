Title: Bikeshedding disk partitioning
Category: Blog
Tags: linux, zfs, nixos
Date: 2019-07-11

I recently got a new Thinkpad. Well...new is a stretch.
It's an X230, featuring an i5 and 16GB of RAM.

One of the first things I did with this laptop was to [flash coreboot on it][coreboot].
This is something I've always wanted to be able to do,
but so far lacked hardware that was supported.
And generally, it felt like finally maybe I could have a laptop to tinker around with.

[coreboot]: https://octodon.social/@spacekookie/102150706024564666

And that's where this post begins...

## Encrypted disk

So from the start I knew I wanted to have a fully encrypted disk.

What that means is that your `/boot` partition 
(whether it is it's own partition or not), is also encrypted.

Secondly, I don't like (U)EFI...
What that means is that I'm installing GRUB
in the MBR (with a DOS partition table) instead.

Now: GRUB stage 1 can handle the encryption for us,
but there's some limitations

- Keyboard layout limited to `US`
- `/boot` can only be certain partition type
- `/` and `/boot` need be contained in an LVM

That last one _might_ not be accurate if you only want
to have an `ext4` (or similar) rootfs. But because I
want to have a `zfs` root, I need to embed it into an LVM.
This is also the reason why `/boot` needs to be it's own partition.
After we've done all this, we will install a linux distribution of choice
(which we'll reveal later).

Anyway, let's get started!

## Preparing the disk

(Feel free to skip this step)

Something you might want to do is letting your disk look
otherwise uninitialised, or "securely erasing" any data
that is already on it.
But generating random data is a lot of work and `/dev/urandom`
is very slow.

Instead you can create a crypto-disk (luks) on it, then fill it
with zero's. But because of the encryption it will seem random.

(`/dev/sda` is my disk in this example because lolwat is nvme even?)

```console
$ cryptsetup luksFormat /dev/sda1
$ cryptsetup luksOpen /dev/sda sda_crypto
$ dd if=/dev/zero of=/dev/mapper/sda_crypto bs=512 status=progress
```

This might take a while, but considerably less time than filling
the disk with random data. After this is done, you might want to
actually wipe the first bunch of bytes.

```console
$cryptsetup luksClose sda_crypto
$ dd if=/dev/urandom of=/dev/sda bs=1M count=8
```

## Basic partitioning

So what we want to do is setup a single partition on `/dev/sda`,
the same way we did to prepare the disk. Then repeat the previous
command to setup a cryptodisk.

What follows is the LVM setup:

```console
$ pvcreate lvm
$ vgcreate vg0 /dev/mapper/lvm
$ lvcreate vg0-boot -l 1G
$ lvcreate vg0-swap -l 16G
$ lvcreate vg0-root -L +100%FREE 
```

I included the `swap` partition in the LVM instead of as a ZFS subvolume
because those can sometimes deadlock and this just makes things easier.

Now we want to create the filesystems. 
For `/boot` we can just use `mkfs.ext4`,
but consider that I want to use `zfs` on `/`,
that will require some more work.

```console
$ zpool create rtank /dev/mapper/vg0-root
```

Feel free to call your pool whatever!
At this point you could also create subvolumes to 
split `/`, `/home`, ... if you wanted.

## Mounting & Configuration

So that's all good. How do we initialise this system now?
We need to mount the zfs pool first, then `/boot` and then install
our linux secret distribution of choice (spoilers: it's [NixOS]!)

[NixOS]: https://nixos.org

```
$ mkdir -p /mnt/boot
$ zpool import rtank
$ mount -t zfs rtank /mnt
$ mount /dev/mapper/vg0-boot /mnt/boot
$ nixos-generate-config --root /mnt
```

That last line is obviously NixOS specific.
You now have a fully encrypted disk setup, without
using EFI. Wuuh!

The rest of this post I want to talk about how to make this
all work with NixOS and reproducable configuration.

Most of what we need to configure is in the `boot` option.
Let's go through the settings one by one:

- `boot.loader.grub`
    - `efiSupport = false` actually the default but I like being explicit
    - `copyKernels = true` enable this to avoid problems with ZFS becoming unbootable
    - `device = "/dev/sda"` replace this with the device that holds your GRUB
    - `zfsSupport = true` to enable ZFS support 😅
    - `enableCryptodisk = true` to enable stage-1 encryption support
- `boot.zfs.devNodes = "/dev"` to point ZFS at the correct device tree (not 100% if required)
- `fileSystems."/".encrypted`
    - `enable = true`
    - `label = "lvm"` the label of your LVM
    - `blkDev = "/dev/disk/by-uuid/f1440abd-99e3-46a8-aa36-7824972fee54"` the disk that
      ZFS is installed to. You can find this out by looking at your symlinks in 
      `/dev/disk/by-uuid` and picking the correct one.
- `networking.hostId` needs to be set to some random 8 bytes    

Following is the complete config to make it easier to copy stuff from:

```
boot.loader.grub = {
    efiSupport = false;
    copyKernels = true;
    device = "/dev/sda";
    zfsSupport = true;
    enableCryptodisk = true;
};
boot.zfs.devNodes = "/dev";

fileSystems."/" = {
    encrypted = {
        enable = true;
        label = "lvm";
        blkDev = "/dev/disk/by-uuid/f1440abd-99e3-46a8-aa36-7824972fee54";
    };
}
    
networking.hostId = "<random shit>";
```

And that's it.
If you spot any errors in this article (or any for that matter),
feel free to e-mail me or send me a PR over on github.
