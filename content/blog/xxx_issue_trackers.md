Title: Issue trackers are garbage (and here's why)
Category: Blog
Tags: /dev/diary, dev culture,
Date: 2019-13-12
Status: Draft

(Outline)

- Tracking what needs to be done/ progress
- Giving newcomers a place to be onboarded
- Let people ask questions and report bugs
  - Build a knowledge base with answers that can be searched over time
  
- Tracking issues don't get updated or suck up a lot of time being maintained
  - Don't actually make it easy to write updates about what people are doing
- Discussions can easily be derailed
  - "chat" like discussions take over spaces easily
  - editing comments can be massively misleading
- How to discuss things that might be two issues at once?

> We don’t know who struck first, us or them. But we know that it was
> us that invented **issue trackers**. At the time development was very
> chaotic and it was believed that they would bring **order into the
> chaos**.

Whenever I talk to people about making FOSS projects more
approachable, one thing that always comes up is issue trackers. "Label
your issues", they say, "Mark them as 'good first issue' and
such". This is, of course, to make it easier for newcomers to see what
needs to be done, where they can help, or even just have a place to
ping for mentoring.

So far so good.

In this post I want to talk about how issue trackers are flawed and
why. Many people still insist that issue trackers are a neccessity in
the development space. This especially comes up whet discussing
decentralisation efforts for development. Many people reject the idea
that git is inherently decentralised, citing the need for an issue
tracker as a reason why.

I want to go through some examples and show why issue trackers don't
work, why they can't work, and also highlight some alternatives.

## Onboarding

I wanna talk about onboarding first because it feels like the biggest
reason people insist on having issue trackers, and might be the one
place where they're not entirly terrible.

The idea of publishing a list of things that need to be worked on,
tailored to newcomers, is a good one.  It gives people an easy way to
ask for help, and getting in the mood to submit their first patches to
a project.  A "generic list of things that should be done" list can
also in general be usefol to project maintainers, to prevent someone
from keeping too much state in their head at all times.

I think that any project should have something like this, but it
doesn't require an issue tracker to implement.  I will talk about the
alternatives later in this post, but the same described mechanism can
be implemented using a shared collaboration pad or a mailing list.

## Tracking issues

Many people keep tracking issues in their projects to give external
people and maintainers a nice way of seeing what is being worked on
and what things need to be finished before a release can happen or a
feature is fully implemented.  It also gives people the ability to
discuss things under the issue, coordinate, etc.  So far so good.

The problems here are both that tracking issues are a lot of work to
maintain, and that discussions on these issues tend to derail.
Information that's posted on an issue might not be relevant anymore in
2 weeks, yet it is presented to anyone coming into the space as "what
to read next".

Some platforms will compress some comments down, but it's still
requiring someone new to the issue to read a _lot_ of stuff before
they understand the current state of affairs.  And this doesn't even
address everyone using a different client or e-mail notifications.

Also, a badly maintained tracking issue is worse than useless.
Sometimes issues only link to other issues, at which point the
conversation can get split between mustiple places, making it slightly
les jaring to read.  But the fact remains: long-living entities
ultimately attract bloat.  Your tracking issues are informative now,
but what about in 3 months?  Or 6 months?

## Asking questions/ report bugs

"What about reporting issues," I hear you say.  "That's literally what
an issue is!" and...granted, sometimes they can be good this way.  But
there's something to consider here.  While I lumped both "reporting
issues" and "asking questions" into the same category, they are
actually wildely different things from a maintainers perspective.
They are sometimes considered one and the same, because the workflow
for a user is the same: open an issue and post some logs.

Answering questions from a maintainers perspective usually, after the
problem has been resolved, doesn't result in other issues.  Sometimes
a project might want to imprve their documentation to make this
particular use-case easier to understand, but usually the software is
left unchanged.

However if a bug was found that needs to be fixed, the issue now
describing it is written from the perspective of an outsider.  Even
the most detailed bug reports are not going to capture enough internal
state to easily communicate to a project maintainer why something has
happened.  The logs will be a guiding first principle, yes, but there
is a lot of work required for anyone looking at the issue in the
future.

A much better approach would be to repost the issue, describing what
is so far know about it, from the perspective of a maintainer.  This
might link to the ininal report, maybe adding them to CC.  This would
be aimed at other contributors, and future-contributors, making it
easier for someone to pick up work on the issue in the future.

