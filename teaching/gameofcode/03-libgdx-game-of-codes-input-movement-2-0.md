Title: 03. (LibGDX) Game of Codes: Input & Movement 2.0
Date: 2013-12-19 13:12
Category: Game of Codes
Tags: Guides
Slug: 03-libgdx-game-of-codes-input-movement-2-0
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we learned how to listen for keyboard
input, move things on the screen and do some basic game logic with
vectors. In this issue I want to re-touch that subject, but in a more
advanced manner. This time we'll have a look at InputProcessors and
their ability to listen for any kind of input, including mouse and
touchscreen gestures. If you haven't already worked through the last
issue of this tutorial series, you should do that
[now](http://www.spacekookie.de/02-libgdx-game-of-codes-input-movement/ "02. (LibGDX) Game of Codes: Input & Movement")!
I'll wait here.

Oh, you stayed. Well then, let's get started.

 

First of all we'll want to create a new class that extends the
InputAdapter.

``` {.lang:java .decode:true}
package de.spacekookie.libgdxtutorial;

import com.badlogic.gdx.InputAdapter;

public class InputHandler extends InputAdapter {

}
```

You can name yours whatever you want, I chose InputHandler, as for any
managing class that HANDLES things in my software :) Handlers and
Dealers, the criminal underworld in my source code is real.

We will add things to this class later, first of all we should tell our
game that it exists. And we can do that by adding the following code
into the games creation method.

 

``` {.lang:java .decode:true}
 private InputHandler handler;

    @Override
    public void create() {

        . . .

        handler = new InputHandler();
        Gdx.input.setInputProcessor(handler);

        . . .
    }
```

Great. Now that we told our game to actually use the InputAdapter we
created we can start and add some actual code to it. If you look at the
class that we're extending you can see a few methods that we can
override. Why don't you add this method to the InputAdapter class.

``` {.lang:java .decode:true}
 @Override
    public boolean keyDown(int keycode) {
        return true;
    }
```

Remember when I told you in the last post that polling
Gdx.input.isKeyPressed(. . .); was only an indirect way to get the
status of a key and would only react to a listener event? Well guess
what...that's an event listener that will react t ANY key-down event.
The keycode passed into the listener specifies the key in question.

Go ahead and check if keycode is the same as the integer representing a
key (Keys.\*) like SPACE.

``` {.lang:java .decode:true}
if (keycode == Keys.SPACE) {
    System.out.println("If this game had gravity I would want to JUMP!");
}
```

If you compile this you'll see that the game will of course still
recognize the inputs handled in the Games render() method but in
addition to that will react to keystrokes being handled in our
InputAdapter. However...we have a problem. To actually handle the input
in the Adapter we need to pass on some information into it. We can
either pass the Sprite along but I would say something much better is to
create a custom Object to hold all the important information to render,
move and manipulate the ship (or other entities we might add later). So
why don't you go ahead and create a new class called "Entity". I went
ahead and added some code to it to actually make it useful.

``` {.lang:java .decode:true}
package de.spacekookie.libgdxtutorial;

import java.util.Random;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.Sprite;
import com.badlogic.gdx.graphics.g2d.SpriteBatch;
import com.badlogic.gdx.graphics.g2d.TextureRegion;
import com.badlogic.gdx.math.Vector2;

public class Entity {

    public static enum EntityType {
        PLAYER, ENEMY;
    }

    public static enum ShipState {
        IDLE, MOVING, DEAD;
    }

    private EntityType type;
    private Sprite self;
    private TextureRegion shipIdle, shipFly1, shipFly2;

    private Vector2 moveVector = new Vector2(0f, 1f);
    private float speed = 5f;

    public Entity(EntityType type) {
        this.type = type;
        moveVector.scl(speed);
        loadResources();
    }

    public void loadResources() {
        if (type.equals(EntityType.PLAYER)) {
            shipIdle = new TextureRegion(new Texture(
                    Gdx.files.internal("USS_Pixel/ship_idle.png")), 0, 0, 64,
                    64);
            shipFly1 = new TextureRegion(new Texture(
                    Gdx.files.internal("USS_Pixel/ship_fly1.png")), 0, 0, 64,
                    64);
            shipFly2 = new TextureRegion(new Texture(
                    Gdx.files.internal("USS_Pixel/ship_fly2.png")), 0, 0, 64,
                    64);

            self = new Sprite(shipIdle);
        }
    }

    public void idle() {
        self.setRegion(shipIdle);
    }

    public void fly() {
        int i = new Random().nextInt(2);
        if (i == 0)
            self.setRegion(shipIdle);
        else if (i == 1)
            self.setRegion(shipFly1);
        else if (i == 2)
            self.setRegion(shipFly2);
    }

    /** Used to get access to methods */
    public Sprite getSelfSprite() {
        return self;
    }

    public Vector2 getMovement() {
        return moveVector;
    }

    public void setMovement(Vector2 moveVector) {
        this.moveVector = moveVector;
    }

    /** Will be called in the @render() method */
    public void draw(SpriteBatch batch) {
        self.draw(batch);
    }

}
```

