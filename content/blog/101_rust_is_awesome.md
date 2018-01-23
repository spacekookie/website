Title: Failure. Or: why Rust is probably the best programming language ever created
Category: Blog
Tags: /dev/diary, reflections, programming, rust
Date: 2018-01-28
Status: Draft

*This post is two stories.* One is about accepting and recognising personal failure, reflecting and growing from it; the other is about an incredibly and seemingly endlessly powerful programming language, called *Rust*.

**In the summer of 2014** I started a project which was kind of insane. I knew it was insane, yet I embarked on that journey regardless. I wanted to write a password manager. I chose Ruby as a language because I didn't know many others and was – in more than one way – still a programmer novice.

The details of development aren't too important. About 6-8 months into the project I had written something rather cool and functional. It wasn't very fast, the code base was a bit of a mess and I was having issues with packaging. But, at the core, I really liked what I had made, which had shifted from just being a password manager to being a universal, platform-independant secrets manager, close to a keychain. In my mind applications could write sensitive information into a "vault" which was managed by this project, without having to worry too much about access rights, authentication or anything else.

# So far so good; this is how both stories start.

Over the next few years this project would take me over and, ultimately, destroy me. I had gotten it into my mind that the cryptography should have been handled by something more low-level, something more "advanced". I talked to people, I looked at languages and in the end, thinking I had more experience now, chose C++ to re-write the project in. *This was the beginning of the end.* It took me another six months to get the basics done, getting caught up on nitty gritty details. 

I ended up switching to C, back to C++, *then back to C again*, not being satisfied with the way that one or the other language handled things. And the scope was out of control. I didn't want to make a cute little secrets manager anymore. I wanted to make a database. It had transactions, sharding, multi-user access, backups, countless optimisations, run modes and even it's own SQL-like query language. I went completely overboard and lost all grasp of what it was I wanted to create. After literally years, re-writing the same parts of the code again and again, creating new libraries to handle even smaller tasks that had been completely trivial in Ruby, **I stopped.**

What this project had turned into wasn't maintainable. It didn't even really make any sense. It had no use-case, besides "being cool" and that wasn't really enough to motivate me anymore. I was also caught up with other work, getting involved with the Google Summer of Code 2016, then slowly fading work on the project into the background. This wasn't a conscious decision though. In my mind, I was just putting it on hold, learning from all of my failures and then trying myself again at another re-write. I didn't know that *not* trying again would be the act of learning from it.

<br/>

As hackers, we are often compelled to take on the world. Everything seems plausible, sometimes trivial. We understand technology in a way that most people don't and in that, we gain confidence in our abilities past the point of reality. Hubris. We want to make things, break things, modify things. And we forget our own limitations, time and scope. We end up starting so many things that we never finish. Or we get obsessed with something that doesn't make any sense.

It took me over 2 years to understand that I can't let my impulse to adventure drive the way I work. I love open source and I love working on things that are just *free* and out in the open. I want to help build an ecosystem of tools and applications that help people, without any cost or baggage of being for a closed down system. But learning, that there were things that I can't do, that maybe the way that I viewed work, problems and how to tackle them was *fallable*, that took some more time to understand. In the end, everything I did on this project was a collosal waste of time. It's still on my github, more as a reminder to myself of how failure works...

It has nothing to do with not knowing how to solve a problem. It has nothing to do with failing to understand code or a language or a toolkit... It has *everything* to do with not knowing how to limit a project, **and when to stop...**

# This is the end of story one

It's been nearly a year since I worked on this project (or the 5th iteration of a re-write anyways), in the meantime I've worked on many small things, trying to keep in mind what I want to do, what is plausible and also useful. And in the meantime I've come into contact with a magical programming language: *Rust*!

I had started programming in Rust before, during a very stressful time in 2016. And I never managed to get into it much. This year was different though. The toolchain had matured and maybe I had also matured as a developer. And maybe I was in a better state of mind to learn new concepts. Whatever it was, I'm glad it happened.

Rust is a systems programming language by Mozilla. It's a compiled and safe language which prevents segfaults and allows for *fearless concurrency* (as they put it), without sacrificing speed. In fact, it runs [almost as fast as regular old C code]().

Now though, that's only half the reason why Rust is amazing, and I will show in a moment how the first part of this story is in any way relevant.

After creating a few smaller projects in Rust, I started thinking again about password managers. The landscape looks a little different now than it did in 2014, yet I'm still not 100% satisfied. Everything ends up being an add-on to keepass which, in my opinion, doesn't have a very good database layout or file format. And end-user applications are usually very complicated or badly designed. I know I have high standards when it comes to UI/UX design so please don't consider this slander about these projects. I just didn't want to use them and had been sticking to my Windows application running in a WINE for the last few years.

Now I knew Rust. Because the amazing thing about Rust is only partially the language. The other half is the entire toolkit that comes with it. From a built-in version manager to a kickass package manager, an ecosystem of `crates` that can be easily included, following the UNIX philosophy of enabling you to do small things, in good ways, yet somehow always fitting together.

I remembered what I had thought about before. Limitation of scope, accepting limitation of time and limits also in my own abilities. And I started writing a project very close to what it had once been in Ruby. And within a week or so, I was close to the feature set of the version I had finished, before beginning my descent into madness. It took me a week of collecting external crates, writing a few hundred lines of code myself, playing around with different crypto backends and there I was, in the process of building something cool again.

Rust makes it incredibly simple to do rapid prototyping. Yes, the language is very strict sometimes. Yet it has this feeling of "throwing shit against the wall" and seeing what sticks. With the added benefit that there are compile-time checks that make sure that there are no serious issues with your program. You can still write bad code, it just seriously limits the damage you can do. And that makes it incredibly fun to write with.

# What's the point of all this?

Well, first that I love Rust 😝.

But secondly that sometimes failure looks different than what we might expect. It's not about failing on a technical but either on a social or planning level. And maybe that this is something we should talk about and foster in the hacker community.

Rust is an amazing language for many things but it also has it's limits. There are countless people in the hacker culture who stick to their technologies because they feel familiar, dragging others into their little bubbles because they want to expand their influence, never considering if what they're advocating is sensible or scalable.

This isn't just something we (as a culture) do with tools, it also happens on a social level. And in the end, shouldn't we all strife to learn new things, broaden our horizons and, last but not least, choose the right tool, for the right job?
