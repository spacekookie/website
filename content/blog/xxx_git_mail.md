Title: Collaborating with git-send-email
Category: Blog
Date: 2020-01-16
Tags: /dev/diary, git, email
Status: Draft

There's is a conversation that I keep having with various people, and
while some of my thoughts are available in e-mail threads on my
[public-inbox], I felt like maybe it was time to write a blog post
about it as well.

[public-inbox]: https://lists.sr.ht/~spacekookie/public-inbox/%3C87woa41sgn.fsf%40kookie.space%3E

The reason for this is that there is documentation on the internet on
how to use git-send-email in theory, but few ever really talk about
the resulting workflow beyond a single patch.

I won't pretend that the tools couldn't use some work or that it
doesn't take a bit of getting used to, but the reward is well worth
it, and something that I feel deserves more attention.

At the end of this I will talk a bit about why I think this mode of
collaboration is good, and could potentially be better than existing
collaboration models.


## The basics

To get into the basics of sending patches by email, I recommend
[git-send-email.io], which goes into the setup of basics on various
platforms.  It's one of those things where your setup will vary
slightly, depending on your OS and email hoster, and not something
that I feel needs too much more explanation.

[git-send-email.io]: https://git-send-email.io

You can go through that set of slides to send a test patch to the
project that's hosted on sourcehut to see if your setup is working
properly.  This is enough to send short one-offs to projects without
having to make an account anywhere (except the e-mail you already have
anyway).


## Discussion and patches

I think one of the main advantages of git mail collaboration is that
the workflow of sending patches and creating meaningful discussion on
patches is so interlinked.  While you are using different clients to
send patches and replying to feedback, the code that you send is still
available in your e-mail client. So it's easy to reply to both
feedback, while coping parts of a patch for reference.

It's important here to send e-mail as plain text, because otherwise it
might cause for people to reply to.  There's a great website that
helps you make sure your e-mail client can and is configured to use
plain text: [useplaintext.email].

[useplaintext.email]: https://useplaintext.email/


## Patchsets and revisions

So having the basics out the way, I think it's important to discuss a
more complete workflow.  When people send contribtions to projects
using pull-requests, often a set of changes will go through several
revisions before getting merged.  It's also nice to quickly force push
to fix a small typo or similar without having to let that typo ever be
part of the history of the commits that get merged.

When collaborating with git over e-mail this is still possible via
"revisions".  When sending a patchset, you can provide a `-v`
parameter with a number.  The patches you send will then have a
revision number in them, as follows: `[PATCH v2]`.  It's recommended
to send newer revisions of your patchset as a reply to the previous
one, i.e. `[PATCH]: foo` being the parent of `[PATCH v2]: foo` in the
same thread.

If you get replies to your patch, you can make changes to your
commits, then send out a new revision to the whole set, or just
individual patches, if your set of changes contains a lot of code and
you want to keep the volume of e-mails down.

The advantage of this is both that people can comment on things as
they happen in the history of the code instead of being forced to
understand a set of changes all in one go, and that you are
automatically encouraged to squash commits with messages like "small
fixes" before sending them out to a project's mailing list.


## Cover letters

One neat thing that many people also don't know about are cover
letters.  Sometimes a set of changes is so large and requires some
preface to make sense, it's a good idea to write an introduction for
someone to read first.  This is what GitHub pull-request descriptions
were derived from.

To generate a cover letter you need to create your patches in two
stages:

**git-format-patches** to generate a series of `.patch` files that can
later be turned into e-mails.  This tool takes a `--cover-letter`
paramenter that indicates to it to generate an empty patch called
`0000-cover-letter.patch`, which contains the diff-stat (git-shortlog) of
your proposed changes.  You are then free to edit this file in your
favourite text editor to write a friendly introduction to your
patchset.

Another often overlooked feature here is "timely commentary", are
comments in the patch e-mail that won't be part of the patch or the
commit message itself.  They can be made after the `---` marker in a
patch mail, but before the actual patch starts.  This section is
usually used for the diff-stat of that particular patch.

After that you can use **git-send-email**, almost the same as before,
but instead of giving it a series of commits to send (say `HEAD~3`),
you now just say `*.patch` or wherever you saved the patch files
earlier.

You don't have to resend the cover letter every time you send a new
revision of your whole patchset.  On the other hand, if things have
fundamentally changed, it might be a good idea to add one again, just
to make sure it's up to date for new people joining the thread for
feedback.


## An example

