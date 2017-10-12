Title: 08. (LibGDX) Game of Codes: Screens & Subscreens
Date: 2014-01-19 09:30
Category: Game of Codes
Tags: Guides
Slug: 08-libgdx-game-of-codes-screens-subscreens
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we looked at user interfaces with Stages
and Scene2D. Today I want to show you how to make your game a LOT better
and more functional by adding *Screens *(I already spoiled this last
tuesday ;) ). Let's begin!

First of all we should take a step back and look at our game. We have
our main-game class that currently extends "ApplicationListener" and
does a whole lot of stuff. It's the main game loop, it populates and
updates the world and handles input. So essentially it's a class that is
tied into everything that LibGDX does to make a game runnable. Well...an
"Application". That's a very broad term and there is another subclass of
that main class that we currently extend, that we need to use in the
future. it's almost the same as the ApplicationListener but \*slightly\*
different. And we need that. The class is called "Game". So what I want
you to do now is go into the main "Game" class and change the extend
from "ApplicationListener" to "Game". In my case it's the line below.

``` {.lang:java .decode:true}
public class StarChaser extends Game {
```

Eclipse might give you some trouble with implementing the new methods.
Usually you just have to clean your project (Project --\> Clean --\>
All) and it'll calm down. In the worst case scenario just copy all your
code into a different editor, delete all the code from the class (except
the class definition and package of course, let Eclipse import
everything for you again, implement the methods and then paste your code
into the methods it create (that will be EXACTLY the same as the ones we
had before. But you know...Eclipse is weird sometimes :) ).

What did this get us? Well...if you added the sources to your Libraries
you can right-click that "extends Game" and show it's declaration to see
the Game class that we now extend. It extends the ApplicationListener
and adds something we want to use now: a *Screen!*

A screen is a layer of our game. It gets shown, rendered, paused and
destroyed. It acts very much like a fragment on Android (if you're
familiar with the Android API) and can be an overlay or replacement of
the entire game. using screens is a much better solution in switching
between "screens" than creating new games or trying to use a lot of
booleans and flags to determine what part of which GUI is supposed to be
visible.

So why don't you go and create a new package called "screens" and add a
new class to it and let it implement "Screen". I called mine
"MenuScreen".

``` {.lang:java .decode:true}
package de.spacekookie.starchaser.screens;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.Screen;
import com.badlogic.gdx.scenes.scene2d.Stage;

public class MenuScreen implements Screen {

  /** UI */
  private Stage stage;

  @Override
  public void render(float delta) {
    stage.act();
    stage.draw();
  }

  @Override
  public void resize(int width, int height) {
    stage.setViewport(width, height);
  }

  @Override
  public void show() {
    stage = new Stage();
  }

  @Override
  public void hide() {

  }

  @Override
  public void pause() {

  }

  @Override
  public void resume() {

  }

  @Override
  public void dispose() {

  }

}
```

