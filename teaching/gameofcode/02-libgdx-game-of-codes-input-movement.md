Title: 02. (LibGDX) Game of Codes: Input & Movement
Date: 2013-12-18 18:45
Category: Game of Codes
Tags: Guides
Slug: 02-libgdx-game-of-codes-input-movement
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we learned how to set up LibGDX in our
Java project and draw pictures onto the screen. We used Textures to
import the image and then drew a Sprite from a specific TextureRegion.
This would allow for multiple assets to be saved in a single texture and
thus saving time when loading assets.

In this edition I want to show you LibGDXes abilities to handle input
and move things on the screen. This will be all very basic but hang in
there with me. Let's begin.

Two ways of registering input
-----------------------------

There are two ways to register input events. The first one is to
directly listen to input events in your main game loop and execute code
depending on what happens.  

[![input\_raw](http://www.spacekookie.de/wp-content/uploads/2013/12/input_raw.png)](http://www.spacekookie.de/wp-content/uploads/2013/12/input_raw.png)

 

The other method is to create an input processor that sorts through all
the input (not just certain types), allows for more complex features
(like dragging gestures on Android)

 

![input\_handler](http://www.spacekookie.de/wp-content/uploads/2013/12/input_handler.png)

For now, we'll just use the first method. It'll make the process of
input handling very clear. In the second part of this tutorial we'll
have a look at input processor that are mostly needed for mouse and
gesture tracking.

 

Listening for simple button events
----------------------------------

The easiest way to listen for a button-pressed event is by calling

``` {.lang:java .decode:true}
Gdx.input.isKeyPressed(Keys.W)
```

where Keys is an enum index that contains all keys on a regular
keyboard, excluding international characters (Like Ö, æ or å). This
method returns a boolean that can simply be the argument of an
if-statement:

``` {.lang:java .decode:true}
     if (Gdx.input.isKeyPressed(Keys.W)) {
        }
```

Will run, when the a-key is pressed, if we put this into our games
"render" method. By polling the state of the boolean for the Key "W"
every frame we can get its status whenever the game is running. However
note that this is getting the value indirectly. When a button is pressed
this triggers an event listener to set the boolean to "true" and to
"false" again, once the listener detects that the button has been
released.

But back to our example. In our case we want the spaceship to fly up,
whenever the "W" key is pressed. Let's take a look at the render method
of our game.

``` {.lang:java .decode:true}
 @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

        batch.setProjectionMatrix(camera.combined);
        batch.begin();
        sprite.draw(batch);
        ship.draw(batch);
        batch.end();
    }
```

We already use the "ship" sprite in the method. All we need to do now is
update the position before drawing it onto the screen. Unfortunately
there is no direct way to add values to the position of a sprite, only
to overwrite it. So we need to fetch the position first, add our desired
value and then set that new position. The code for that looks something
like that (using the example above where we want the "W" Key to move the
ship up):

``` {.lang:java .decode:true}
if (Gdx.input.isKeyPressed(Keys.W)) {
            Vector2 updated = new Vector2(ship.getX(), ship.getY() + 5);
            ship.setPosition(updated.x, updated.y);
        }
```

Now compile this and press the "W" key and watch what happens. The ship
is moving up. Why? Because with each frame it is being checked if the
"W" key is pressed and if that is the case we add 5 pixels to the
Y-coordinate of the ship sprite.

We can now continue and do this for all four directions:

``` {.lang:java .decode:true}
 @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

        if (Gdx.input.isKeyPressed(Keys.W)) {
            Vector2 updated = new Vector2(ship.getX(), ship.getY() + 5);
            ship.setPosition(updated.x, updated.y);
        }
        if (Gdx.input.isKeyPressed(Keys.S)) {
            Vector2 updated = new Vector2(ship.getX(), ship.getY() - 5);
            ship.setPosition(updated.x, updated.y);
        }
        if (Gdx.input.isKeyPressed(Keys.D)) {
            Vector2 updated = new Vector2(ship.getX() + 5, ship.getY());
            ship.setPosition(updated.x, updated.y);
        }
        if (Gdx.input.isKeyPressed(Keys.A)) {
            Vector2 updated = new Vector2(ship.getX() - 5, ship.getY());
            ship.setPosition(updated.x, updated.y);
        }

        batch.setProjectionMatrix(camera.combined);
        batch.begin();
        sprite.draw(batch);
        ship.draw(batch);
        batch.end();
    }
```

Note that the "updated" vector is only a local variable inside the
if-statement and can't be used outside of it. Re-using the name inside
each if-block won't have any weird side effects or break the code.

If you now compile this you'll see that you can move the ship around on
both axis and in all directions but this isn't really a great game yet.
Why? Well...while this might be enough for a retro-side-scroller where
the player only faces up (down) or right (left) for tall intention
purposes, we want the ship to fly around more realistically. So it's
time to introduce rotation to our little game.

As you might have expected we can simply choose two other keys on our
keyboard (let's take Q and E) and use them to check for other if
statements. In addition to that there is a sprite-method called
"rotate". It should be fairly obvious now :)

``` {.lang:java .decode:true title="Add this to your render() method!"}
       if (Gdx.input.isKeyPressed(Keys.Q)) {
            ship.rotate(-5f);
        }
        if (Gdx.input.isKeyPressed(Keys.E)) {
            ship.rotate(5f);
        }
```

And that's it. Compile and see what happens. Fly around a bit. I'll be
waiting here.

------------------------------------------------------------------------

Oh. You're back quickly. Do I see a hint of disappointment on your face?
:) That's okay. See…we might have changed the rotation in the code,
however the displacement vectors (aka the direction that the ship will
be moved into) isn't in correlation with the rotation, just x and y
values. So the rotation doesn't matter, pressing "W" will move the ship
up, etc.

Now...there is an easy way to do this and a hard one. I want you to be
familiar with the mathematical basics first before I show you the easy
way.

[caption id="" align="aligncenter"
width="256"]![libgdx1\_vectoring](http://www.spacekookie.de/wp-content/uploads/2013/12/vectoring.png)
x = tan(α) \* y[/caption]

For each movement the angle of the ship needs to be considered before
moving the ship into the direction of the rotation-vector. Now the easy
way:

First create a new global vector that holds the speed of the ship and
the direction that the speed should be applied to. In this case 5 pixels
on the Y-axis.

``` {.lang:java .decode:true}
Vector2 move = new Vector2(0f, 5f);
```

Now you need to add a bit of code to the if-statement that checks if the
"W" key is pressed.

``` {.lang:java .mark:3 .decode:true}
  if (Gdx.input.isKeyPressed(Keys.W)) {
        Vector2 temp = new Vector2(ship.getX(), ship.getY());
        temp.add(move);
        ship.setPosition(temp.x, temp.y);
    }
```

We're almost done. The last thing we need is to actually rotate the
movement vector by the amount that the ship has rotated.

``` {.lang:java .mark:2 .decode:true}
  if (Gdx.input.isKeyPressed(Keys.A)) {
        move.rotate(5f);
        ship.rotate(5f);
    }
```

You can adjust the if-statement to check if the "S" key is pressed but I
removed it from my code for now.

So this is the full code

``` {.lang:java .mark:1,9,13-14,17-18 .decode:true}
Vector2 move = new Vector2(0f, 5f);

@Override
public void render() {
    Gdx.gl.glClearColor(1, 1, 1, 1);
    Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);
    if (Gdx.input.isKeyPressed(Keys.W)) {
        Vector2 temp = new Vector2(ship.getX(), ship.getY());
        temp.add(move);
        ship.setPosition(temp.x, temp.y);
    }
    if (Gdx.input.isKeyPressed(Keys.A)) {
        move.rotate(5f);
        ship.rotate(5f);
    }
    if (Gdx.input.isKeyPressed(Keys.D)) {
        move.rotate(-5f);
        ship.rotate(-5f);
    }

    batch.setProjectionMatrix(camera.combined);
    batch.begin();
    sprite.draw(batch);
    ship.draw(batch);
    batch.end();
}
```

Compile the game and enjoy flying around a bit. This is a very elegant
way to handle rotation of an object because the movement logic (move
vector) is disconnected from the rendering logic (Sprite).

One last thing I want to add in this post is some eye candy. In the next
post we'll have a look at the InputAdapter and get some mouse
interaction into our game.

First you should add three more texture regions: shipIdle, shipFly1 and
shipFly2 and refactor the code for the textures and the regions a bit to
be less confusing. My refactored code below as reference but you don't
have to do it exactly as I do.

``` {.lang:java .mark:4-6,22-27 .decode:true .crayon-selected}
public class TutorialLauncher implements ApplicationListener {
    private OrthographicCamera camera;
    private SpriteBatch batch;
    private Texture background;
    private Sprite space, ship;
    private TextureRegion shipIdle, shipFly1, shipFly2;

    @Override
    public void create() {
        float w = Gdx.graphics.getWidth();
        float h = Gdx.graphics.getHeight();

        camera = new OrthographicCamera(w, h);
        batch = new SpriteBatch();

        background = new Texture(Gdx.files.internal("space.jpg"));
        background.setFilter(TextureFilter.Linear, TextureFilter.Linear);
        TextureRegion region = new TextureRegion(background, 0, 0, 800, 600);
        space = new Sprite(region);
        space.setPosition(-space.getWidth() / 2, -space.getHeight() / 2);

        shipIdle = new TextureRegion(new Texture(
                Gdx.files.internal("USS_Pixel/ship_idle.png")), 0, 0, 64, 64);
        shipFly1 = new TextureRegion(new Texture(
                Gdx.files.internal("USS_Pixel/ship_fly1.png")), 0, 0, 64, 64);
        shipFly2 = new TextureRegion(new Texture(
                Gdx.files.internal("USS_Pixel/ship_fly2.png")), 0, 0, 64, 64);

        ship = new Sprite(shipIdle);
    }

    @Override
    public void dispose() {
        batch.dispose();
        background.dispose();
    }
```

So we're essentially creating three TextureRegions and mapping the
different pictures of the USS Pixel to it. Lastly, we want the game to
randomly pick one of these three textures when the ship is flying around
to generate an animation effect. For that purpose you should change some
code in the if-statement that checks whether the "W" key is pressed.

``` {.lang:java .mark:11-20 .decode:true}
  @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

        if (Gdx.input.isKeyPressed(Keys.W)) {
            Vector2 temp = new Vector2(ship.getX(), ship.getY());
            temp.add(move);
            ship.setPosition(temp.x, temp.y);

            int i = new Random().nextInt(2);
            if (i == 0)
                ship.setRegion(shipIdle);
            else if (i == 1)
                ship.setRegion(shipFly1);
            else if (i == 2)
                ship.setRegion(shipFly2);

        } else {
            ship.setRegion(shipIdle);
        }
```

Now compile this and enjoy.

![LibGDX\_stargame\_1](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-18-at-19.59.03.png)

You should now know how to handle basic keyboard input, how to properly
process it and also to move things on the screen more intelligently than
just to adjust their pixel coordinates manually. In the next issue I
want to introduce you to the InputAdapter but I feel that it would drag
this post out too much. So until next time, keep coding.