I always work well with examples and I think it's good to illustrate
how all of this can work, especially for people who might be scared by
the concept of collaborating this way.

I'm creating some patches for my `libkookie` repo and I want to get
some feedback from myself, so I decide not to push to master, which I
totally could do, but to my public-inbox instead.

There's two commits that I want some feedback on, so I make my
commits, and verify that they are indeed what I want them to be:

```
 ❤ libkookie> git log HEAD~2..HEAD
 commit 3a147c15e998d57d9db877c9cd92d0cf04411cc9 (HEAD -> master)
Author: Katharina Fey <kookie@spacekookie.de>
Date:   Wed Jan 15 21:01:06 2020 +0000

    ws/kitty: setting default shell to tmux

commit d54937fa9414d87971a01dbc0dec5105b97e8f7e
Author: Katharina Fey <kookie@spacekookie.de>
Date:   Wed Jan 15 20:59:40 2020 +0000

    ws: adding gpg submodule by default
```

Well, perfect.  This way I can also verify that the sometimes
confusing range syntax in git (`HEAD~2..HEAD`, meaning all commits
`HEAD~2`, so 2 commits ago, and `HEAD`, so now) works the way I'm
expecting it to.

I think this is quite an impressive set of changes so I decide to
reward myself with a good ol' cover letter.

```
 ❤ libkookie> git format-patch --cover-letter HEAD~2..HEAD
0000-cover-letter.patch
0001-ws-adding-gpg-submodule-by-default.patch
0002-ws-kitty-setting-default-shell-to-tmux.patch
```

I can go and verify the patches look okay, do a final pass over the
typos and then edit the cover letter as well:

```
From 3a147c15e998d57d9db877c9cd92d0cf04411cc9 Mon Sep 17 00:00:00 2001
From: Katharina Fey <kookie@spacekookie.de>
Date: Wed, 15 Jan 2020 21:06:37 +0000
Subject: [PATCH 0/2] The best patchset in the universe

To whom it may concearn,

I have created the most magnificent patch set in the history of the
universe and I really think you should merge it because otherwise
you'd be a git.

Cheers,
me!


Katharina Fey (2):
  ws: adding gpg submodule by default
  ws/kitty: setting default shell to tmux

 modules/workstation/default.nix      | 1 +
 modules/workstation/kitty/kitty.conf | 3 ++-
 2 files changed, 3 insertions(+), 1 deletion(-)

-- 
2.24.1
```

Perfect, they'll just love that over at spacekookie inc.  I quickly
exit, save, and close the file and send off the patches:

```
 ❤ libkookie> git send-email --To "~spacekookie/public-inbox"@lists.sr.ht *.patch 
0000-cover-letter.patch
0001-ws-adding-gpg-submodule-by-default.patch
0002-ws-kitty-setting-default-shell-to-tmux.patch
(mbox) Adding cc: Katharina Fey <kookie@spacekookie.de> from line 'From: Katharina Fey <kookie@spacekookie.de>'
From: Katharina Fey <kookie@spacekookie.de>
To: ~spacekookie/public-inbox@lists.sr.ht
Cc: Katharina Fey <kookie@spacekookie.de>
Subject: [PATCH 0/2] The best patchset in the universe
Date: Wed, 15 Jan 2020 21:10:48 +0000
Message-Id: <20200115211050.31664-1-kookie@spacekookie.de>
X-Mailer: git-send-email 2.24.1
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit

    The Cc list above has been expanded by additional
    addresses found in the patch commit message. By default
    send-email prompts before sending whenever this occurs.
    This behavior is controlled by the sendemail.confirm
    configuration setting.

    For additional information, run 'git send-email --help'.
    To retain the current behavior, but squelch this message,
    run 'git config --global sendemail.confirm auto'.

Send this email? ([y]es|[n]o|[e]dit|[q]uit|[a]ll):
```

You can get the question about the Cc not to show up by providing
`--supress-cc all` as a parameter, but I find it useful.  Basically a
Cc is just a ping, and if you're mentioning people by e-mail address
in your patchset (for example, if you have `Co-Authored-By` lines in
there) the appropriate people can be pinged for you automatically.

So, I'm happy with things as they are, so I hit "a", for all and send
off all three e-mails.  (You can find them in the archive
[here][thread]).

[thread]: https://lists.sr.ht/~spacekookie/public-inbox/%3C20200115211246.1832-1-kookie@spacekookie.de%3E

I wait, drink some chocolate oat milk, and wait for a reply.

