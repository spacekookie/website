Title: LibGDX interface containers
Category: Blog
Tags: /dev/diary, libgdx, game dev, java
Date: 2017-01-24 00:14

**Let me tell you a factual statement**

*UI programming is terrible*

**Let me tell you an even more factual statement**

*UI programming in LibGDX is even more terrible*

I am a big fan of LibGDX. It's a really nifty library/ framework to get started with game development if you're more comfortable inside a code editor than a full blown game engine that is more targeted towards designers and artists. And I put my money where my mouth is: I have a series about LibGDX development for beginners on this blog and work almost exclusively with it when it comes to my own projects.

Yet, there is something that bothers me and there didn't seem to be a great solution to fix it. UI code structure. In this post I want to highlight a utility I have written for LibGDX which is very easily embeddable into your existing projects which will you help structure UI code more efficiently.

## The root problem

The reason I dislike UI programming with LibGDX is that it usually results in very long code files or passing dozens of parameters into sub-classes that are needed to update the UI for button presses, etc.

This goes so far that I have written an editor for game assets before just to realise that (once the development was complete) it had become completely unmaintainable and I had to start from scratch with better structure. It is incredibly easy to just throw out a UI design with Scene2D and LibGDX but unfortunately it is equally easy to produce very bad code which will turn into a big spaghetti mess.

Let's look at an example problem that I wanted to solve.

![LibGDX UI design problem](/images/libgdx_ui/01_base_problem.png)

Looking at this structure we have three main components that interact with each other. We have a class that handles UI logic (setting up actors in tables, adding listeners, etc), we have a window state which in the particular case which made me write an alternative was a "Lobby Handle" which coordinated what players were going to enter a match, the map, game mode and if everybody in the multiplayer match was set to "Ready". Lastly we have the actual network signal handlers that listen to TCP/ UDP packets and execute code to write/ read from the window state as well as update UI elements.

Implementing this structure with Scene2D and LibGDX will result in a lot of very ugly code. Because the network signals need to know everything about the UI (how it is structured, etc). And our window state can be written to by two different sources which means that we need to mutex it to avoid race conditions.

So, what was I trying to solve? First a bit of limitation of scope. Because a lot of UI problems have been solved over and over again and usually at the cost of runtime performance or with a *lot* of extra code.

1. UI code doesn't have to be embedded in a screen
2. All UI code can access the shared context of the screen
3. UI elements can update each other
4. Clean API that can be called on from anywhere (with a reference to the handle) that triggers range of functions.

So with that in mind, this is what I did.

```java

class MyUIHandle extands UIHandle {
    public static enum UI implements UI_BASE {
        PLAYER_LIST;
    }

    { /** Initialiser block for new objects */

        registerHandle(new PlayerList(), UI.PLAYER_LIST);
        // ... more handles
    }

    @Override
    public void initialise(Stage s, Object ... var) { ... }

    public class PlayerList extends UIContainer {

        @Override
        public void initialise(Stage s) { ... }

        // Define more API here ...
    }

}

```

When we initialise a new `UIHandle` the initialiser block will create our `PlayerLists` and register them with the `UIHandle`. That code is hidden away from you. You can see that we're implementing a different enum type that we overload with values so that we can address submodules via a compile-time checkable value (such as enums). From inside (and outside) this class `UIContainer's` are available via `handle.get(UI.SUB_HANDLE)`. Obviously keeping your enum labels short will make your function calls snappier :)

The following graphic will sort-of explain the layout in more detail.

![Super UI fixing attempt](/images/libgdx_ui/02_ui_structure.png)

What you might also notice is that the `UIHandle` has an initialise function with variadic parameters while the `UIContainer` class only takes a stage. That is because window context is stored once in the `UIHandle` and then accessable from all `UIContainer` classes. This way we only need to do the inversion of control pattern once instead of for every sub-component.

You can keep the `UIContainer` classes outside this code-file. Then you might however want to provide a construct that does another inversion of control so that an external `UIContainer` can access the context provided via initialise!

```java

public class PlayerList extends UIContainer {
    
    private MyUIHandle parent;
    public PlayerList(MyUIHandle parent) { this.parent = parent; }

    // ...
}

```

Now let's talk about that public API. In our original example we wanted to have networking code update some UI elements. And we want UI elements to update other UI elements. So first of all, we keep context in each `UIContainer` about what UI elements are accessable to it. So what we can do in every of our submodules is this:

```java
    parent.get(UI.PLAYER_LIST).updatePlayers(playerList);
```

It also means that if we get new data from – say – a network socket or AI simulation, we can very easily update data in some random UI element. 

```java
    handle.get(UI.PLAYER_LIST).populate(playerList);
```

So all in all, we have solved the following problems:

1. We have access to all game state in the UI code without passing too many parameters into lots of sub-classes
2. UI code can be moved into lots of files for easier understandability
3. Context isn't duplicated
4. UI code can update other UI code without needing a direct reference to it.

The individual `UIContainer` instances are essentially independant of each other via dependency injection.

This library isn't done yet. Most of this is kinda hacked together to fit into **my** game. But I'm interested in making it more generic and putting it on Github. Especially because I can see myself using it again in the future.

Hope this might be useful to somebody out there. If you have questions, comments, hatemail...

[Twitter](https://twitter.com/spacekookie) or [E-Mail](mailto:kookie@spacekookie.de)