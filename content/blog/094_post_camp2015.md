Title: Chaos Communication Camp 2015
Category: Blog
Date: 2015-08-25 15:30
Tags: /dev/diary, ccc, c3

Hey everybody, long time no read.

As I returned from vacation on the Chaos Communication Camp 2015 (Not sure if I'll post more about that) and probably starting a new job next week (*pssst* not sure if I should talk about it 😉 ) the rest of my summer is still ahead of me and I'm booming with ideas and inspiration to do stuff.

I've started more intensively coding on the `newdawn` branch of Reedb, the C port of the database and planning some features for the old codebase via the `backports` branch. Because the new codebase will use a different crypto backend (from OpenSSL to gnu_crypt) a migration agent will be neccesary to migrate between 0.11.x to 0.12+ vaults. But as very few people currently use Reedb and most setups are for testing purposes only that isn't a very big priority right now. Depends on how the current version of reedb develops :)

But that's talk for another day. What else has been going on? After the Chaos Communication Camp 2015 I've been playing around a bit with my rad1o badge.

![Rad1o Badge](/images/rad1o_badge.png "Rad1o Badge")

But not much has resulted from that yet. The distribution I'm using (Fedora 22) at this time unfortunately has a broken arm-gcc package which means that a linker for embedded systems isn't working properly. So hacking on that will have to wait a little bit. But I will very likely post more stuff about that in the future.


Until another day,
Kate