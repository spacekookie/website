Title: 01. (LibGDX) Game of Codes:  The Setup & Basics
Category: Game of Codes
Tags: LibGDX, Tutorial, Game Dev
Slug: 01-libgdx-game-of-codes-the-setup-basics
Status: published

**Hey everybody and welcome to a new/ old series on this blog about LibGDX.**

LibGDX is a Java game development framework based on LWJGL and OpenGL which makes it relatively easy to make a game from scratch without requiring a big engine. It supports Desktop, Android, iOS and HTML as export targets which means that your game is automatically cross platform.

Getting to know the framework can be challenging in the beginning, which is why I wanted to make a little series about it. Before I moved my blog to a static site generator I had a rather popular series about LibGDX called "Game of Codes". Unfortunately large parts of the guides are now outdated and no longer relevant. And the Wordpress export destroyed most of the formatting.

Which is why I decided to rewrite them. Here it is: the Game of Codes! *plays theme song*

NOTE: This tutorial requires a basic level of programming/ scripting skills. General Java knowledge is required or at the very least knowledge of how coding works. If you don't know that yet then I
recommend [Bucky Roberts Java Programming series on Youtube](https://www.youtube.com/watch?v=Hl-zzrqQoSE&list=PLYJQBQw9Wdiid6eT1_DqBP3lnbJCzo3s8).
It's very good!


### Setting up LibGDX

Now that we've got that out-of-the-way let's set up our workspace to make some neat games. I am writing and testing these tutorials on Linux. So if there are some platform specific issues you encounter, please give me feedback at [kookie@spacekookie.de](mailto:kookie@spacekookie.de).

1. First of all you'll need to have Java and an IDE (Integrated Development Environment) installed on your computer. In this series I will be assuming that you're using **Eclipse**. For pointers on how to install that, please use Google!
     - LibGDX uses Gradle as a build system. The latest version of eclipse has it integrated but older versions might require a plugin!
3. Go to [libgdx.badlogicgames.com](http://libgdx.badlogicgames.com/) and download the libgdx setup app. It will help you configure your project with Gradle so you can either develop on it in a text editor of your choice or import it into an IDE.

<img class="dual" src="/images/gameofcodes/series01/02_setup_ui.png" align="left">

<img class="dual" src="/images/gameofcodes/series01/01_setup_ui.png" align="right">

Let's step through the setup UI on your left real quick. We have some base settings. You can fill out the name of the game, the name of the main class as well as the package. If you're new to Java, the convention is that every application has a unique package root. And it's usually the reverse of a web-address. So for me it's `de.spacekookie` and then the project name. In homage to the original tutorial series I will call it `de.spacekookie.starchaser`.

Also important to choose are the directory where to setup the project as well as your Android SDK location (if you want to build on Android). I will be ignoring Android for now and focus on the Desktop.

<br/><br/><br/>

<!-- Introduction to the module we need -->

Make sure that you tick the following extentions (and extentions from the "third party" visible below the main window):

 - Ashley (Entity management library)
 - Box2D (2D physics)
 - Box2DLights (2D realistic lighting)
 - VisUI (Good looking skin for UI elements)

Also make sure that if you want to use an IDE (such as Eclipse or IntelliJ) to select the project export from under "Advanced". When you're done with the configuration, hit that lovely "Generate" button and let's get going with development :)

I will skip the importing step because that will be different for different IDE's. All I will say is that in Eclipse you should avoid putting your workspace *inside* your project directory as it will cause issues for you in the future (or during import).

> **Tip**

> While there are many ways to work on LibGDX, in this series I will assume that the project was added to Eclipse via Gradle while the building is done via a normal "Java Application" launch target in Eclipse. This is (in my opinion) the best of both worlds with a quick and easy build but the dependency management of Gradle built int the IDE.

### Working with LibGDX

So assuming that you were able to follow until here, you should now have a Java development IDE in front of you

<!-- Add a picture of Eclipse here? -->

> **Tip**

> LibGDX is very closely entangled with Android. For example, if you create a project to have an Android target, all of the game assets will be stored in the "Android" subfolder because of who the system handles file imports. This means that the Desktop/ iOS and HTML versions only use symlinks to the Android assets directory.

> If you don't have an Android project (only Desktop for example) assets are simply stored in your core project with all your game code!

Now that everything is ready to go, let's investigate a little into what code was already generated for us and what we can do with it. Feel free to just hit that "build" button and get started but we're taking a more scientific approach :)