This is what your class should look like (more or less). I took the
liberty of already adding a stage to it because we want to draw a menu
screen, something with buttons and text and the easiest way to do that
is with Scene2D (as we've learned in the last tutorial).

Next up we'll want to populate that stage. I prepared something and am
just gonna paste it in here. You can arrange your buttons in whatever
order you want. I went for something very simple and centric.

``` {.lang:java .mark:25 .decode:true}
  @Override
  public void show() {
    stage = new Stage();

    table = new Table(ResPack._SKIN);

    table.setFillParent(true);
    table.center();

    title = new Label("MAIN MENU", ResPack._SKIN);
    title.setFontScale(2.5f);

    resume = new TextButton("RESUME GAME", ResPack._SKIN);
    options = new TextButton("OPTIONS", ResPack._SKIN);
    exit = new TextButton("RAGE QUIT", ResPack._SKIN);

    table.add(title).center().pad(25f);
    table.row().height(75);
    table.add(resume).center().width(500).pad(5f);
    table.row().height(75);
    table.add(options).center().width(500).pad(5f);
    table.row().height(75);
    table.add(exit).center().width(500).pad(5f);
    stage.addActor(table);
    Gdx.input.setInputProcessor(stage);
  }
```

You should understand what I'm doing here and it's nothing more advanced
than what we did in the last tutorial. Except that I set a row height,
give buttons a specific size and add padding around them to make it look
more smooth.

<span style="text-decoration: underline;">Note how we overwrite the
input processor from the main game to the stage. This means that the
game will be unresponsive, We'll have to change that back later!</span>

So far so good. But what do we now actually do with this? We want to add
this screen to the main game class in a way that we don't have to create
new instances of it all the time. So go ahead and create a global
variable in the main game class and initialize it on create().

``` {.lang:java .decode:true}
 /** Screens */
  private MenuScreen menuScreen;

  @Override
  public void create() {

    . . .

    /** Setting up support screens */
    menuScreen = new MenuScreen();

    . . .
  }
```

And another global variable we'll have to create is "self" which has the
type of our main game class (which in my case is "StarChaser"). We can
do that by creating an object with the class name and initializing it
with the following.

``` {.lang:java .decode:true}
  private StarChaser self = this;
```

We will need this global variable in our click-listener, because
there the scope is different. See, while we can easily call "this" or
"super" in our main game class to access anything in the class or that
we inherit from, in the Clicklistener we're technically in a different
class (the ClickListener class) and thus we can't access things we
inherited outside of it. To circumvent this we add a global variable
that we can still see, access and Boya!

In the ClickListener you can throw out the Log call and add this.

``` {.lang:java .decode:true}
self.setScreen(menuScreen);
```

When you now compile this you'll see that you don't see anything. :)
Because we're not actually rendering the screen. For that to happen you
have to add this line of code to the bottom (the very end) of your
render() method (in the main game class that is).

``` {.lang:java .decode:true}
super.render();
```

This will ensure that if there is a screen visible that their
appropriate render method is being called at the right time (You can
look at the super-render() method when you look at the super-class. It's
sometimes interesting).

Now compile this and see, that we have a neat overlay of our buttons
over the game. And we can no longer move our ship around and we're also
kinda stuck in that menu screen because we haven't set up any listeners
yet. Now...resetting the screen works in a very similar way: we take our
main game, call setScreen(null) on it and the screen will disappear.
However...we don't have that inheritance in our Screen object, do we?
No. So we'll have to pass it in via the constructor.

So first we create a constructor in the MenuScreen class.

``` {.lang:java .decode:true}
  public MenuScreen(StarChaser self) {
    this.parent = self;
  }
```

And of course a global variable in the class called "parent" or
"cupcake" or whatever you want to store the information. Also make sure
to update the constructor call (in the ClickListener) from no parameters
to "self".

With this new variable in our screen we can go ahead and create a new
Clicklistener for one of our lovely buttons. I only chose the "Resume"
one for now but we can add functionality to the other ones as we move
along with our game.

``` {.lang:java .decode:true}
 resume.addListener(new ClickListener() {

      public void touchUp(InputEvent event, float x, float y, int pointer, int button) {
        parent.setupInput();
        parent.setScreen(null);
      }
    });
```

You'll probably go "Woooah, easy there girl, what's that setInput()??"
and well...you're right. See, when we get back to our game and the
screen is hidden somewhere in memory we can't control the game anymore.
We haven't told our game yet that we want to resume using the input
Multiplexer so that we can actually control our ship again.

For that to happen I created this public method that sets the input to
the Multiplexer and sets up the Stage-listeners (for our buttons). In
the main game simply call this method instead of the actual calls (so
after adding things to the Multiplexer). Because the InputAdapters still
exist in memory, we don't want to re-initialize them. That'd be a waste
of resources and memory.

``` {.lang:java .mark:10,13-17 .decode:true}
  @Override
  public void create() {

    . . .

    /** Input Controllers */
    plex.addProcessor(stage);
    plex.addProcessor(camController);
    plex.addProcessor(handler);
    this.setupInput();
  }

  public void setupInput() {
    Gdx.input.setInputProcessor(plex);
    this.setupListeners();
  }
```