If you actually look at the code you won't see anything you haven't seen
before. What I did was move all the texture loading, sprite setup and
region swapping when flying and idling into this class as well as
creating a few getters to access the information from outside the class.

The only two new things are the two enums, ShipState and EntityType
which will become more useful in the future. But laying the groundwork
now for a more complex game will become handy later.

Next up we need to take a look at the InputAdapter and change it in a
way that it uses flags on keyDown and keyUp (as in setting a flat to
"true" on down and "false" to up). Then move all the movement logic into
a method called "update()" that will be called in the games render()
method.

Here is my code as reference.

``` {.lang:java .decode:true}
package de.spacekookie.libgdxtutorial;

import com.badlogic.gdx.Input.Keys;
import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.math.Vector2;

public class InputHandler extends InputAdapter {

    private Entity entity;
    private boolean moving, clock, counterClock;

    public InputHandler(Entity entity) {
        this.entity = entity;
    }

    @Override
    public boolean keyDown(int keycode) {
        if (keycode == Keys.W) {
            moving = true;
        }
        if (keycode == Keys.A) {
            counterClock = true;
        }
        if (keycode == Keys.D) {
            clock = true;
        }
        return true;
    }

    @Override
    public boolean keyUp(int keycode) {
        if (keycode == Keys.W) {
            moving = false;
        }
        if (keycode == Keys.A) {
            counterClock = false;
        }
        if (keycode == Keys.D) {
            clock = false;
        }
        return true;
    }

    public void update() {
        if (moving) {
            Vector2 temp = new Vector2(entity.getSelfSprite().getX(), entity
                    .getSelfSprite().getY());
            temp.add(entity.getMovement());
            entity.getSelfSprite().setPosition(temp.x, temp.y);

            entity.fly();
        } else {
            entity.idle();
        }
        if (counterClock) {
            entity.getMovement().rotate(5f);
            entity.getSelfSprite().rotate(5f);
        }
        if (clock) {
            entity.getMovement().rotate(-5f);
            entity.getSelfSprite().rotate(-5f);
        }
    }
}
```

And the games render() method.

``` {.lang:java .decode:true}
 @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

        handler.update();

        batch.setProjectionMatrix(camera.combined);
        batch.begin();
        space.draw(batch);
        player.draw(batch);
        batch.end();
    }
```

Make sure to remove all calls from the main game class that we have
already moved to our Entity. And that's it. Compile this and see what we
made (a huge mess, I know).

So? Well done, we just remade what we already had, just in less
clustered and more shiny. But this isn't very impressive, is it now?
Sure this code looks much cleaner than before but InputAdapters are a
lot more powerful than that. Why don't you go ahead and add a new method
to our InputAdapter.

``` {.lang:java .decode:true}
 @Override
    public boolean mouseMoved(int screenX, int screenY) {
        System.out.println(screenX + " : " + screenY);
        return false;
    }
```

When you compile this you'll see the coordinates of your mouse output in
the console as you move the cursor over the game window. That's because
the listener is being called every time the mouse is moved and without
any further filtering it of course. Now it's gonna get rough, so put on
your thinking hats and try not to go mad. Because we'll have to go and
mock around with Vectors quite a bit and I will have to introduce you to
camera vectors already. I will only brush the subject here and retouch
it in a later version to go more in depth.

First up we need to change a few things in our main game class. First,
change the OrthographicCamera variable to "static".

``` {.lang:java .decode:true}
private static OrthographicCamera camera;
```

And then write a little getter for that camera variable that's also
static, so that we can access it without having to worry about a
constructor.

``` {.lang:java .decode:true}
 public static OrthographicCamera getCameraInstance() {
        return camera;
    }
```

 

Now, go ahead and create three more global variables in the
InputAdapter.

``` {.lang:java .decode:true}
 private boolean clicked;
    private Vector3 vec;
    private Vector3 target;
```

