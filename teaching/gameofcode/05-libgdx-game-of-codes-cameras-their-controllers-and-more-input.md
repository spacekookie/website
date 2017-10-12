Title: 05. (LibGDX) Game of Codes: Cameras, their controllers and more Input
Date: 2013-12-20 02:21
Category: Game of Codes
Tags: Guides
Slug: 05-libgdx-game-of-codes-cameras-their-controllers-and-more-input
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we learned how to use Texture Atli and
sort our assets in a way that we don't get lost in them (and also import
them all in one place, our ResourcePacker). In this issue I promised you
something about cameras and I realised that this would be the perfect
opportunity to add some more action into our game. Let's begin!

The first thing we'll want to do is create a new class in our utility
package and call it something along the lines of CameraController,
CameraInputAdapter or CameraManager. Let the class extend the
InputAdapter and already create a few variables in it. An
OrthgraphicCamera called camera and 4 Vector3 objects called current,
mouse, last and delta. We'll need these to handle the scrolling logic
for our camera.

``` {.lang:java .decode:true}
public class CameraController extends InputAdapter {
  final OrthographicCamera camera;

  private final Vector3 current = new Vector3();
  private final Vector3 mouse = new Vector3();
  private final Vector3 delta = new Vector3();
  private final Vector3 last = new Vector3(-1, -1, -1);

}
```

Be sure to give last three "-1" values and the rest you can leave empty.
That's that, now create a constructor that takes the camera and stores
it into the camera variable in our controller.

Add the highlighted code into your games create() method to set up the
CameraController. **Notice how we replaced the InputAdapter as the Input
Processor and are now using the camController!!!**

``` {.lang:java .mark:3-4 .decode:true}
    camera = new OrthographicCamera();
    camera.setToOrtho(false, w, h);
    camController = new CameraController(camera);
    Gdx.input.setInputProcessor(camController);
    camera.update();
```

And that's where we'll take a step back and look at cameras for a
moment. I already mentioned "unprojecting" in a previous tutorial and
the term "Orthographic" has been flying around quite a lot recently. So
I actually wanted to take the time and explain a few things about
cameras because they'll make the whole ordeal less complicated (and also
give you the ability to come up with your own camera code).

