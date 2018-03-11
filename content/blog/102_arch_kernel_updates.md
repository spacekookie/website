Title: The Kernel is dead! Long live the Kernel
Category: Blog
Tags: /dev/diary, linux, arch linux, pacman
Date: 2018-02-08
Status: Draft 


So I run Arch Linux and mostly I love it (I'm weird, I know 😝). But there is one thing that's really been annoying me which happens after some `pacman -Syyu` runs: all of my old kernel modules become unavailable, forcing me to do a reboot. But recently I found some stuff online to prevent that from happening so let's document all of it here.

I have similar hooks, with a slight difference - keep `/usr/lib/modules/$(uname -r)` looking exactly the same as before the upgrade.

We need a hook that is run before a pacman transaction

```
# /etc/pacman.d/hooks/linux-modules-pre.hook

[Trigger]
Operation = Upgrade
Type = Package
Target = linux

[Action]
Description = Save Linux kernel modules
When = PreTransaction
Depends = rsync
Exec = /bin/sh -c 'KVER="${KVER:-$(uname -r)}"; if test -e "/lib/modules/${KVER}"; then rsync -AHXal --delete-after "/lib/modules/${KVER}" /lib/modules/backup/; fi'
```

And another hook that is run after a pacman transaction (duh 😜)

```
# /etc/pacman.d/hooks/linux-modules-post.hook

[Trigger]
Operation = Upgrade
Type = Package
Target = linux

[Action]
Description = Restore Linux kernel modules
When = PostTransaction
Depends = coreutils
Depends = rsync
Exec = /bin/sh -xc 'KVER="${KVER:-$(uname -r)}"; if test -e "/lib/modules/backup/${KVER}"; then rsync -AHXal --ignore-existing "/lib/modules/backup/${KVER}" /lib/modules/; fi; rm -rf /lib/modules/backup'
```

But that's only half of the problem. When we eventually reboot we want to clean up the old modules. This means writing a systemd service which cleas up our old modules when we finally start the new kernel.

```
# /etc/systemd/system/linux-modules-cleanup.service

[Unit]
Description=Clean up modules from old kernels

[Service]
Type=oneshot
ExecStart=/bin/bash -exc 'for i in /usr/lib/modules/[0-9]*; do if [[ $${i##*/} = \'%v\' ]] || pacman -Qo "$${i}"; then continue; fi; rsync -AHXal "$${i}" /usr/lib/modules/.old/; rm -rf "$${i}"; done'

[Install]
WantedBy=basic.target
```

You can specify how long you want to keep your old kernel modules in this config file as well

```
# /etc/tmpfiles.d/linux-modules-cleanup.conf

R! /usr/lib/modules/.old/* - - - 4w    
```


I use `rsync --ignore-existing` to merge the backup even if `/lib/modules/$(uname -r)` still exists, in case most of its contents have disappeared in the upgrade but the directory still exists due to a stray file untracked by pacman.