The boolean will be used to flag whether the mouse button has been
clicked and the ship is still en-route. The two 3D vectors will be used
to pinpoint the target we're trying to approach and the movement vector
that the ship will be using. They need to be Vector3 objects (3D
vectors) because they need to interact with our camera, which is a 3D
object. Don't forget! LibGDX is a 3D game development framework, so we
need to ignore the third dimension most of the time. Just set it to "0"!

Now we need to handle the mouse actions. Go and delete that line of code
from the mouseMoved method and create a touchDown() method. It will be
used to register mouse events but can also be used to register touches
on Android devices.

``` {.lang:java .decode:true}
 @Override
    public boolean touchDown(int x, int y, int pointer, int button) {
        if (pointer == 0) {
            if (button == 0) {

            }
        }
        return false;
    }
```

The pointer is "0" in case of the mouse but can be something else, when
we're dealing with touchscreen input. The button "0" is the left mouse
button, "1" is the right one. Nest those two if-statements, so that both
need to be true for our code to be executed. I will go through what we
do here line by line because it's not exactly trivial.

``` {.lang:java .decode:true}
vec = new Vector3(x, y, 0);
```

First we take that Vector3 (vec) we created before and put some
information into it. X and Y are the mouse coordinates that are passed
into the listener (where the click occurred) and put 0 for the
Z-Coordinate.

``` {.lang:java .decode:true}
TutorialLauncher.getCameraInstance().unproject(vec);
```

Next up, we need to call that static method we created in our main game
class to get the camera and call "unproject" onto it. Unprojecting means
associating a coordinate in the camera space with a pixel coordinate on
the screen. When the camera is moving around it will change the
coordinates quite drastically. So a camera coordinate (5000, 10000)
could still correlate to a pixel coordinate that's more like (255, 128),
etc. Unprojecting the camera and passing our Vector3 object into it
aligns the camera space with the pixel space on-screen. We WILL talk
about cameras and matrix projection in a later issue. For now, I hope
that this is at least somewhat clear.

Next up, store the unprojected vector in our target Vector3 that we
created, set the boolean and return from the method.

``` {.lang:java .decode:true}
target = new Vector3(vec);
clicked = true;
return true;
```

The target Vector3 will not change and serve as a reference where the
original click was made and when we want our ship to stop flying. We're
almost done. We already flag our button clicks in the listener, now we
just need to use that flag in our update() method that gets called every
frame.

``` {.lang:java .decode:true}
 if (clicked) {
        entity.fly();
    } else {
        entity.idle();
    }
```

You should understand what that does, just registering the clicked flag
and setting the textures accordingly.

``` {.lang:java .decode:true}
 Vector2 temp = new Vector2(entity.getSelfSprite().getX(), 
                        entity.getSelfSprite().getY());
```

Log the current position of our sprite and save it in the temp Vector.
And now it's getting kinda tricky. There is a Vector method called lerp,
which interpolated two vectors. We will touch Vectors again in a later
issue. If you want to read the mathematical principles of interpolation
you can click [here](http://en.wikipedia.org/wiki/Linear_interpolation).
(If you're masochistic like that).

``` {.lang:java .decode:true}
 temp.lerp(new Vector2(vec.x, vec.y), 0.1f);
    entity.getSelfSprite().setPosition(temp.x, temp.y);
```

Vec starts as the target and gets shorter and shorter as the temp vector
approaches the target more and more. Afterwards we do the normal jazz
and adjust the entities Sprite position with the new temp vector (which
isn't the target position but rather the first step on the way to the
target.

Lastly we need to deactivate the ships engines when the ship has reached
the target position (that's why we saved it in the target vector :) )

``` {.lang:java .decode:true}
 if (target.dst(temp.x, temp.y, 0) < 2)
        clicked = false;
```

Add this to the end of the if(clicked)-statement. dst(. . .) returns the
range between two vectors (target and temp, where we only look at the X
and Y coordinates) and we can then compare that range to a number, in my
case 2. So when the temp vector gets into a range of 2 pixels to the
target vector the if-statement is true and sets the clicked boolean to
"false" and stops moving the ship (and then the else-statement is called
and sets the texture to idle again). It also corrects the rotation
correction that we used before.

 

And that's that. Compile the game and try out the two methods of
movement we now have. Rotating the ship properly when clicking would be
too long and difficult for this tutorial so I left it out. (Well
actually rotating isn't too difficult but making the click-rotation and
the keyboard rotation compatible is a bit tricky).

What we did in this issue was refactor our input handling and add some
more code to interact with the game using the mouse. I don't know what
we'll touch on next but I think we'll end this issue here. I hope you
learned something and until next time, keep coding!

 
