Title: 01. Omnitool - Introduction
Slug: 01-omnitool-introduction
Category: Blog
Tags: Dev Diary, Hardware
Date: 17-09-2015 15:45
Status: published
Illustration: omnitool_background2.jpg

Any good fan of the game, book, comic, stuff series will now jump up and down in excitement. The omnitool is a constant companion, helper and friend for Commander Shepard and a life saver in several situations. Whether it be hacking doors, turning into a plasma blade and cutting peoples faces open or just plain transferring a bribe credit to the slimy Vorcha in front of you.

But please, settle down, I haven't invented holographic technology. Nor have I invented plasma tubings or even solved the financial crisis by coming up with a perfect currency (of couse generically called 'credits') that everybody wants to use.

### Then why waste your time
That's a good question :) I would hope that this series doesn't turn into a waste of time for anyone. Because...well, while I haven't done any of those things. I am planning on building an omnitool. Just a bit more low-tech.

I was actually inspired by something on Adafruit, called the Flora. It's a round gimmick with a ring of RGB LED's, GPS (I think) and an arduino to program it.

![Adafruit Flora](/images/flora_pinout.png "Adafruit Flora")

I was only really inspired to do this project when a friend of mine showed off his Flora on the CCCamp2015. 

He did some minor modifications to it, including a wristband (IDE cable) and a battery on the underside and programmed a few modes for displaying time (as an analogue clock) and a flashlight by just dialing the LED's up to full power.

![Adafruit Flora 2](/images/flora_withleds.jpg "Adafruit Flora2")

And that's kinda what gave me the idea for an omnitool. The idea of circular rings of LED's as display elements are pretty cool. 

### Basic concept

So the basic conceptis a simple. Create a wrist accessory with one or two LED rings (using shift register RGP LED's to display patterns, colours and different brightness settings), include a generic SOC to program, probably something single core ARM. Give it a bunch of RAM to run applications and a embedded systems linux.

Include GPS, blutooth, a sensor package such as temperature, preasure, accelerometer, etc.

Include extention slots where, with a simple click, the tool can be expanded to include speakers, a microphone, a bigger screen, a bigger battery, etc.

And all this in the form factor of the so beloved omnitool from Mass Effect.

I know this is a bit of a crazy project. And it will take months, if not years to complete.

Because this is the thing: I want to do it all as custom cut PCB and maybe some custom cut plastic for casings. 

I've been getting into KiCad recently, with my first project the Christmas Bauble ([Click here for details](/dev-diary/jolly-christmas-decoration/)) and have fallen in love with the tool – Don't worry Ashley, not *that* much :)

But it is pretty awesome and I urge everybody who wants to get into that sort of electronics stuff to checkout it out! [KiCad](http://www.kicad-pcb.com)

### What to expect

So what will this series be? (Hopefully) regular status reports about what I've been doing, writing about my experimences with the project, letting you guys know what I'm learning and generally just let people follow the project.

All stuff about the project will be in a Github repo. From the KiCad files to the C firmware I'll have to write. Everything you would potentially need to make your own, study it and learn from it is in there.

**[Omnitool Repository](https://github.com/spacekookie/omnitool)**


I hope that you follow along. And I'm looking forwards to comments from all of you. Have a lovely day and read you soon.

~Kate
