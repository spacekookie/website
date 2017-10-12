Title: 07. (LibGDX) Game of Codes: User Interfaces and the power of Scene2D
Date: 2014-01-14 21:31
Category: Game of Codes
Tags: Guides
Slug: 07-game-of-codes-user-interfaces-and-the-power-of-scene2d
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we added new features to our game and
learned that the best step forward is often a step to the side (or back)
to get a view over what's going on. In this tutorial I want to show you
something that has absolutely nothing to do with features but will be
among the most important things in the game: the UI. We'll talk about
stages (like the acting stages, not rocket stages), UI elements and
something called Scene2D. Let's begin!

Any game will be composed of several layers. In the background you want
to draw a map or textures to let the players know where they are
(relatively). In the actual scene you want to draw all sorts of objects
including the player themselves to show what's going on. And in the
foreground you want to draw the UI with which the player can interact to
manipulate the game. Sure, we already have our input listeners set up in
a way that we can manoeuvre around our ship. But what about a UI?
Buttons? An inventory? This is something we'll tackle in this tutorial.
It's gonna be a long one too so be sure to bring some time and maybe
re-read it at a later point again.

In LibGDX we can use a UI-package called "Scene2D" which is perfect for
anything UI. It uses a layer of our game called the "Stage" that will be
populated by "Actors". In the beginning we'll stick with standard actors
but we can soon expand and write our own Actors by expanding that
superclass and doing own things with it. The stage will gladly welcome
our new Actor object into its ranks and manage everything there is to
manage about it. Just like our world-class. So you can see that it's
always a good idea to implement a managing parent class, followed by a
bunch of child objects.

![Scene2D](http://www.spacekookie.de/wp-content/uploads/2014/01/Screen-Shot-2014-01-13-at-17.08.28.png)

But before we get some stuff done with Scene2D and the stage I need to
explain you a few things about skins. A skin is a way to tell the game
how a UI should look. It includes fonts, graphics and textures to
describe how things have to be drawn. And creating beautiful skins is a
tutorial of its own (with which I'm honestly not very familiar. I'm a
programmer, not a designer ;) ). But luckily the creators of LibGDX
provide us with a standard skin that we can just download and use. It's
not exactly pretty and I wouldn't recommend using it in your games end
release. But it'll get the job done until then. And if you at a later
stage decide that you want to use your own skin, you will only have to
change the skin files and everything else remains the same. Pretty cool,
eh?

------------------------------------------------------------------------

So first off we'll need some files that make up the skin:

[A
FONT](https://github.com/libgdx/libgdx/blob/master/tests/gdx-tests-android/assets/data/default.fnt)

[AND IT'S
RESOURCE](https://github.com/libgdx/libgdx/blob/master/tests/gdx-tests-android/assets/data/default.png)

[A TEXTURE
FILE](https://github.com/libgdx/libgdx/blob/master/tests/gdx-tests-android/assets/data/uiskin.png)

[AND IT'S
ATLAS](https://github.com/libgdx/libgdx/blob/master/tests/gdx-tests-android/assets/data/uiskin.atlas)

[A JSON
FILE](https://github.com/libgdx/libgdx/blob/master/tests/gdx-tests-android/assets/data/uiskin.json)

(To actually download the text-files just view their content in "Raw"
and copy them into a text editor of your choice. However use something
that let's you set your own file types. TextWrangler or TextMate on macs
and Notepad++ on Windows)

------------------------------------------------------------------------

Download these from the LibGDX github repository. In general, if you're
ever stuck or want to look at some samplecode or just get to know what's
under the hood of the latest nightly build, check the github repository
for answers. It's a great tool! Put them all into a new folder in your
assets directory called "Skin" or something and then go into your
Resource packer class and create a new public final static object there.

``` {.lang:java .decode:true}
  public static final Skin _SKIN = new Skin(Gdx.files.internal("data/skin/uiskin.json"));
```

And that's that. LibGDX will do the rest. From now on, every time we
want to use anything related to the UI we will have to pass in this skin
to make it work (and look the same as the rest of the game). Now we'll
be doing some stuff in LibGDX's Scene2D. It's all very basic but
necessary to understand. Again...I might not cover everything. But if
you google "Scene2D + anything" you'll find your answers quite quickly.
90% of coding: googling how to do things :)

Basics of Tables
----------------

We'll want to go into our main game class and create a new object called
"Stage". Make it private and initialize it just after the camera. And
then set the viewport in the resize method. Confused? Look below.

``` {.lang:java .decode:true}
  /** UI */
  private Stage stage;

  @Override
  public void create() {

    . . .

    /** UI */
    stage = new Stage();

    . . .

  }
    . . .

  @Override
  public void resize(int width, int height) {
    stage.setViewport(width, height);
  }
```

This way the stage will be resized every time we resize the viewport of
the game. Which currently is only at launch because we don't allow for
user resizes. But that could change. That's a pretty good idea, we
should actually do the same with our camera. So remove our two variables
"w" and "h" and move "camera.setToOrtho(...)" to the resize method so it
looks like this.

``` {.lang:java .decode:true}
  @Override
  public void resize(int width, int height) {
    stage.setViewport(width, height);
    camera.setToOrtho(false, width, height);
  }
```

Now...enough spontanious refactoring, let's actually get into our
tables. The stage itself is an invisible object, much like our world. It
won't draw anything unless we actually add some actors and then act out
the stage in our render method.

Why don't we create a button that says "Menu" in the top-right corner? I
think that's a nice start to our UI and actually useful. In LibGDX there
are many button implementations, including some with pictures and an
abstract type that you can implement your own types on. But the regular
"TextButton" is sufficient for us at this time. So go create a global
variable of the type TextButton, give it a name and then, after
initializing the stage, initialize the button. How? Like this.

``` {.lang:java .mark:1,10 .decode:true}
  private TextButton menu;

  @Override
  public void create() {

    . . .

    /** Setting up the UI */
    stage = new Stage();
    menu = new TextButton("Menu", ResPack._SKIN);

    . . .
  }
```

You can see that the button wants a string to display on itself and of
course a skin. So far so good. But how do we tell it to go to the
top-right corner of the screen? Well...that's not so simple and I
actually want to show you this way first so you NEVER think about doing
this manually again :) We will need to take the size of the stage and
then substract the size of the button from it and set that as its new
position.

``` {.lang:java .decode:true}
 menu.setPosition(stage.getWidth() - menu.getWidth(), stage.getHeight() - menu.getHeight());
    stage.addActor(menu);
```

Pretty complicated, eh? That second line adds the menu-button to the
stage. It's essentially the same thing that we're doing with our world:
creating a bunch of objects and passing them into a large-scale manager.
But, if you remember correctly, our world needs something in the render
method to work. And the same applies to our stage. First we need to act
out the stage which means moving things that need to be moved, animating
things that need to be animated, etc. And then draw the stage. So in our
render method we add.

``` {.lang:java .decode:true}
 stage.act();
    stage.draw();
```

Be sure to put this at the very bottom of our rendering so that it ends
up on TOP of our stack. (Laying a stack of papers, the sheet you put
onto it first will be on the bottom (the background) while the one you
put on last will be on top (the UI).

![StarChaser\_UI\_Test1](http://www.spacekookie.de/wp-content/uploads/2014/01/Screen_Shot_2014-01-12_at_11_14_13-2.png)

Now compile this and marvel at its glory. Well...kind of. See...when we
now need to add a second button to that menu maybe titled "Inventory"
we'll have to do very complicated mathematics in order to line up the
buttons. Which isn't great and which is why Tables were created.

Just after creating your button, why don't you go and create a "Table"
object, initialize it after the stage and then add the button to the
table and the table to the stage.

``` {.lang:java .mark:1,10,12-13,16 .decode:true}
  private Table buttons;

  @Override
  public void create() {

    . . .

    /** Setting up the UI */
    stage = new Stage();
    buttons = new Table(ResPack._SKIN);

    buttons.setFillParent(true);
    buttons.top().right();

    menu = new TextButton("Menu", ResPack._SKIN);
    buttons.add(menu);

    stage.addActor(buttons);
```

So instead of adding the button to the stage we add it to the table, we
tell it to fill its parent (which is important for the validation of the
table during render) and then call "top" and "right"...see, instead of
working with pixel coordinates here we can just tell the table to go to
any corner of the window (center, top, bottom, left, right). And the
coolest thing is that the table will try to stay on-screen, even if we
add more buttons. Let's do that now honestly, create a new button called
"Inventory" and add it to the table just as the menu button. Note that
the table will be populated from left to right meaning that if you want
the Inventory button to be to the left of the menu button you'll have to
add it first.

And that's that for tables for now. There are more advanced things
concerning tables but I won't cover them here (and now). If you're
curious or this isn't specific enough for what you have planned, why
don't you go [here](https://github.com/EsotericSoftware/tablelayout) and
read about it :)

Handling input
--------------

Something you might have noticed is that our current buttons don't react
to any kind of input. That has to do with the fact that we never
register the stage as an input processor. Usually you call
Gdx.input.setInputProcessor(stage) but as we already have an input
multiplexer set up we can just add the stage to that.

``` {.lang:java .decode:true}
 plex.addProcessor(stage);
```

And voila you'll see that the buttons now react to our clicks, even with
just a red glow. Because to actually HANDLE the input we need something
to listen to it. In our input processors we have listeners to certain
events, like moving the mouse or pressing a certain button. And we use
these events to manipulate our game. For the UI it's no different.
Well...it's slightly different. We don't want to create a UI
InputProcessor. It's not only completely ridiculously complicated but
actually inadvisable. Instead we'll set up the listeners for each button
manually in our game class and tuck them away in a method somewhere at
the bottom of the class to be out of sight and out of mind.

``` {.lang:java .decode:true title="Clicklistener - innertype"}
  private void setupListeners() {
    menu.addListener(new ClickListener() {

      public void touchUp(InputEvent event, float x, float y, int pointer, int button) {
        Gdx.app.log("Stage", "Menu button pressed");
      }
    });
  }
```

What you see above is known as an inner-type. If you've worked with my
Android series before you'll know them. it's essentially a way to create
a class inside another class (in the parameter brackets of a method) to
define how a passed down to the "addListener" method.

The ClickListener extends the InputListener where we can manually
override one of the listeners. In my case I decided to override the
"touchUp" method with all the parameters it takes and log the case. Now
create a second listener for the second button, just as the one I showed
you above. Compile it and see what happens. Pretty cool, eh (again)?

Okay, maybe not that cool. Initially I wanted to go on here and make
options and inventory screens but I think we should do this at a later
time because it would take hours and not really have anything to do with
Scene2D anymore. Let's just check out some other elements we have in
Scene2D before wrapping this up.

So create a new table with a name of your choosing and add a few thing
to it.

``` {.lang:java .decode:true}
 temp = new Table(ResPack._SKIN);
    temp.setFillParent(true);
    TextureRegionDrawable trd = new TextureRegionDrawable(new TextureRegion(new Texture(
        Gdx.files.internal("graphics/image_button.png"))));
    imageButton = new ImageButton(trd);
    checkbox = new CheckBox("This is a checkbox", ResPack._SKIN);
    field = new TextField("This is a textfield", ResPack._SKIN);

    temp.add(imageButton);
    temp.row();
    temp.add(checkbox);
    temp.add(field);
    temp.top().left();
    stage.addActor(temp);
```

Oh boy, I know. Let's go trough it line by line. Temp is just a table
that we set to fillparent = true. The next thing we do isn't really
important for now, just note that we're doing it. A
TextureRegionDrawable extends a Drawable that we need for our button.
Ideally you want to have all your button images in your skin. But the
default skin doesn't. So because I didn't want to add stuff to the skin
I went with the "hard" but quick way. Afterwards we initiate a checkbox
and a textfield.

[![image\_button](http://www.spacekookie.de/wp-content/uploads/2014/01/image_button.png)](http://www.spacekookie.de/wp-content/uploads/2014/01/image_button.png)

Note how we're adding things to the table and using "row()" only once.
Each time you call row() it will create a new row. So in effect the
first item will be on it's own row and then the checkbox and textfield
on another. If you put another row between them that will change of
course. Above you have the button image that I used. Go import that into
your project if I want it to work OR of course just create your own
Button image.

I hope that this tutorial has shown you how powerful Scene2D can be.
With just a few lines of code we created a whole layout and added
listeners to it. The process remains that easy and you ca of course
still add and subtract offsets to tables to fine-tune their position. If
you have further questions about Scene2D, go ahead and post them below.
But in general the API is relatively well documented and if you have
questions you can always check out the LibGDX forums or the IRC.

Thats it for today, I'll continue with this next time but we'll have our
focus on something called Screens. They're nifty little things that can
make our life a whole lot easier (and more difficult actually ;) ).  
I actually wanted to do something \*slightly\* different today (that
involved computer hardware) but I actually ordered a wrong part. So
that'll be delayed. Not sure when it'll come out.  So until next time,
keep coding.
