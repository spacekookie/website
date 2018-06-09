Title: Making my server completely replacable
Category: Blog
Tags: /dev/diary, linux, ancible
Date: 2018-02-08
Status: Draft 

**This is mostly a draft so far, so maybe pad it a bit more 😉**

I have a virtual server running Arch Linux hosted somewhere in Germany which I want to use to host some personal services and toolchains. Currently this is done via LXD which I was a fan of for quite a while. I am using Zfs as a backend for these containers which means that I can do quick snapshots and deduplication between the base systems. But...I'm not really sure this is a nice way to do it anymore. I would like to run services in Containers just because it means that the host can be setup in a more clean way.

But right now there is a lot of manual configuration required because I'm struggling with the new way that LXD handles network taps. And while I'm gonna have to touch my configs anyways, I thought: why not go a bit further?

# Existing setup

```
 ☁ (icarus) ~> lxc list
+-------------+---------+----------------------+------+------------+-----------+
|    NAME     |  STATE  |         IPV4         | IPV6 |    TYPE    | SNAPSHOTS |
+-------------+---------+----------------------+------+------------+-----------+
| betakookie  | STOPPED |                      |      | PERSISTENT | 2         |
+-------------+---------+----------------------+------+------------+-----------+
| dcmerge     | RUNNING | 10.130.123.13 (eth0) |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
| dns         | STOPPED |                      |      | PERSISTENT | 1         |
+-------------+---------+----------------------+------+------------+-----------+
| gitlab      | RUNNING | 10.130.123.20 (eth0) |      | PERSISTENT | 2         |
+-------------+---------+----------------------+------+------------+-----------+
| hazelnot    | RUNNING | 10.130.123.12 (eth0) |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
| partkeepr   | STOPPED |                      |      | PERSISTENT | 3         |
+-------------+---------+----------------------+------+------------+-----------+
| spacekookie | RUNNING | 10.130.123.10 (eth0) |      | PERSISTENT | 2         |
+-------------+---------+----------------------+------+------------+-----------+
| stats       | RUNNING | 10.130.123.22 (eth0) |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
| turtl       | STOPPED |                      |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
| vpn-core    | STOPPED |                      |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
| wiki        | RUNNING | 10.130.123.23 (eth0) |      | PERSISTENT | 0         |
+-------------+---------+----------------------+------+------------+-----------+
```

Ultimately I want to run a few core services:

 - My website (Also available in early access on Github 😱)
 - A friend's static website
 - Gitlab
 - Bookstack (my wiki)
 - Matomo (previously Piwik)
 - Partkeepr (a tool for managing electronic components)
 - Turtl (a cool evernote clone)
 - My own Quassel core (instead of using my ex-girlfriend's one 😉)

And maybe some more that I haven't setup yet. Including a VPN between my server, my NAS and all of my other devices.


# Future setup idea

I have two servers running pretty much all the time:

 - My cloud server
 - My NAS at home

What I want to get over is having to manually configure containers and 