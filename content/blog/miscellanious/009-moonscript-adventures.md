Title: Dabbling with Moonscript
Category: Blog
Tags: Dev Diary, moonscript, programming
Date: 2017-05-06 11:55

![Lua means moon in portuguese](/images/lua_moon_banner.png)

Recently I've started learning/ using Moonscript. It's a language that compiles to [lua](https://www.lua.org/) and as such can run in the LuaJIT, an alternative lua engine which allows very easy and *fast* ffi calls into native code. This makes lua code capable of writing very performant applications and games that use native rendering, window creation or general libraries.

But in my opinion lua has always felt a bit cumbersome. I use awesomewm so I had to write it occasionally to customise my UI layout. And this is where Moonscript comes in. It's a lot of syntactic sugar on top of lua as well as some other concepts such as object orientation which lua just plain out doesn't have. And while yes, you can write good code without OO (*cough*  **C** *cough*) it is a nice tool to have in your pocket, especially when writing GUI applications or games.


## The language

```Moonscript
class Thing
  name: "unknown"

class Person extends Thing
  say_name: => print "Hello, I am #{@name}!"

with Person!
  .name = "MoonScript"
  \say_name!
```

As you can see Moonscript is an indentation based language which (in my opinion) combines syntactic elements from lua and ruby together. In the snippet above (which is from the [moonscript website](http://moonscript.org/)) you can see classes, inheritance as well as the `with` keyword which allows you to initialise/ work with objects without typing it's variable name over and over again.

If you want to learn more about the language, I can only recommend you have a look at the [Moonscript in 15 minutes guide](https://github.com/leafo/moonscript/wiki/Learn-MoonScript-in-15-Minutes)


## How to use it

You can just write Moonscript files, add `#!/usr/bin/env moon` to them and get going. Obviously that's pretty cool for little scripts that you just want to get going. But not so great for larger applications because a) you don't have access to `ffi` via luaJIT and b) it adds additional startup cost.

So instead for my projects so far (which so far are a [game](https://github.com/spacekookie/dinodino) and a desktop app) I use a `Makefile` to build and run the Moonscript compiler and then execute the `init.lua` with luajit.

```Makefile
SOURCES := $(wildcard *.moon) $(wildcard **/*.moon)
LUAOUT := $(SOURCES:.moon=.lua)0

.PHONY: all run build

all: run
build: $(LUAOUT)
%.lua: %.moon
        moonc $<
run: build
        luajit init.lua
```

## Wrapping up

So...I'm kinda excited about this. Most of the code I write is either in C or Java (depending on what exactly I'm doing). And those two strongly typed and compiled languages have served me well and will continue to be my go-to solutions for a lot of problems.

But I've long been looking for a dynamicly typed, interpreted/ just-in-time compiled language that I can use for anything from little scripts to medium-sized desktop applications. I used to use python for this but have recently (over the last 6-9 months) fallen out of love and developed a rather passionate dislike of it and it's ecosystem.

My current project will get it's own little article at some point but I don't mind teasing the progress here. I'm writing a new UI for redshift which works with X11 linux backends and is heavily inspired by f.lux on MacOS. It's written in moonscript, with my own forked version of redshift (which I call [libredshift](https://github.com/spacekookie/libredshift)). It's on [github](https://github.com/spacekookie/redshift_ctrl) and licensed under MIT. 

Hope I've made you a little curious about Moonscript. And stay tuned for updates on future projects with it :)