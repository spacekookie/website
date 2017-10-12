Title: 02. (LibGDX) Game of Codes: Input & Movement
Category: Game of Codes
Tags: LibGDX, Tutorial, Game Dev
Slug: 02-input-and-movement
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX framework. In the last edition we learned how to set up LibGDX with a new Java project and draw simple pictures onto the screen. We used textures to import that image and then drew it via a SpriteBatch.

Today we will look at basic input handling and how to make things move on screen. And though we won't be able to cover everything in this article we will explore the basic input stack that LibGDX has to offer and how to make things in your game move.

Exciting! :) 

A little note: all the code that gets shown off here is available in a [Github repository](https://github.com/spacekookie/starchaser) for you to tinker with. After each tutorial I tag the commit so that it's obvious what got changed when!

You can also use that repository to report issues or give feedback if you'd like. Otherwise, my email is always available!

### Registering input

Before we talk about inputs, we need to think about what it even means to register an input. When the user presses a button in our game, we want that button press to notify us so we can affect some behaviour. To understand what is going on here, we should consult the following graphic.

![Life of a Frame](/images/gameofcodes/series02/01_framelife.png)

You can see that LibGDX (obviously) considers the main run loop of our game...a loop :) In this series we only really care about the purple boxes. And in this article in particular, we are only considering the first purple box: "Input". What LibGDX does during this step is poll all input hardware for activity. It then writes this activity into a buffer and signals all registered input adapters to handle their input.

So with that in mind, there are two ways of checking for input. The first is essentially polling the hardware again yourself during the "Render" step, while the other hooks into the "Input" step and is called asynchronously.

Both ways of handling input are slightly unique. And we will start with the polling aproach first to demonstrate some basic functions.

First, go into the main game class and add a position variable into the class body:

```java

import com.badlogic.gdx.math.Vector2;

public class StarChaser extends ApplicationAdapter {
    //...

    Vector2 position;

    // ...
}
```

Furthermore, in the `create` block of the game, initialise the position to some value that is greater than `(0,0)` and not too big to be off window :)

```java
    position = new Vector2(250, 150);
```

If you're not too familar with Java, what this means is that we declare `position` to be a object variable which means that every function in an instance of this class can access it (Object-Oriented Programming). In the `create` function we then initialise it to have a value other than `null`.

What that means now is that we can use the position variable (which has an `x` and a `y` component) in our draw calls to tell the picture where to go. The main advantage of this is that when we change the position variable (say...via a button press), the picture gets an updated position!

```java
    public void render() {
        Gdx.gl.glClearColor(1, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);

        updateInputs();

        batch.begin();
        batch.draw(background, 0, 0);
        batch.draw(img, position.x, position.y);
        batch.end();
    }
```

So far so good...wait. Do you see that `updateInputs()` function call there? That wasn't there last time. In fact, it doesn't yet exist. But it should soon. Why don't you go and create a new function in the class somewhere with the signature `void updateInputs() { ... }`. We will fill it's body with some stuff soon.

So fundamentally, we want to poll inputs and then when we have determined that an input is pressed we want to enact some functionality. The simplest form of polling buttons is with the `Gdx.input.isKeyPressed(key)` function where `key` is an integer variable that corresponds to a key-code. Don't worry, there are bindings that make it easier and you don't have to manually check for numbers ;)

> **Tip**

> Other input polling functions include `isButtonPressed(button)` for mouse buttons as well as `getX()`, `getY()` which give you the cursor position in your game window!


So why don't you add the following lines of code to your `updateInputs` function and see where it gets us.

```java
        if (Gdx.input.isKeyPressed(Keys.W)) {
            position.y++;
        } else if (Gdx.input.isKeyPressed(Keys.S)) {
            position.y--;
        } else if (Gdx.input.isKeyPressed(Keys.A)) {
            position.x--;
        } else if (Gdx.input.isKeyPressed(Keys.D)) {
            position.x++;
        }
```

