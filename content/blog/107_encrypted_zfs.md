Title: Bikeshedding disk partitioning
Category: Blog
Tags: linux, zfs, nixos
Date: 2019-06-14
Status: Draft

I recently got a new Thinkpad. Well...new is a stretch.
It's an X230, featuring an i5 and 16GB of RAM.

One of the first things I did with this laptopwas to
[flash coreboot on it](https://octodon.social/@spacekookie/102150706024564666).
And generally I felt like setting up a laptop in the way I would have always wanted.

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
After we've done all this, we will install a linux distribution of choice
(which we'll talk about later).

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

(/dev/sda is my disk in this example).

```console
$ cryptsetup luksFormat /dev/sda1
$ cryptsetup luksOpen /dev/sda sda_crypto
$ dd if=/dev/zero of=/dev/mapper/sda_crypto bs=512 status=progress
```

This might take a while, but considerably less time than filling
the disk with random data. After this is done, you might want to
actually wipe the first 4096 bytes.

```console
cryptsetup luksClose sda_crypto
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

Now we want to create the filesystems. 
For `/boot` we can just use `mkfs.ext4`,
but consider that I want to use `zfs` on `/`,
that will require some more work.

```console
zpool create rtank /dev/mapper/vg0-root # feel free to call your pool whatever!

# At this point you could also create subvolumes for split `/` and `/home` 
```

## Mounting & Configuration

So that's all good. How do we initialise this system now?
We need to mount the zfs pool first, then `/boot` and then install
our linux secret distribution of choice (spoilers: it's [NixOS]!)

[NixOS]: https://nixos.org

```
mkdir -p /mnt/boot
zpool import rtank
mount -t zfs rtank /mnt
mount /dev/mapper/vg0-boot /mnt/boot

nixos-generate-config --root /mnt
```

That last line is obviously NixOS specific.
You now have a fully encrypted disk setup, without
using EFI. Wuuh!

The rest of this post I want to talk about how to make this
all work with NixOS and reproducable configuration.

**edit before release**

```nix
boot.loader.grub = {
    enable = true;
    version = 2;
    efiSupport = false;
    copyKernels = true;
    device = "/dev/sda";
    zfsSupport = true;
    enableCryptodisk = true;
};
boot.zfs.devNodes = "/dev";
boot.cleanTmpDir = true;
boot.tmpOnTmpfs = true;
hardware.cpu.intel.updateMicrocode = true;

fileSystems."/" = {
    encrypted = {
        enable = true;
        label = "lvm";
        blkDev = "/dev/disk/by-uuid/f1440abd-99e3-46a8-aa36-7824972fee54";
    };
    
networking.hostId = "<random shit>";
};
```