<img class="dual" src="/images/gameofcodes/series01/04_eclipse.png" align="left">

As you should already have noted there are several projects that were created for you. One project without a suffix and multiples with suffixes. The one project without a suffix is called the "meta" project (it contains relatively uninteresting things), while the other projects have to be divided into "core" and "targets". The idea is simple: you write all your logic, rendering and gameplay into the "core" while platform dependant code is used in the "targets". If this is complicated to understand, don't worry. It'll become clearer when using it.

So as explained above, we will write most of our code in the highlighted "core" module. It is where you should in fact write all of your game code that isn't platform-specific to launch the game (for example getting the screen size or setting a custom icon).

Please go ahead and open up the two files marked by arrows. They are the only code files that were generated for me. The lower one labelled `DesktopLauncher.java` contains the main function which will actually launch our game. The code should be very straight forward and we will look at the configuration settings later.

<!-- Explain the basic structure of the project & function lifetimes -->

The second file, labelled `StarChaser.java` in my case (and whatever you named your main class in the setup tool) contains much more interesting goodies: game code!

Inspecting the code from the StarChaser class you can see a few functions in there that are responsible for describing the lifetime of our game object. These function are `create`, `render` and `dispose`. The create, play and, when we're done, destroy our game object. Everything else we do lives in between those functions.

In fact, there are a few extra steps in between that are hidden from you by default. Check out the following list:

```java

/** Called when the game is created **/
public void create();

/** Called after create and every time the window is resized (if that is allowed) **/
public void resize(int width, int heights);

/** Starts calling after create() and resize() and will be 
 *  recalled every frame. This is your game loop! **/
public void render();

/** Called when the game is closed on Android **/
public void pause();

/** Called when the game is re-opened on Android **/
public void resume();

/** Called when the game is closed. **/
public void dispose();

```

This layout allows for very structured game code that walks through stages. You can of course allocate new objects in any of these functions to move functionality away from one class but in the end, you are always bound by the lifecycle of your game object. Note that all of these functions are provided by the `ApplicationAdapter` super-class that our main game class implements. 

> **Tip**

> If you're ever curious about something you use/ extend/ implement works under the hood, don't be afraid to right-click on the part in question and click "Open Declaration" (when using Eclipse). This will open the source file for this module and you can see what is happening behind the scenes. In fact, I highly recommend being curious throughout this entire series.

<!-- Explain the awefulness that is Eclipse run configurations -->

If you haven't already launched the game to see what it does, I would recommend you do that now. Click the small black arrow next to the green "play" symbol in the top bar (or F5 in Eclipse), select "Launch Configurations" and create a new "Java Application" config. Check out the picture below for reference on how to fill it out. And if you have issues in this step, there are plenty of tutorials that go into depth online!

![Eclipse Launch](/images/gameofcodes/series01/05_eclipse.png)


<div class="alert alert-warning">
<h1>Fixing an Eclipse error</h1>

<br />

<p>By default LibGDX uses Gradle. This means that paths are considered differently than when you're using Eclipse. For example, the above code will not by default work with Eclipse unless you tweak something. In fact, you might encounter an error like this:</p>

