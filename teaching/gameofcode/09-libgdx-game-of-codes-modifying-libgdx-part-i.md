Title: 09. (LibGDX) Game of Codes: Modifying LibGDX — Part I
Date: 2014-04-04 13:57
Category: Game of Codes
Tags: Guides
Slug: 09-libgdx-game-of-codes-modifying-libgdx-part-i
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. It's been a while since my last post and I want to make up
for that today. Last time we were talking about Screens and subscreens
for a game that made showing new information a whole lot faster and more
intuitive as it didn't require more UI elements to be written into the
same class.

Well…despite what you might think I HAVE been very busy coding on my own
project (\*hinthint\*
[www.spacekookie.de/projects/empires](http://www.spacekookie.de/projects/empires/ "Interstellar Empires") \*hinthint\*
;) ) and have started modifying the LibGDX core a few months ago to
better suit my needs. Well…most of my modifications are pretty specific
to my case. Changing the hexagon renderer to account for my custom data
types, changing the input handling method, etc... But in the last 2
weeks I have done something that I think can be quite handy and I want
you to see it. Additionally I will be using that example to show you how
modding LibGDX to your own needs can be very productive and even fun. It
will give you the ability to learn and understand how that framework
we've only been using so far is structured and works. And it will remove
some of the magic that you might feel is involved ;) So shall we begin?

 

First of all I want to show you a graphic again from my last post of the
Game of Codes.

