Title: 01. (LibGDX) Game of Codes:  The Setup & Basics
Category: Game of Codes
Tags: Guides
Slug: 01-libgdx-game-of-codes-the-setup-basics
Status: published

Hey everybody and welcome to a new/ old series on this blog about LibGDX.

LibGDX is a Java game development framework based on LWJGL and OpenGL which makes it relatively easy to make a game from scratch without requiring a big engine. It supports Desktop, Android, iOS and HTML as export targets which means that your game is automatically cross platform.

Getting to know the framework can be challenging in the beginning, which is why I wanted to make a little series about it. Before I moved my blog to a static site generator I had a rather popular series about LibGDX called "Game of Codes". Unfortunately large parts of the guides are now outdated and no longer relevant. And the Wordpress export destroyed most of the formatting.

Which is why I decided to rewrite them. Here it is: the Game of Codes!

NOTE: This tutorial requires a basic level of programming/ scripting skills. General Java knowledge is required or at the very least knowledge of how coding works. If you don't know that yet then I
recommend [Bucky Roberts Java Programming series on Youtube](https://www.youtube.com/watch?v=Hl-zzrqQoSE&list=PLYJQBQw9Wdiid6eT1_DqBP3lnbJCzo3s8).
It's very good!


### Setting up LibGDX


Now that we've got that out-of-the-way let's set up our workspace to
make some neat games.

1. First of all you'll need to have Java and an IDE installed on your computer. I recommend Eclipse. For pointers on how to install those please use Google.
2. Go to [http://libgdx.badlogicgames.com/](http://libgdx.badlogicgames.com/) Downloads and download the framework. You can either go for a nightly build (that will contain more awesome features but probably bugs) or the stable version. Current stable at the time of writing this is 0.9.9 and the version that I will be using (and am using for all my projects).
3. Save and extract the libgdx-0.9.9.zip file somewhere on your computer and open up the folder. You'll see a multitude of things. Now…we could set up an Eclipse project, import all the right files and  write some dummy code but there is an easier way to do this and it's called the Setup-UI. The following two screenshots will explain the basics. This should be trivial but I'll still go over it. Feel free to skip to the next part below.

![](http://www.spacekookie.de/wp-content/uploads/2013/12/libgx_install_1.png)

The following steps will be conducted in the .Jar setup UI. On the upcoming window click on CREATE and then fill out the information on the next screen. Everything you need to consider is being marked as red in the next screenshot.

![libgdx\_install\_2](http://www.spacekookie.de/wp-content/uploads/2013/12/libgdx_install_2.png)

Make sure you already have the directory created that you want to put the project in. The java UI can NOT create folders. Be sure to disable the iOS project. It won't break anything if you leave it ticked but we won't be working with it.

During the selection of the libraries you need to select the folder icon  and then point the application at the archived .zip file you downloaded in the beginning for LibGDX and press the other little arrow button for the Universal Tween Engine to download it. The Jar isn't included in the LibGDX package by default but it can come in handy later. When you're ready to continue everything should light up green. Click on OPEN THE GENERATION SCREEN to continue, click LAUNCH and watch the magic happen.


### Working with LibGDX

Now that we have an auto generated LibGDX project it's time to import it into Eclipse and look at the actual code. Go into Eclipse, File --\> Import. Select General --\> "Existing Projects into Workspace". Navigate to the path and check that all your LibGDX projects are shown as in the screenshot below. Afterwards you should be set to do some serious coding!

![LibGDX\_install\_3](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-14-at-11.00.37.png)

NOTE: LibGDX works very close with Android and when you import the
project you will see the Android project having exploded because of
various issues. Make sure that you have Android set up on your computer.
If you don't, may I refer you to an older blog post of mine: This will
explain the setting up of Android.

That's important, as LibGDX uses the Android assets folder as a link to
the main project. You can change that, if you want. But we'll leave it
as is for now! If you're having issues with this step, post your problem
in the comments below and I'll try to help you resolve it.

 

Now that everything should be ready to go, let's check what kind of code
we have here and understand the basic structure of LibGDX. As you've
already seen there are several projects that were just created: three
projects with suffixes (-android, -desktop, -html) and a core project
without a suffix. All the actual coding will be done in the core project
while the other projects are called "deployment projects". In them you
can adjust platform specific code to deploy your software. But for now,
we will only be working with the Core project and use the desktop
deployment for debugging.

NOTE: Make sure that you leave your Android project open, as LibGDX uses
the androids Assets folder for all the other projects.

 

Now, that we have this figured out, go to your core project and open up
the only class that there should currently be in there. Mine is called
TutorialsLauncher and it has a certain layout of methods in it that
LibGDX always uses.

-   **public void create()** - Called when the game is created
-   **public void resize()** - Called after create and every time the
    window is resized (if that is allowed)
-   **public void render()** - Starts calling after create() and
    resize() and will be recalled every frame. This is your game loop!
-   **public void pause()** - Called when the game is closed on Android
-   **public void resume()** - Called when the game is re-opened on
    Android
-   **public void dispose()** - Called when the game is closed.

This layout allows for very structured code to be written. An
interesting thing to note is that this layout comes from the
implementation of the **ApplicationListener** interface. So when you
create your own main game class you just implement that interface and
it'll suggest the code layout for you automatically.

Before we look at the code in more detail and see what it actually does
we should launch the application though and see what it looks like. For
that you'll need to create a Run Configuration for a Java Application
and point it at the Main class in your \*\*-Desktop project. A new
window will open and TADA! The dummy "game" :)

![LibGDX\_instllation4](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-14-at-12.29.10.png)

Now let's look at the actual code that does stuff:

``` {.width-set:false .lang:java .decode:true title="Create Method"}
   @Override
    public void create() {      
        float w = Gdx.graphics.getWidth();
        float h = Gdx.graphics.getHeight();

        camera = new OrthographicCamera(1, h/w);
        batch = new SpriteBatch();

        texture = new Texture(Gdx.files.internal("data/libgdx.png"));
        texture.setFilter(TextureFilter.Linear, TextureFilter.Linear);

        TextureRegion region = new TextureRegion(texture, 0, 0, 512, 275);

        sprite = new Sprite(region);
        sprite.setSize(0.9f, 0.9f * sprite.getHeight() / sprite.getWidth());
        sprite.setOrigin(sprite.getWidth()/2, sprite.getHeight()/2);
        sprite.setPosition(-sprite.getWidth()/2, -sprite.getHeight()/2);
    }
```

First thing the code does is log the current resolution of the game and
store them in two float variables.

Next up we create a camera, set up with the ratio of the resolution we
just stored in the variables. (We'll talk more in-depth about cameras
later)

The next block loads a texture from the data folder which is stored in
the Androids assets folder and applies a linear filter (If you want to
learn more on that click
[here](http://gaming.stackexchange.com/questions/48912/whats-the-difference-between-bilinear-trilinear-and-anisotropic-texture-filte)).
Don't worry if the rest of that class looks like alien text. I'll
explain renderings, drawings, textures etc. in more detail in a later
article. For now you just need to know: it's setting up a sprite
(texture).

Next up in the code we have dispose:

``` {.width-set:false .lang:java .decode:true}
 @Override
    public void dispose() {
        batch.dispose();
        texture.dispose();
    }
```

Objects that use anything with OpenGL need to be disposed (should. it's
good practise). It's not that important if you quit the application but
rather when changing screens (more on that later too).

Which brings us to the main method doing stuff in this "game". Render():

``` {.width-set:false .lang:java .decode:true}
 @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
        Gdx.gl.glClear(GL10.GL_COLOR_BUFFER_BIT);

        batch.setProjectionMatrix(camera.combined);
        batch.begin();
        sprite.draw(batch);
        batch.end();
    }
```

The first two calls are OpenGL specific and absolutely need to be in
there. It clears the screen completely and then draws over with a colour
(actually ClearColor only sets a colour and the glClear clears the
screen and draws the colour but more to that later too).

Then comes the tricky part.

"batch" is the SpriteBatch that was created earlier in the create();
method. It's essentially handling texture mapping to the screen and uses
the cameras viewport (aka what the camera is looking at and how many
pixels it contains) to properly map the texture to the screen. It's
begun, then a sprite is drawn and then it's ended. (That's how you draw
things low-level with OpenGL). And that's the game loop.

Depending on how the window is scaled this means that the texture will
always look (more or less) right because it's being adjusted to the
camera viewport (which is essentially just the entirety of the
application window.

 

I know that this was a lot to take in for now. But I'll touch these
topics in later articles (again). And if I don't then there are plenty
of great resources out there (probably better than these :) to help you
around.

However, I want to do one more thing here and that is give this Game a
more Game-y feeling. First of all you should head to the image processor
of your choice (in my case Photoshop) and sketch up something that might
look like a spaceship.

![LibGDX\_Tutorial\_PS](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-14-at-22.55.25.png)

Make sure that the size of the image is by the power of 2 (so 2, 4, 8,
16, 32, 64, 128, 256, 512, 1024, 2048, 4096, etc. because that's how
LibGDX works.

What you say? You're too lazy? You don't have an image processing
application? You managed to delete Paint from your computer? Kudos. Use
[this](http://www.spacekookie.de/downloads/Tutorials/LibGDX1/USS_Pixel.zip "USS Pixel")
then! Next up we want a picture of space. I'm not gonna make something
myself here. And neither will you (most likely). How about
[this](http://www.wallsave.com/wallpapers/1024x1024/galaxies/236804/galaxies-cool-galaxy-and-space-ipad-236804.jpg "Space")?

Save both of these on your computer and import them into your
Android-projects assets folder (copy, not link!) Next up we want to
adjust a bit of our code. If you use external resources they always need
to be as power-of-two pictures. And to overcome that there is a thing
called a TextureAtlas (SPOILERS). But I'll touch that later.

For now, we just need to change the path in one line:

``` {.width-set:false .lang:java .decode:true}
texture = new Texture(Gdx.files.internal("space.jpg"));
```

I made it easy on me and just renamed the picture into "space" and moved
it into the assets folder which in LibGDX internal files is being
referenced as root. If you compile this you'll see two white bars on the
sides. So first, we might want to change that to black to make it
more…space-y but secondly we might want to change the starting
resolution of the game. If you were observant before you know where to
change the OpenGL colour. That's right. Here:

``` {.width-set:false .lang:java .decode:true}
 @Override
    public void render() {
        Gdx.gl.glClearColor(1, 1, 1, 1);
```

It uses R-G-B composition colours referenced with floats. The fourth is
the alpha channel. So to get Black we want to set it to

``` {.width-set:false .lang:java .decode:true}
Gdx.gl.glClearColor(0, 0, 0, 1);
```

For the resolution we need to check our platform-specific launcher. In
our case we have to check the Main method in the \*\*-Desktop project
and adjust two things. First, we want the starting resolution to be
800x600 as that's what the TextureRegion cuts from the original texture.
And we want to disable the ability for the window to be resized (for
now) as it adds a whole mess to take care of.

``` {.width-set:false .lang:java .decode:true}
     cfg.resizable = false;
        cfg.width = 800;
        cfg.height = 600;
```

So essentially we need to add one line to the configuration and change
two.

However, we're not done yet. We gave the texture the new path to import.
But that's not all. We need to tell the texture region what part of the
cake to slice from the original texture. And we also need to change some
of the positioning that happens. Essentially you want your code to look
like this:

``` {.width-set:false .lang:java .mark:6,12,15 .decode:true}
    @Override
    public void create() {
        float w = Gdx.graphics.getWidth();
        float h = Gdx.graphics.getHeight();

        camera = new OrthographicCamera(w, h);
        batch = new SpriteBatch();

        texture = new Texture(Gdx.files.internal("space.jpg"));
        texture.setFilter(TextureFilter.Linear, TextureFilter.Linear);

        TextureRegion region = new TextureRegion(texture, 0, 0, 800, 600);

        sprite = new Sprite(region);
        sprite.setPosition(-sprite.getWidth() / 2, -sprite.getHeight() / 2);
    }
```

I changed the camera setup to just simply use the width and height as
it's viewport, told the texture region to cut a 800x600 part from our
1024x1024 texture and removed the size and origin manipulation. Now
compile this and BOOM.

![Screen Shot 2013-12-15 at
00.19.23](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-15-at-00.19.23.png)

Shiny! \<3 Now we need some slick advertisement and EA will sell this
for 60\$ (+ DLC of course).

Now…we have that ship. Let's just quickly add the ship in idle state in
the middle of the screen before this post gets too long. You should know
how to add the space ship texture by now:

``` {.width-set:false .lang:java .mark:4-5,21-25,32,43 .decode:true}
public class TutorialLauncher implements ApplicationListener {
    private OrthographicCamera camera;
    private SpriteBatch batch;
    private Texture texture, shipTexture;
    private Sprite sprite, ship;

    @Override
    public void create() {
        float w = Gdx.graphics.getWidth();
        float h = Gdx.graphics.getHeight();

        camera = new OrthographicCamera(w, h);
        batch = new SpriteBatch();

        texture = new Texture(Gdx.files.internal("space.jpg"));
        texture.setFilter(TextureFilter.Linear, TextureFilter.Linear);
        TextureRegion region = new TextureRegion(texture, 0, 0, 800, 600);
        sprite = new Sprite(region);
        sprite.setPosition(-sprite.getWidth() / 2, -sprite.getHeight() / 2);

        shipTexture = new Texture(Gdx.files.internal("USS_Pixel/ship_idle.png"));

        TextureRegion shipRegion = new TextureRegion(shipTexture, 0, 0, 64, 64);

        ship = new Sprite(shipRegion);
    }

    @Override
    public void dispose() {
        batch.dispose();
        texture.dispose();
        shipTexture.dispose();
    }

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

And voila :)

![LibGDX\_Tutorial\_Final](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-15-at-00.32.03.png)

But this is it for today. I will start working on the next post
immediately where we will discuss input and movement on the screen (all
very basic) as well as TextureAtli (maybe, if you're lucky)

Until then have a good day/night,

Kate

 