You can run this now and see what happens. When we press the keys in question the image on screen will move all over the place. Cool! But...it's not particularly pretty, is it? 

For one, we can only move in one direction simultaniously. But even if we split the X-Y axis into two different if-blocks, there is still the problem that `W` will always have precedence over `S` and `A` will have precedence over `D`. Which means that if we press all keys, we will *always* move top-left. And that's not particularly great :(

> **Tip**

> Also consider the following: when you move in one direction you apply 1 to the axis you're moving along. But if you move in two directions, you apply 1 in both x and y direction. Which means that (via trigonometry) you actually move **~1.41** in total. This means your game isn't consistent about rules.

> It's clear that more logic is required to move!

So how do we fix this? We can of course add more logic to our `updateInputs()` function but it will result in a lot of dirty hacks. And while game development is often about making dirty hacks that work, starting a project off some will quickly make your code-base unmaintainable.


### Using Input Adapters

The second method of getting input from the user I mentioned earlier is via an input adapter. It can be considered faster because we only do input polling once and it allows us to use input signals between different game components (gameplay, game HUD, etc.)

So how do we use this awesome functionality? Well, it's simple. We need an InputAdapter. So first, create a new class via Eclipse. If you don't know how, consult the *suuuuper* helpful screenshot below :')

![Life of a Frame](/images/gameofcodes/series02/02_createclass.png)

Give it a useful name like `InputHandle` or `ShipInputHandle` or something. You can be quite specific in the naming because you very often have multiple input adapters for different aspects and parts of your game. So being specific in the naming just helps you out in the long run.

Once you've done that you should be greeted with a very boring and empty class in your editor. So we need to add some basic code to get going. I took the liberty of doing that and will now show off what I did (and you'll finally get to see what name I chose...).

```java

import com.badlogic.gdx.InputAdapter;
import com.badlogic.gdx.math.Vector2;

public class ShipInputHandle extends InputAdapter {
    Vector2 shipPosition;

    public ShipInputHandle(Vector2 shipPosition) {
        this.shipPosition = shipPosition;
    }
}

```

So, as you can see we have a class that extends `InputAdapter` as a subclass. With that comes free functionality we don't have to implement ourselves. Additionally I create a constructor that takes a vector and stores it as an instance variable (like before in the game class). Note that we're not copying the value here but rather storing a reference to the "original" variable in the game.

> **Tip**

> If you're coming from a language like C or C++ this can be quite confusing. What is a copy, what is a reference? In general: java always passes by reference (pointer) unless it is a primitive value. What is a primitive value? `int`, `float`, `double`, `boolean`, `byte`, `long` and all other lower-case types that become purple in the IDE (keywords).

Next up, let's handle some inputs! The principle is similar to the polling: we check what input we are handling (because we only have generic functions - this will become obvious in a second), then invoke some behaviour. But as we have already seen before, we need to store some state. And that's why this is perfect: we have a new class where we can store the input state to check against. But at the same time, it's contained and doesn't clutter our main game class.

Now...to solve the problem of moving in multiple directions at the same time, without letting one direction take precidence over another we can use a tri-state variable. In Java this can easily be done with an enum. Create a enum titled `TS` (or TriState if you feel verbose) in our `ShipInputHandle` class and create two values `x` and `y` that use it. The initial value should be `NEUTRAL`

```java
    enum TS { POS, NEG, NEUT };

    TS x = TS.NEUT, y = TS.NEUT;
```

In the `keyDown(int keycode)` and `keyUp(int keycode)` functions we can then use a switch statement to flick the `x` and `y` variables in their favour. We *can* also perform a simple check if the `x`, `y` variables are already set to avoid another direction overwriting our current movement. But then again, maybe you consider this preferred behaviour. I chose to perform the check in the following code!

