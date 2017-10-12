Title: All aboard, it's a C port
Category: Blog
Date: 2015-10-21 18:02
Tags: Dev Diary, Reedb

It's been a long time coming. This blog post, not what I am writing about. Though...what I am writing about has also been a long time coming. So in a way, yes, I guess I was right.

### Anyways.

Over a year ago I switched to Linux. I was a Mac fangirl before. I loved the ecosystem, the OS, loved the convenience and the idea of having a system that just *worked* and the power of a root terminal.
But something changed. The garden of bliss grew smaller and smaller and as I realised that I didn't own or understand my computer, that Apple was in charge of what icons I used on my Desktop, I was drawn towards Linux.

I had used the OS on servers before and even my gaming computer ran Ubuntu to play the 64bit variant of *Kerbal Space Program*. But that last step...that took a bit longer.

One of the issues I was faced with was compatibility of software. And while most of the things I used (Eclipse, Sublime Text, Spotify, etc.) were also available on Linux, one thing wasn't: my password manager.

I shall not name it by name because I don't want to advertise a product I no longer want to use. But my password manager was a problem.

So just over a year ago I set out to write my own password manager. > How hard could it be < I remember myself saying. Oh could I have been more wrong? Probably. But it wasn't easy.

### The Origin

Back in the day (and I know it's silly because it's only been a year. But still - a lot of things have changed since then) I knew Java, some Python and wanted to learn Ruby. My brother told me about a mobile framework with which I could easily make a mobile version of the password manager and I was convinced:

I wanted to write it in Ruby. 

7 months of development, feedback, discussions in a variety of hackerspaces with an even larger variety of people later - Reedb 0.10, the first usable version of what was once a password manager and had migrated into something bigger, something much cooler than I ever thought it would be: a database.

And as I added more and more features and this database became more and more intelligent I suffered from the limits of Ruby. Speed was terrible, packaging was practically impossible and it became obvious to me that Ruby was a language for the web (not because of the language. But rather because of the people that used it. The rails hipsters and web devs).

After mucking around with it for at least a month, trying several build systems and desperately trying to get this application to work I had enough. I wanted to port it.

Only around 3000 lines of code it wouldn't be too difficult to port Reedb into a different langauge. After all, most of the work had gone into the design process, not the actual coding. And while I wrestled with myself and tried a variety of languages, in the end I settled for C.

With it came a wave of problems. Conventient datastructures that just existed in Ruby such as the Hash (`{}`) or dynamic types made it easy to prototype something and quickly work with large amounts of data. All of that was different in C. And it took me a few months to really start to understand the C ways.

In the end I made a breakthrough with the design process when I finally discovered unions. And it's been a few weeks since. For now the C port of the project lives on the `newdawn` branch of the [github repo](https://github.com/reepass/reedb/tree/newdawn). The issue tracking has since been migrated to the [Lonely Robot Redmine](https://bugs.lonelyrobot.io/projects/reedb/issues) where you're welcome to fly by and check out the progress.

### The Future

I don't know how long it will take for me to finish this port. I'm making good progress, wind is in my favour. But there are still questions to be answered. Especially when it comes to the encryption of things.

But overall I'm happy with my descision. C is definately different. But it's a good kind of different where you can feel the control you have over your code. The performance is brilliant and a pure C binding makes integrating it into other languages or writing extentions for it as easy as pie.

I'll wrap this article up for now, it's gotten rather long. I hope that I can post updates about Reedb soon. Plus, I also have some other cool stuff lining up in the hardware section of my mad projects. I still want to do the Omnitool project and I'll definately keep that series alive. But it's a rather large undertaking. And I want to get some experience with smaller projects before I try to do something as mad as that. + it isn't exactly cheap to fuck up a prototype ;)

---

Anyways, I have to sail back into the C...

Kate

P.S. Sorry for the bad sailing puns. I promise there won't be any more, for shore.