![rt7obekn-1](http://www.spacekookie.de/wp-content/uploads/2014/01/rt7obekn-1-1024x576.jpg)

This is how I thought our menu would be, have a screen in front of our
game that then showed some stuff. Well…that's all nice and good IF you
only use one game-screen. But most games aren't that simple. Usually in
a complex game you want to have your background code for music and input
handling or whatever jazz you're doing running in your game but then
have different screens for the Menu, the game, the settings, maybe an
inventory? Who knows? And well…that's all very 1-dimentional. So what I
did first was look at how things were structured in LibGDX.

``` {.lang:java .decode:true}
public abstract class Game implements ApplicationListener {
    private Screen screen;

    . . .

    public void setScreen (Screen screen) {
        if (this.screen != null) this.screen.hide();
        this.screen = screen;
        if (this.screen != null) {
            this.screen.show();
            this.screen.resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
        }
    }

    . . .
}
```

As you can see the "Game" class that we extend with our MainGame-Class
where we have our ship and station and input and all those lovely assets
implements the ApplicationListener, JUST as our MainGame-class did
before we started working with Screens. Oh and look! There is some of
that code that we use to set a Screen.

Now…what can we do with this? Well first of all we can create a new
class in our Core package and call it "CustomGame" or anything you like.
But it should be clear that it's something very specific. Make it
abstract and let it implement the ApplicationListener interface, just
like the example above.

We can also actually just copy most of that code in the stock-Game class
into our own.

``` {.lang:java .decode:true}
public abstract class CustomGame implements ApplicationListener {
  private Screen screen;

  @Override
  public void create() {

  }

  @Override
  public void resize(int width, int height) {
    if (screen != null)
      screen.resize(width, height);

  }

  @Override
  public void render() {
    if (screen != null)
      screen.render(Gdx.graphics.getDeltaTime());

  }

  @Override
  public void pause() {
    if (screen != null)
      screen.pause();

  }

  @Override
  public void resume() {
    if (screen != null)
      screen.resume();

  }

  @Override
  public void dispose() {
    if (screen != null)
      screen.dispose();

  }

  public void setScreen(Screen screen) {
    if (this.screen != null)
      this.screen.hide();
    this.screen = screen;
    if (this.screen != null) {
      this.screen.show();
      this.screen.resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
    }
  }

  public Screen getScreen() {
    return screen;
  }

}
```

All that does is exactly what the other class did before. If you now go
into our main-game class and let it extend "CustomGame" instead of
"Game" and compile the game it will run JUST like it did before. Because
nothing has changed. And that's what we'll change RIGHT NOW.

What do we want? Well…we want to use Screens in our game for the actual
game screens (menu, in-game, settings, cut scenes, etc.) as well as
Screens to display information OVER the current one (for example for an
Inventory screen or dialogue options or WHATEVER!). Now…there are two
things we could do right now:

The first would be to only add one more screen, call it "overlay" and
copy the same code as for the other screen into the class. That would
give us two screens to work with. But I don't like that idea at all.
Instead I want to do something different. I want to be able to have a
stack of Overlays over each other. And that's why we'll use a
Stack\<Screen\>!

``` {.lang:java .decode:true}
  private Stack<Screen> overlays;

  @Override
  public void create() {
    overlays = new Stack<Screen>();
  }
```

Put this code under the declaration of the private Screen variable and
initialize the stack in your create() method that was (so far) not used.
Now we of course need to make sure we actually call "super.onCreate()"
in our child-class (So our main game-class).

So far so good. But, we can't actually do anything with that yet. First
we will want to write two access methods for the stack.

``` {.lang:java .decode:true}
  public void addOverlay(Screen overlay) {
    overlays.add(overlay);
    overlay.show();
    overlay.resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
  }

  public void removeOverlay() {
    if (!overlays.isEmpty())
      overlays.pop().dispose();
  }
```

What this will do is add a new overlay to the stack when we need one and
also call the show and resize method on the overlay (which is really
just a screen) to set up everything correctly!  
The second method will remove the last overlay (if it exists) by
popping it off the stack and calling dispose() on it to finalize. This
is important so that we avoid having un-used and non-removed resources
in our memory.

So far so good. The problem now is that our screen won't actually be
shown anywhere. Sure, we add it to our stack and show() and resize() it.
But it's not getting rendered. For that to happen we'll have to add some
more code. And in addition to that I would recommend more code to then
dispose of the screens again as well.

For every action that we take on our main-screen we need to add this
code to it as well.

``` {.lang:java .decode:true}
 if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.ACTION_HERE();
```

Essentially iterating over the stack to apply it to every overlay. This
way we can have stacking UI-overlays while the ones in the background
still get rendered. And this is how the final CustomGame class then
looks.

``` {.lang:java .decode:true}
import java.util.Stack;

import com.badlogic.gdx.ApplicationListener;
import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;

public abstract class CustomGame implements ApplicationListener {
  private Screen screen;
  private Stack overlays;

  @Override
  public void create() {
    overlays = new Stack();
  }

  @Override
  public void resize(int width, int height) {
    if (screen != null)
      screen.resize(width, height);

    if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.resize(width, height);

  }

  @Override
  public void render() {
    if (screen != null)
      screen.render(Gdx.graphics.getDeltaTime());

    if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.render(Gdx.graphics.getDeltaTime());

  }

  @Override
  public void pause() {
    if (screen != null)
      screen.pause();

    if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.pause();

  }

  @Override
  public void resume() {
    if (screen != null)
      screen.resume();

    if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.resume();

  }

  @Override
  public void dispose() {
    if (screen != null)
      screen.dispose();

    if (!overlays.isEmpty())
      for (Screen o : overlays)
        o.dispose();

  }

  public void setScreen(Screen screen) {
    if (this.screen != null)
      this.screen.hide();
    this.screen = screen;
    if (this.screen != null) {
      this.screen.show();
      this.screen.resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
    }
  }

  public Screen getScreen() {
    return screen;
  }

  public void addOverlay(Screen overlay) {
    overlays.add(overlay);
    overlay.show();
    overlay.resize(Gdx.graphics.getWidth(), Gdx.graphics.getHeight());
  }

  public void removeOverlay() {
    if (!overlays.isEmpty())
      overlays.pop().dispose();
  }

}
```

This is it for part 1. I don't want to let this get too long so in PART
2 of this post I'll be showing you what exactly we can do with this. If
you have any questions or suggestions, leave them in the comments below.

Until then, keep Coding!

 

==== EDIT ====

Do you want this series to get picked up again? Go here:
http://www.spacekookie.de/continue-libgdx-game-of-codes/
