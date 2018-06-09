Title: Why I still use Unity
Category: Blog
Tags: /dev/diary, linux
Date: 2018-04-04
Status: Draft 

In early 2016, AMD announced a new graphics driver for Linux: `amdgpu`. I was incredibly curious what they had been doing and as such, I installed Ubuntu 16.04 on my workstaton/ gaming PC and bought an R9 380X graphics card to test the new driver (previously using an older NVidia card). Over the following months I played around with custom Kernel modules, tested driver flags and did *so many benchmarks...*

Late 2016, after I finished Google's [summer of code](https://spacekookie.de/blog/what-i-have-done-in-gsoc-2016/) program, I bought a 4K display. This would turn out to be more complicated than I initially thought. Using Ubuntu with Unity I had absolutely no issues with the new resolution. I switched the UI (not just text) scaling to `1.25` which made elements large enough to interact with without cluttering the screen. Performance was nice, even with an (at the time) experimental graphics driver. I was pretty happy.

Until...the summer of 2017, when I decided that I didn't really want to use Ubuntu anymore and installed Arch on the desktop computer, the same OS I use on my laptop and two servers. But, this would turn out to be a lot more complicated than initially thought. There were a few problems that I encountered because of this and this blog article is meant to both track and inform about them. A lot of things are happening in the Linux desktop environment world and maybe this could be considered a snapshot of a changing ecosystem at some point in the future.

## The competitors

There were two desktop environments I tried. `gnome` and `cinnamon`. Both are Gtk+ based which is why I chose them. Note that KDE is being excluded for exactly that reason; I *really* don't like the way that Qt applications look and feel. 

GNOME and Cinnamon both share some common components. In fact Cinnamon started as a fork of GNOME but has since moved a bit further in their own direction. The most important component (in my opinion) is the window compositors: `mutter` and `muffin` which is a fork of the former made by the Cinnamon project.

#### Compositor?

Now, you might be asking: why a compositor? Can't you live without flaming windows or stupid transition effects? And my response to that is...well...that's not really all a compositor does. In a modern operating system the compositor provides windows with an off-screen buffer to draw into, then later blipping all the windows together onto the screen. The X server handles the screen and coordinates on it, the compositor is responsible for laying out the windows, scaling and moving them. Most bugs and performance problems with graphical desktop environments are at the compositor level, not X itself.

### The problems

But anyways, I was being side-tracked here. I was talking about problems.

- Window performance (moving, scaling, minimising) under GNOME and Cinnamon is jumpy and laggy.
  - Cinnamon (`muffin`) actually does a slightly better job at this than GNOME (`mutter`)
- Switching workspaces (either directly or into an overview, then to a new workspace) is laggy
  - GNOME is doing slightly better than Cinnamon in this regards. But neither are acceptable
  - When I had switched to either of them, I actually stopped using workspace entirely
- Neither GNOME nor Cinnamon support fractional UI scaling. **This is being worked on by GNOME!**