```
Katharina Fey <kookie@spacekookie.de> (0 mins. ago) (inbox unread)
Subject: Re: [PATCH 2/2] ws/kitty: setting default shell to tmux
To: ~spacekookie/public-inbox@lists.sr.ht
Date: Wed, 15 Jan 2020 21:30:23 +0000

A comment on this commit:

> --- a/modules/workstation/kitty/kitty.conf
> +++ b/modules/workstation/kitty/kitty.conf
> @@ -1,10 +1,11 @@
>  font_size 10
> -font_familt twemoji-color-font
> +font_family twemoji-color-font

This was a typo before but I think we don't really want this feature
anymore, because all the font integration stuff is broken anyway.  I
think it'd be better to remove this line and then add it again when it
becomes relevant again.

~k
```

What's interesting is how feedback can be layered into the patch
itself, to comment on changes that need to be made.  This way it's
possible to keep track of the relevant lines of code, and also be able
to have a threaded conversation.

I guess I have a fair point here, the emoji fonts have been broken on
my computer for ages. So while I'm somewhat annoyed by having to
change things again, I can also understand why.

What I want to do now is reply with only a second revision on this one
commit because I don't know if there's more feedback coming for the
rest of the patchset.  First, we need to figure out what the
`Message-Id` of the previous reply is, either via you e-mail client,
or the public mail archive of the project.

**Note**: this can sometimes be tricky, but usually you should be able
to see the "raw" message in most mail clients to find the `Message-Id`
of the e-mail you care about.

```
 ❤ libkookie> git send-email \
    --To "~spacekookie/public-inbox"@lists.sr.ht \
    --reply-to "<87r2001k7k.fsf@kookie.space>"
[...]
OK. Log says:
Sendmail: /home/.nix-profile/bin/msmtp -i ~spacekookie/public-inbox@lists.sr.ht kookie@spacekookie.de
From: Katharina Fey <kookie@spacekookie.de>
To: ~spacekookie/public-inbox@lists.sr.ht
Cc: Katharina Fey <kookie@spacekookie.de>
Subject: [PATCH] ws/kitty: setting default shell to tmux
Date: Wed, 15 Jan 2020 21:42:56 +0000
Message-Id: <20200115214256.1770-1-kookie@spacekookie.de>
X-Mailer: git-send-email 2.24.1
In-Reply-To: <87r2001k7k.fsf@kookie.space>
References: <87r2001k7k.fsf@kookie.space>
MIME-Version: 1.0
Content-Transfer-Encoding: 8bit

Result: OK
```

The way that the reply works mean the thread now looks somewhat like
this:

```
[PATCH 0/2] The best patchset in the universe 
 ↳ [PATCH 1/2] ws: adding gpg submodule by default
 ↳ [PATCH 2/2] ws/kitty: setting default shell to tmux
    ↳ Re: [PATCH 2/2] ws/kitty: setting default shell to tmux
      ↳ [PATCH v2] ws/kitty: setting default shell to tmux
```

I wait a bit longer and I get another e-mail thanking me for my
contributions, and saying that the patches have been merged.

Sometimes it can be nice to re-generate a patchset with all the latest
versions of patches, even if they've been sent to the list before,
just to make it easier to apply them.  But that's often also not
required.


## The conclusion

Hey, you made it all the way to the end of this post, congrats!

I think the way of collaborating I outlined in this post has a lot of
advantages over currently popular models (i.e. pull-requests on GitHub
or merge-requests on GitLab).  People talk about wanting to
decentralise development, escaping these walled gardens that companies
have built, and they often disagree on how this can best be done.

There's even people who gladly opt into this model because they feel
that the added gamification of the platform will get people to work
more.  Not only do I think that the relationship that people have with
maximising a number on a website can be abusive, but also that I've
felt better getting patches into projects via a mailing list than any
PR has ever made me feel.

I'm not gonna pretend that the tooling for all of this couldn't use
some work: git-send-email has a 1000 confusing options and also
getting the `Message-Id` to reply to patches with can be hard and
annoying.

In fact, I'm working on some tools to make both sending and applying
patches easier (as part of the [dev-suite] project started by my
friend Michael.  I'll write more about this soon!)

[dev-suite]: https://git.sr.ht/~spacekookie/dev-suite/

In this model of development there's no need for a central service
like GitHub, no need for special software to make pull-requests
federate or even for you to host a copy of the project anywhere.

All you need is the code the project provided you, a text editor and a
mail address.