And that's it. If you compile this you'll have a functional button that
takes you to the MenuScreen and back again when you press the
appropriate button. I hope you understand the logic behind this. We show
a screen, we use it, we hide it. Think of the screens like overlays that
you put over your main "game-layer". But just because we can
conveniently draw over our main layer that doesn't mean that we won't
have to change a few things, pass parameters along and manually reset
the input (as an example). LibGDX is a framework that allows for the
complicated stuff to be easy (the drawing a new screen over the current
game etc.). The rest is up to you, how you want to handle it, how you
want your game (or just application) to look. Below is a picture that
shows the current setup we have.

![rt7obekn-1](http://www.spacekookie.de/wp-content/uploads/2014/01/rt7obekn-1.jpg)

Speaking of looks...I don't actually like how that menu screen is
looking. I'd much rather have it be semi-transparent in the background
so the game gets grayed out. Luckily that's easily possible.
Well...possible :)

First you should create a Camera object in our MenuScreen and get the
camera from the main game in the constructor. (We already have a static
method called "getCameraInstance()" that we used a couple of issues back
for our input processor to do things. After that create a
"ShapeRenderer" and initialize it in the "show()" method.

``` {.lang:java .mark:1,2,5,13 .decode:true}
  private Camera camera;
  private ShapeRenderer render;

  public MenuScreen(StarChaser self) {
    this.camera = StarChaser.getCameraInstance();
    this.parent = self;
  }

  . . .

  @Override
  public void show() {
    render = new ShapeRenderer();

    . . .

  }
```

ShapeRenderers are used to draw very simple polygon shapes onto the
screen. In our case we want a rectangle, filled with a colour, that
spans over the entire screen (+10 pixels or so for border) and blends
the background colours with our colour that we give an alpha channel.
Confused? Don't worry, check out the code below (the new render method)
and then I'll go over it bit by bit.

``` {.lang:java .decode:true}
  @Override
  public void render(float delta) {

    Gdx.gl20.glEnable(GL20.GL_BLEND);
    render.setProjectionMatrix(camera.combined);
    render.begin(ShapeType.Filled);
    render.setColor(0, 0, 0, 0.5f);
    render.rect(-10, -10, Gdx.graphics.getWidth() + 20, Gdx.graphics.getHeight() + 20);
    render.end();

    stage.act();
    stage.draw();
  }
```

First we have to call an OpenGL function called "glEnable" which will
enable certain features during render. We pass in the "GL\_BLEND"
parameter (in the GL2.0 package) which will trigger OpenGL to blend
colours together (so allowing two colours to merge slowly instead of
being absolute values).

Afterwards we take the projection matrix from our camera and set it for
the renderer so that the drawn shapes are in the same reference frame as
the rest of our game. And then we begin the magic.

We set the Type (Filled), we set a colour (black with 50% alpha), we set
the border (the screen + 10 pixels padding over the screen). And then we
end the renderer. That's it.

Compile this and look at how it looks. In my opinion a lot better! For
reference, this is what my menu now looks like. Again...you can have
your buttons in different orders, sizes, whatever.

![StarChaser\_Menu](http://www.spacekookie.de/wp-content/uploads/2014/01/Screen-Shot-2014-01-19-at-10.57.46.png)

But I hope you understand now how you can create different screens to
make have different tasks. And in the same way that we've now created
this Menuscreen we can make an options screen (We just need to pass
along the Game again and call "setScreen(whatever)" when we're done).

And at some point I want to make an inventory and trade screen like
this. But that's a long way out. Because next up I actually want to do
some bug-fixing. Things that I missed a few "episodes" ago and thought
it'd be a good learning opportunity. And also teaching you about game
structure a bit more.

I hope you enjoy this series so far, leave me your feedback in the
comments and I'll see you guys (and gals) next time. Keep coding!
