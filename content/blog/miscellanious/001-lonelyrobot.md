Title: Lonely Robot and the future
Category: OldBlog
Date: 2015-08-25 15:30
Tags: Dev Diary, Lonely Robot

Hey everybody, long time no read.

As I returned from vacation on the Chaos Communication Camp 2015 (Not sure if I'll post more about that) and probably starting a new job next week (*pssst* not sure if I should talk about it ;) ) the rest of my summer is still ahead of me and I'm booming with ideas and inspiration to do stuff.

I've started more intensively coding on the `newdawn` branch of Reedb, the C port of the database and planning some features for the old codebase via the `backports` branch. Because the new codebase will use a different crypto backend (from OpenSSL to gnu_crypt) a migration agent will be neccesary to migrate between 0.11.x to 0.12+ vaults. But as very few people currently use Reedb and most setups are for testing purposes only that isn't a very big priority right now. Depends on how the current version of reedb develops :)

But that's talk for another day. What else has been going on? After the Chaos Communication Camp 2015 I've been playing around a bit with my rad1o badge.

![Rad1o Badge](/images/rad1o_badge.png "Rad1o Badge")

But not much has resulted from that yet. The distribution I'm using (Fedora 22) at this time unfortunately has a broken arm-gcc package which means that a linker for embedded systems isn't working properly. So hacking on that will have to wait a little bit. But I will very likely post more stuff about that in the future.

Now, what was this post supposed to be about? Not Reedb. Or my new job. Or the Rad1o Badge or even the cccamp. It's supposed to be about a new software studio I created.

### Lonely Robot

So far we have a website at [lonelyrobot.io](https://www.lonelyrobot.io), an issue tracker at [bugs.lonelyrobot.io](https://bugs.lonelyrobot.io) and are expanding our web prescence but mostly working on projects.

Two things that we currently have going on are an Android game called **Graviton** (which started out as a tech demo that got out of hand) and, more exciting, LRGE, the `Lonely Robot Game Engine`.

The whole thing got started between my boyfriend and me who wanted to make video games together. And after a few months of day-dreaming, talking about ideas late at night and bitching about the current state of the gaming industry. But only after a few months of talking we actually started doing something.

Over the last couple of months we've been working with the LibGDX framework, making some minior and other major modifications to it and writing the specification for an engine.

We decided to use C++ for it and build it on top of SDL (the Simple DirectMedia Layer) with a very modular design which will allow for modules to be swapped in and out.
While we are still early in the planning phase of the engine it is what we want to focus our efforts on for the next couple of months, possibly the next year.

While we do make (free) software most of our ideas are for games. Our vision is that with this game engine we will be in a position where we can create them.

We decided to go for a self-written engine over something like Unreal or Unity because of a multitude of reasons. One of which is that neither of us are very great at blackbox development (that is the development of systems with another system that the developer doesn't fully understand). It is a problem I've always had with game modding but have also run into when playing around with the Unreal Development Kit.

Even with LibGDX I've always wanted to understand the inner workings of the framework which in the end lead me to modifying large chunks of it.

So that's that. I wanted to write about it here but will probably move other thoughts about the studio to my Lonely Robot dev blog on [lonelyrobot.io](https://www.lonelyrobot.io/blog).

That'll be it for now. I have an idea for a different project brewing in my head but I don't want to talk about it for now. All you should know now is: `hardware` :D

Until another day,

Kate