![zyGF1](http://www.spacekookie.de/wp-content/uploads/2013/12/zyGF1.gif)

These are the two camera types, left perspective and right orthographic.
The main difference is that the perspective camera actively uses the
third dimension to create the effect of depth while orthographic cameras
will project everything onto the screen in a straight line. The third
dimension can be used to move things behind one another but there is no
effect of depth. Two objects could be apart by 500 pixels in the z-axis
and still have the same size on-screen.

![unprojectcameras](http://www.spacekookie.de/wp-content/uploads/2013/12/unprojectcameras.png)

Camera projection is a bit tricky but it boils down to using two
different coordinate sets. When you draw something on the screen every
point in your window has a pixel coordinate from an origin (either top
left or top right corner). But when you're using a camera that camera
can scroll around, it can zoom and move. Therefor every point in the
camera space has a different coordinate than the pixel coordinates on
the screen. In the example of the picture above it is visible that the
point on the screen (in pink) has a different coordinate on the map than
on the screen (because the map and screen origin aren't the same).

When registering clicks, drags or any kind of interaction all those
coordinates will be in the screen-coordinate system. But we don't want
the game to just set place in one screen width/ height so we move around
and by calling "unproject" with a Vector3 we can translate the screen
coordinates (with help of the camera) into world coordinates. Those two
can be the same if the origins are the same but they can also be vastly
different when on the other side of the game world.

Don't forget to remember this! Your camera space will always move around
while your pixel space will stay the same.

If you have questions about that, post them in the comments below. But I
hope this should be clear now. Now we should get back to the matter at
hand.

Controlling the Camera {style="text-align: justify;"}
----------------------

We're gonna have a look at zooming the camera first and limiting zoom
range so that the player can't zoom out to see the entire world or zoom
too far in that one pixel of the ship takes up the entire screen. But
first up, I want you to do one things: go into the games Main method
(the one that starts the Desktop client) and change three things.

``` {.lang:java .decode:true}
 cfg.useGL20 = true;
    cfg.width = 1280;
    cfg.height = 720;
```

Using OpenGL2 isn't important for now but we should do it anyways. It
will make things look smoother and work faster but not be compatible
with older (Android) devices. The second thing is just upgrading the
game to 720p resolution which in 2013 is probably better. Aaaaaand JUST
like that we have the same resolution as the Xbox One :')

``` {.lang:java .decode:true}
  @Override
  public boolean mouseMoved(int screenX, int screenY) {
    mouse.set(screenX, screenY, 0);
    return false;
  }

  @Override
  public boolean scrolled(int amount) {
    float newZoom = camera.zoom * (1 + (amount < 0 ? 0.1f : -0.1f));
    changeZoom(newZoom, mouse.x, mouse.y);
    return true;
  }
```

Add these two methods to our camera controller. The mouseMoved method
should be fairly trivial, we only log the current mouse location into
our lovely vector, with the z-axis set to "0" and return with false.

The second method is the scrolled(. . .) method that gets passed in an
amount (-1 or 1, depending on the mouse-wheel direction) and executes
some code to calculate the zoom.

First up we create a new float called newZoom and take the current
camera zoom and multiply it by 1 + either 0.1 or -0.1, depending on
whether amount was 1 or -1. This is a general syntax that can be used, a
shortened if-statement:

``` {.lang:java .decode:true}
(a < b ? 1 : 2)

means:
"Is a smaller than b? If that's the case return 1, if not, return 2"
```

We could have written a whole nestation of if-statements for it but why
do that if we can just write one line.

The next line calls "changeZoom" which is a method that we have yet to
implement and gives it the newZoom value, as well as the latest
mouse-pointer-coordinates. This means that the picture will zoom towards
the mouse, like in any decent game. If you wanted it to zoom towards the
center of the screen you could use this.

``` {.lang:java .decode:true}
changeZoom(newZoom, Gdx.graphics.getWidth() / 2, Gdx.graphics.getHeight() / 2);
```

Now let's have a look at what we need to do in the changeZoom(. . .)
method we have yet to write.

-   We need to log the current screen position to translate the screen
    by amount x and y to fit the new zoom position
-   We need to check if zoom should be applied (aka if inside the zoom
    boundaries)
-   Apply the zoom, update the camera and check the new camera position
-   Then calculate how to move the camera to its new position

So there will be a tiny tiny delay between zooming and panning to a side
but in practise it's not noticeable. So let's get to work.

First you should add another vector to the list, this time just a
Vector2, that will hold our zoom boundaries for us. I just went with two
hardcoded values that I found worked out quite well in practise. But
you're free to experiment around.

``` {.lang:java .decode:true}
  /* x = min, y = max */
  Vector2 zoomBounds = new Vector2(0.45f, 0.75f);
```

Next up, we can go create our method and tackle the first two bulletins
on our list.

``` {.lang:java .decode:true}
  public void changeZoom(float zoom, float x, float y) {

    Vector3 before = new Vector3(x, y, 0);
    camera.unproject(before);

    if (zoom <= zoomBounds.x || zoom >= zoomBounds.y) {
      return;
    }
  }
```

Returning from a void method with no value will just jump out of the
method. It's an easier why than to nest the entire algorithm into an if
or the following else-statement. The statement just checks if the zoom
value that we pass into the method.

Now that we've shown that the zoom is valid we can apply it and update
the camera. Then we can store the new location vector, unproject it and
afterwards translate the camera from the old position to the new by
subtracting the two vectors and thus getting the connection vector.

``` {.lang:java .decode:true}
 camera.zoom = zoom;
    camera.update();
    Vector3 after = new Vector3(x, y, 0);
    camera.unproject(after);

    camera.translate(before.x - after.x, before.y - after.y, 0);
```

Go ahead and try that for a bit. You'll see that the camera won't zoom
past our barriers which means that the player can be focused on their
ship and the environment at times and still zoom out a bit and get some
sort of overview. It was important to having implemented this first
because now we're gonna tackle the much harder subject of scrolling
around (by clicking and dragging) and also setting boundaries around the
map that limit the player from scrolling past our beautiful star map and
into the nothingness that is the white background colour :O

Start by adding two more methods: touchDragged, touchUp and update().

``` {.lang:java .decode:true}
  @Override
  public boolean touchDragged(int x, int y, int pointer) {
    camera.unproject(current.set(x, y, 0));
    return false;
  }

  @Override
  public boolean touchUp(int x, int y, int pointer, int button) {
    return false;
  }

  public void update() {

  }
```

And start by setting the current vector to the x and y values passed
into the method as they'll be updating the current vector. Then
unproject that bad girl to get the world coordinates of the actions.

Next we want to check if we've already dragged. And that's why I wanted
you to give the last vector the value (-1,-1,-1) because this now allows
us to use this value as a flag. See, because we're only using 0 in the
z-dimention we can assume that if it's set to -1 it's one of our flags.
So go ahead and check if last is (-1,-1,-1) and if it is NOT! set the
delta vector to the last coordinates and unproject that as well.

``` {.lang:java .decode:true}
if (!(last.x == -1 && last.y == -1 && last.z == -1)) {
      camera.unproject(delta.set(last.x, last.y, 0));
    }
```

Afterwards add two more things: we want delta to be the difference
between the last point and our current point, so we need to subtract the
two. And lastly we want to apply that manipulated delta vector to the
camera so that it actually moves from our last position to the current
position (on the delta vector). (Full if-statement to prevent confusion,
I will add the full code again afterwards. This is really non-trivial).

``` {.lang:java .decode:true}
 if (!(last.x == -1 && last.y == -1 && last.z == -1)) {
      camera.unproject(delta.set(last.x, last.y, 0));
      delta.sub(current);
      camera.position.add(delta.x, delta.y, 0);
    }
```

After we're done with this we want the last vector to be set to our
current coordinates because in the next call those need to be updated
(as current will have been updated to our next position). Then we return
with false because we want the event to trickle through every listener
we have. What is that? I know...I'm getting ahead of myself, I will
explain that in a bit!

Now we can scroll around the camera but there is one thing we need to do
and that is set last to (-1,-1,-1) again so that it can't activate the
if-statement on the first call of touchDragged and gets assigned with
the current coordinates.

``` {.lang:java .decode:true}
  @Override
  public boolean touchUp(int x, int y, int pointer, int button) {
    last.set(-1, -1, -1);
    return false;
  }
```

And here the full touchDragged(. . .) again as reference.

``` {.lang:java .decode:true}
  @Override
  public boolean touchDragged(int x, int y, int pointer) {
    camera.unproject(current.set(x, y, 0));

    if (!(last.x == -1 && last.y == -1 && last.z == -1)) {
      camera.unproject(delta.set(last.x, last.y, 0));
      delta.sub(current);
      camera.position.add(delta.x, delta.y, 0);
    }
    last.set(x, y, 0);
    return false;
  }
```

Now...if you try this out you'll see that we can zoom and scroll around
on our lovely landscape. But the problem is that there are no bounds to
keep us inside the landscape and the player can easily scroll too far
and see the white background. Yikes.

To fix this we need to go back to our main game class for a second and
change the render() method a tiny bit.

``` {.lang:java .mark:6-7 .decode:true}
  @Override
  public void render() {
    Gdx.gl.glClearColor(1, 1, 1, 1);
    Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

    handler.update();
    camController.update();

    batch.setProjectionMatrix(camera.combined);
    batch.begin();
    space.draw(batch);
    player.draw(batch);
    batch.end();
  }
```

What did I do here? I stopped updating the camera in the render method
but instead started calling that update() method we created in the
CameraController. We could of course have this code in the render method
but it's good practise to not cluster that thing up too much. Go back to
the camera controller and add that camera.update() call to the update()
method again so that we don't break everything.

And that's the point where I will once again bore you with mathematical
theorems. (Actually it's not too bad). The subject at hand is clamping.
For everybody familiar with this, go ahead and skip this paragraph. For
everybody that is not, let me quote Wikipedia for you:

*"In computer graphics, clamping is the process of limiting a position
to an area. Unlike wrapping, clamping merely moves the point to the
nearest available value."*

So essentially we have a method called clamp(value, min, max); and the
method tries to keep our value between the minimum and the maximum. In
LibGDX this is done by calling the MathUtils class and asking for (the
drunken) clamp.

We will be clamping the cameras x and y position manually but we have
another problem. See...we have our origin in the bottom left, but the
camera position is measured at its center. And because we're zooming in
and out the center doesn't always have the same position. So we need to
adjust the boundaries for the camera dynamically. And we can do that by
taking the size of the screen, multiplying it with the camera zoom and
then dividing it by 2 to get the center.

In code example.

``` {.lang:java .decode:true}
camera.position.x = MathUtils.clamp(camera.position.x, (Gdx.graphics.getWidth() * camera.zoom) / 2, max);
```

Now..for the maximum, we want the camera to stop on the other side of
the texture, so we need to get the size of the texture from the
ResPacker. But we also need to take the same offset we added to the
minimum, because the center is still moved to its center. So instead of
adding to "0" we now subtract from the size of the texture.

``` {.lang:java .decode:true}
ResPack.WORLD_BACKGROUND.getRegionWidth() - (Gdx.graphics.getWidth() * camera.zoom) / 2
```

And that's that. Here is the full code if you wanna check that you did
it right. Of course we want to do this for both the X and the Y axis and
we of course want to take the HEIGHT for the Y axis, not the width
(looks at self in shame after not having found a bug with this).

``` {.lang:java .decode:true}
  public void update() {
    camera.position.x = MathUtils.clamp(camera.position.x, (Gdx.graphics.getWidth() * camera.zoom) / 2,
        ResPack.WORLD_BACKGROUND.getRegionWidth() - (Gdx.graphics.getWidth() * camera.zoom) / 2);
    camera.position.y = MathUtils.clamp(camera.position.y, (Gdx.graphics.getHeight() * camera.zoom) / 2,
        ResPack.WORLD_BACKGROUND.getRegionHeight() - (Gdx.graphics.getHeight() * camera.zoom) / 2);
    camera.update();
  }
```

is now our update method and it's glorious, isn't it? Try it out and
marvel at our limitless glory and genius. And then realise that you can
no longer move the ship. Well....remember? We kinda replaced the
InputAdapter as our InputProcessor. But don't worry, there is a way
around it! Remember when I spoiled you a few lines ago with trickle down
something? Well..turns out that LibGDX offers you a way to add multiple
InputProcessors with something called a *Multiplexer*.

![Input
Multiplexer](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2014-01-10-at-23.57.26.png)

Go into our main game class and add a new Object

``` {.lang:java .decode:true}
private InputMultiplexer plex;
```

And then in the create() method.

``` {.lang:java .mark:6,12-14 .decode:true}
  @Override
  public void create() {

    . . .

    plex = new InputMultiplexer();

    handler = new InputHandler(player);
    camController = new CameraController(camera);

    /* Input Controllers */
    plex.addProcessor(camController);
    plex.addProcessor(handler);
    Gdx.input.setInputProcessor(plex);
  }
```

Adding the CameraController first will give it a higher priority in the
MultiPlexer. Meaning that it will first trigger the events in the
CameraController and then trickle down to the other controllers. That's
why I didn't want to return true in our drag-methods because that would
stop the event and not pass it onto the next InputProcessor.

And that's that, compile this and you'll see that you can fly the ship
around and drag the camera over the map at the same time. And this is
where I'll end this tutorial, I think I've loaded your brain with enough
new stuff right now.

Next time I want to take a look at actual gameplay. Letting the camera
pan after the ship, letting the ship also have boundaries (same as the
camera) and placing those other textures I made around in the world, as
well as some well needed refactoring if we're gonna expand our feature
list. But until next time, keep coding!
