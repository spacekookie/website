Title: 03. (LibGDX) Game of Codes: Rotation & Advanced Movement
Category: Game of Codes
Tags: LibGDX, Tutorial, Game Dev
Slug: 03-rotation-and-advmovements
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX framework. In the öast edition we learned how to listen for user input, keep it's state for consistency and apply it to the world we are building. We did this by simply using a vector as a position for an image to align to.

Today we will have a look at some more input but more importantly: rotation! And with that, also look at some more advanced movement concepts like momentum and some advice how to implement certain movement patterns.

A little note: all the code that gets shown off here is available in a [Github repository](https://github.com/spacekookie/starchaser) for you to tinker with. After each tutorial I tag the commit so that it's obvious what got changed when!

You can also use that repository to report issues or give feedback if you'd like. Otherwise, my email is always available!


### Naïve approach

So let's just take a naïve approach here. We have a vector that is essentially the position of our "ship". And it can have a rotation. So what we do is listen for two new key presses (in my case for `Q` and `E` - left and right rotation) and then create another tri-state variable `rotation` that we can use to determine whether we should rotate left or right.

```java
    switch (keycode) {
    case Keys.W:
    // ...

    /** Handling rotation */
    case Keys.Q:
        rotation = TS.NEG;
        break;
    case Keys.E:
        rotation = TS.POS;
        break;
    }
```

The inverse applies for the `keyUp(...)` function.

```java
    switch (keycode) {
    // ...

    case Keys.Q:
        if (rotation == TS.NEG)
            rotation = TS.NEUT;
        break;

    case Keys.E:
        if (rotation == TS.POS)
            rotation = TS.NEUT;
        break;
    }
```

Our update code needs to be appended slightly. This isn't the most pretty way to do this but for now it'll be alright.

```java
public void update() {
    // ...

    if (rotation == TS.POS)
        shipPosition.rotate(1);
    else if (rotation == TS.NEG)
        shipPosition.rotate(-1);
}
```

Now. What does this actually mean. We rotate the *positional* vector for the ship. You might have an inkling of what is about to happen but if you don't start the game and look at it. Not quite what we had in mind, is it?

![Bad rotation GIF](/images/gameofcodes/series03/01_badrotation.gif)

So what's happening here? Well, our positional vector points to where the ship is. From the origin. Which is in the bottom left of the screen. At coordinates `(0, 0)`... So when we rotate the positional vector, we rotate the ship around the origin. Furthermore, we never told the `SpriteBatch` to rotate the image we're drawing. That's why the ship orientation stays exactly the same: pointed upwards.


### Using TextureRegions

So let's fix this one problem at a time. Let's actually make the ship texture rotate depending on some value (in our case, the phony vector angle). For this we need to look at how we draw things. Right now, that's a texture.

A texture is essentially a raw memory map of an image, loaded onto the GPU. That's why the texture needs to be a power of two because that's how GPU's handle textures in their memory. But what this also means is that if we have multiple textures this will cause a lot of overhead because loading textures in and out of memory from the GPU is expensive.

Also, all transformations to the texture we need to apply manually. Transformations include scaling, moving and rotation. And especially the last one can be challenging.

**Enter: TextureRegion!**

Now, a `TextureRegion` is a collection of textures, essentially a large texture with bits cut out of it. This way we can bundle all our textures together into one large one (or several large ones) while marking different parts of the texture as regions so that we can handle them in the future.

What this also means is that simple transformations can be done on the CPU which is slower but much easier than performing them on the GPU. This means the textures are still stored on the GPU but we get more control over how to transform them. Let's use this in our game!

```java

public class StarChaser extends ApplicationAdapter {

    // ...
    
    TextureRegion img;
    
    // ...

    @Override
    public void create() {
        batch = new SpriteBatch();
        img = new TextureRegion(new Texture("artpack1/uss_pixel.png"));

        // ...
    }
```

The code above creates a TextureRegion instead of a Texture. In this case, we aren't using any of the memory saving benefits of using TextureRegions but that doesn't matter. We can still take advantage of it.

Specifically, we will change the `batch.draw(...)` function to take more parameters. But first, create a second vector, call it "direction" and initialise it with `(0, 1)`.

```java

final float sizeX = img.getRegionWidth();
final float sizeY = img.getRegionHeight();

batch.draw(img,                 // The TextureRegion we draw
           position.x,          // Root X position
           position.y,          // Root Y position
           sizeX / 2,           // Rotation origin X (center point)
           sizeY / 2,           // Rotation origin X (center point)
           sizeX,               // Draw width
           sizeY,               // Draw height
           1, 1,                // Scaling factor (1 is fine)
           direction.angle());  // Region angle (around origin)

```

Additionally, we need to adjust our ShipInputHandle class because we need to make it use our direction vector. The code snippet below will outline what you need to change. Essentially: we rotate our direction vector and noramlise it after every step because rotating vectors actually changes their length.

```java
public class ShipInputHandle extends InputAdapter {
    Vector2 pos, dir;

    // ...

    public ShipInputHandle(Vector2 shipPosition, Vector2 direction) {
        this.pos = shipPosition;
        this.dir = direction;
    }

    // ...

    public void update() {
        if (rotation == TS.POS)
            dir.rotate(1);
        else if (rotation == TS.NEG)
            dir.rotate(-1);

        dir.nor();

        // ...
    }
}
```

If you launch this configuration you will notice that the ship rotates around it's centre point correctly! YAY! You will notice that you can still move your ship independant of it's rotation. You might consider this a feature because it allows you to fly one way and shoot backwards (think Battlestar Galactica Vipers!). But in our case, we want the ship to always fly in the direction that it's pointing towards.

![Proper rotation](/images/gameofcodes/series03/02_rotating.gif)

This is relatively simple. We only need to change the position update code to make this happen. In fact, we only need to consider the direction vector when applying a new position.