<pre>
Exception in thread "LWJGL Application" com.badlogic.gdx.utils.GdxRuntimeException: Couldn't load file: badlogic.jpg
    at com.badlogic.gdx.graphics.Pixmap.<init>(Pixmap.java:148)
    at com.badlogic.gdx.graphics.TextureData$Factory.loadFromFile(TextureData.java:98)
    at com.badlogic.gdx.graphics.Texture.<init>(Texture.java:100)
    at com.badlogic.gdx.graphics.Texture.<init>(Texture.java:92)
    at com.badlogic.gdx.graphics.Texture.<init>(Texture.java:88)
    at de.spacekookie.starchaser.StarChaser.create(StarChaser.java:17)
    at com.badlogic.gdx.backends.lwjgl.LwjglApplication.mainLoop(LwjglApplication.java:147)
    at com.badlogic.gdx.backends.lwjgl.LwjglApplication$1.run(LwjglApplication.java:124)
Caused by: com.badlogic.gdx.utils.GdxRuntimeException: File not found: badlogic.jpg (Internal)
    at com.badlogic.gdx.files.FileHandle.read(FileHandle.java:136)
    at com.badlogic.gdx.files.FileHandle.readBytes(FileHandle.java:222)
    at com.badlogic.gdx.graphics.Pixmap.<init>(Pixmap.java:145)
    ... 7 more
</pre>

<p>While when you build your project with <code>gradle run</code> it will work. This is because Eclipse handles import scopes differently and we need to respect that. You now have two choices:</p>

<ol>
    <li>You hard-code import paths from the filesystem root (i.e. "/home/spacekookie/.../artpack1/uss_pixel.png"</li>
    <li>You add your assets folder to the source path in Eclipse. <strong>This is what I will be doing in this series!</strong></li>
</ol>

<p>Right-click on your desktop project and navigate to "configure build path" as shown in the picture below.</p>
 
<img src="/images/gameofcodes/series01/06_eclipse.png">

<p>Select "Add Folder" in the window that should have opened and in that dialog select "assets". Close the dialog and try to run the game again. It should now work!</p>

<p>If you're having issues with this step, feel free to e-mail me at <a href="mailto:kookie@spacekookie.de">kookie@spacekookie.de</a></p>
</div>

### Understanding the Code

*waits for you to launch the game*

Cute, eh? Not exactly a game but it's a start. The example demonstrates a few basic principles as well as *super* basic 2D rendering. However, before we go, throw it all away and implement our own cool stuff we should try to understand how the current code works.


```java
//...

public class StarChaser extends ApplicationAdapter {
    SpriteBatch batch;
    Texture img;
    
    @Override
    public void create () {
        batch = new SpriteBatch();
        img = new Texture("badlogic.jpg");
    }

    @Override
    public void render () {
        Gdx.gl.glClearColor(1, 0, 0, 1);
        Gdx.gl.glClear(GL20.GL_COLOR_BUFFER_BIT);
        batch.begin();
        batch.draw(img, 0, 0);
        batch.end();
    }
    
    @Override
    public void dispose () {
        batch.dispose();
        img.dispose();
    }
}
```

Let's ignore the package definition and import statements and jump straight into the class declaration. We're creating a class, extending the `ApplicationAdapter` which is responsible for turning the class into an actual game object (as described above).

The first function that would be invoked is the Constructor. Because there is none here, we will skip it. The next function being called is `create()`. It initialises a new SpriteBatch and afterwards a texture for "badlogic.jpg".

You will be able to find the texture in the assets folder. And, if you change it, you will notice the changes in game as well. So far so good. What the hell is a SpriteBatch?

A `SpriteBatch` is an object which is used to keep context during 2D render calls. Basically, you give it a positional and transformational reference frame (in our case DEFAULT) and then tell it to draw 2D images. But I'm getting ahead of myself. Because in this function we only create a new SpriteBatch. So all is good.

Moving swiftly on to the `render()` function. This one is more interesting. The first two lines are two OpenGL calls which prepare a frame to be drawn. The first line sets up a colour while the second line tells the graphics processor to take the prepared colour and paint the entire frame with it. The colour representation is in RGBA (Red, Green, Blue, Alpha) with floating numbers between 0 and 1. So (1, 0, 0, 1) is red. *Try to change the colour and see the result!*

The last three lines in the `render` function tell the SpriteBatch we created early to start, draw our texture and afterwards stop again. This marks the end of the frame at which point the next one will begin shortly.

> **Tip**

> Try to copy the `batch.draw(...)` command and change the coordinates from (0,0) to (200, 0). You will notice how a second instance of our texture is drawn at a different location. Cool, eh?

The last function in the file is `dispose()`. It is only called when we close the game and usually only has other dispose calls in it. In our case, we make sure to properly dispose of the SpriteBatch and the Texture as both of them allocate memory on the graphics processor and we don't want to leak memory!


### Adding to the game

Phew! That was quite a lot to take in, I'm sure. And don't worry if you're a bit fuzzy on some of the details. We will go over some of these things again when we use it. Additionally there are a lot of great resources out on the internet for you to help you out.

But before we wrap up this (way too long) article, I want to do something to make the game feel more like...well, a game. So go ahead and open the image processor of your choice (I will be using GIMP) and create a 128x128 pixel texture that one might consider a spaceship.

<!-- ADD PICTURE OF USS PIXEL HERE -->

You don't have to neccessarily make it 128x128 (I will) but the dimentions of the picture need to be a power of two (so 2, 4, 8,
16, 32, 64, 128, 256, 512, 1024, 2048, 4096, ...). This has to do with how computers load textures (details later).