```java
public boolean keyDown(int keycode) {

    switch (keycode) {
    case Keys.W:
        if (y == TS.NEUT)
            y = TS.POS;
        break;
    case Keys.S:
        if (y == TS.NEUT)
            y = TS.NEG;
        break;
    case Keys.A:
        if (x == TS.NEUT)
            x = TS.NEG;
        break;
    case Keys.D:
        if (x == TS.NEUT)
            x = TS.POS;
        break;
    }

    return true;
}
```

Notice that `return true` at the end of that function? That's what you could call "Input Cascade". It is a concept that we will use extensively in later articles of this series. In short, it is the concept of letting an input signal cascade through different input adapters until it is ended. Returning true in this function signals the core input controller that we are ending the signal: it will not cascade to lower ranking controllers. This means that if you replace it with a `return false`, controllers down the stack will be able to pick up on the signal and use it.

But again, this will become important in later tutorials. For now, let's just end the signal and get it over with. Next up, we can implement the `keyUp` function very simply by checking what axis our key-presses affect and then resetting that direction back to `NEUT` if it is applicable. Not a perfect solution but something that will definately work is implemented below.

```java
public boolean keyUp(int keycode) {
    switch (keycode) {
    case Keys.W:
        if (y == TS.POS)
            y = TS.NEUT;
        break;

    case Keys.S:
        if (y == TS.NEG)
            y = TS.NEUT;
        break;

    case Keys.A:
        if (x == TS.NEG)
            x = TS.NEUT;
        break;

    case Keys.D:
        if (x == TS.POS)
            x = TS.NEUT;
        break;
    }

    return true;
}
```

Now we're almost done. One thing is missing however! We keep a state depending on the inputs of our user. But we don't apply anything to the vector we stored based on that state. This is where we will need to build something slightly custom because the InputAdapter doesn't force you into any workflow.

I recommend you create a new function `void update() { ... }` in the input class and make it public. We consider this function to be called every frame and apply values to the x and y components of the position vector, depending on the state of our inputs.

The following code very quickly checks if we need to apply movement at all (is not NEUT) and then does a conditional application of 1 or -1 to each component.

```java
public void update() {
    if(x != TS.NEUT) shipPosition.x += (x == TS.POS) ? 1 : -1;
    if(y != TS.NEUT) shipPosition.y += (y == TS.POS) ? 1 : -1;
}
```

Now we're done modifying the ShipInputHandle...for now :) Go back to the main game class. There are two more things to do before we can enjoy our new input handles. First, remove the old `handleInputs()` function. We don't need or want it anymore. Also make sure to remove it's function call from the `render()` function.

Secondly, create a ShipInputHandle object and initialise it with our vector. Take the following code segment as reference.

The last line in the `create()` function is key and not to be forgotten! It registers our custom input handler with the LibGDX input system and makes sure that our functions are *actually* being called :)

```java

public class StarChaser extends ApplicationAdapter {
    
    // ...

    ShipInputHandle input;

    @Override
    public void create() {
        // ...

        position = new Vector2(250, 150);
        input = new ShipInputHandle(position);

        Gdx.input.setInputProcessor(input);
    }

    @Override
    public void render() {
        
        // ...

        input.update();

        // ...
    }

    // ...
}
```

And that's it! Run that code and you'll be able to move the image around in a much nicer fashion! Again, this is far from perfect. And you will notice that switching quickly from going-left to going-right can make the whole thing just stop on "Neutral". You can remove the additional check which I added. Realistically, you need a lot more state to mirror what the user is putting into your system if you want real-feedback and logical behaviour from your units. But this will do for now!

And more importantly...it should have given you a glimpse at how to use the InputAdapters.

<hr />

And that's it for this article! Originally I wanted to talk a little bit about rotation. But I realised that I would have had to make a lot of assumptions about systems and not be able to go into too much depth without making the article *waaaayy* too long.

So that'll be handled in the [next issue](https://media.giphy.com/media/z85AlA6CBKxEI/giphy.gif).

Have a good day/ night,

Kate