What is that you say? You're too lazy? You don't have an image processing application? You managed to delete Paint from your computer? Kudos. Fine, you can use my graphics (contains the USS Pixel, a laser burst and a background image from the web). 

**Download [my artpack here](/downloads/gameofcodes/artpack1.zip).**

I would suggest you create a new directory inside your games "assets" folder so that we don't get confused about what's what. So this is how your core/assets/ folder should look like now:

<pre>
❤ (idenna) ~/P/p/c/starchaser/core> tree assets/                                                      
assets/
├── artpack1
│   ├── background.png
│   ├── pixel_blast.png
│   └── uss_pixel.png
└── badlogic.jpg

1 directory, 4 files
</pre>

First, why don't you go and change the line

```java
    img = new Texture("badlogic.jpg");9
```

to 

```java
img = new Texture("artpack1/uss_pixel.png");
```

and marvel at the amazingness that is my art skills :)

When launching the game now you will notice that the face texture has been replaced with a spaceship. However, this doesn't feel very space-y or even game-y yet. So let's not stop here! Reserve a new texture variable in your class and create it with a different resource file during the create function. Your source code should resemble something like the following

```java
Texture img, background;

@Override
public void create() {
    batch = new SpriteBatch();
    img = new Texture("artpack1/uss_pixel.png");
    background = new Texture("artpack1/background.png");
}
```

Then in the render function, before drawing the ship, draw the background texture first! This will make sure that the background is always behind the ship and not vice versa.

```java
    batch.begin();
    batch.draw(background, 0, 0);
    batch.draw(img, 0, 0);
    batch.end();
```

Run the game and feel your jaw drop. It should look a lot nicer now. There is still no game logic or advanced rendering but we're getting there. Try to flip the draw calls around and see what happens to the ship.

Also, you might have played around with the draw calls earlier and realised that `batch.draw(...)` in it's simplest form takes a texture and a coordinate. We will use more advanced draw calls later as this (for example) can't consider rotation.

![StarChaser Mk1](/images/gameofcodes/series01/07_gamechange.png)

<hr/>

Wow! That ended up being longer than I expected :) 

In the next tutorial we will look at how to bring movement into the game. This consists of actually updating certain parts of the game as well as handling user input. See you then!

Kate

[[Next post about Input & Movement](/game-of-codes/02-input-and-movement/)]