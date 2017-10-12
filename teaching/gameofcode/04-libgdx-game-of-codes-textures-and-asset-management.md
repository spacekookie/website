Title: 04. (LibGDX) Game of Codes: Textures and asset management
Date: 2013-12-19 19:18
Category: Game of Codes
Tags: Guides
Slug: 04-libgdx-game-of-codes-textures-and-asset-management
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we learned how to use InputAdapters and
used the keyboard and mouse to order our little space-ship around on the
screen. In this issue I want to take a step back from our actual game
and have a look at our surroundings. Data files, assets and resource
imports. Where to put them to make the game code as practical and
readable as possible. LibGDX has a few quirks and also tools to make
asset management as easy as it can be. So without further ado, let's
begin.

Collecting all Asset imports in one class {style="text-align: justify;"}
-----------------------------------------

The first thing we'll want to do is create a new package in our project.
I named mine "Util" to symbolize that everything in there has to do with
utility classes and tools that don't have a direct effect on gameplay
but are substantially important in using the game. If you're not
familiar with naming conventions for packages here is the rundown.

``` {.lang:java .decode:true}
SUFFIX.DOMAIN.PROJECT.PACKAGE.SUB-PACKAGE

In my case:

de.spacekookie.libgdxtutorial.util
```

If you don't have website where you would publish your code just use
your name with a com or de or whatever your language code is (or you
want it to be to confuse people).

![Screen Shot 2013-12-19 at
15.18.59](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-19-at-15.18.59.png)

Be sure to select your source folder to create the package. And then in
the next dialogue type the entire package tree, not just the name of the
end package you want to name. Because Eclipse will create folders from
these sub-trees.

[![Screen Shot 2013-12-19 at
15.19.16](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-19-at-15.19.16.png)](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-19-at-15.19.16.png)And
to not confuse us in the long run r-click on that other package that so
far holds all other classes and add the subpackage-name "core" to it. It
will symbolize that it holds our darkest secrets (aka the most important
classes in our game, like the main game class or the InputAdapter).

When you're done with that go ahead and create a new class in the "util"
package named along the lines of "ResourceLoader" or "TextureLoader" or
whatever takes your fancy. I'm gonna call it "**ResPack**" short for
"ResourcePacker", because it will be filled with static variables that
we will have to call from all over the game...LOTS of times. So I want
it to be as short as it can be. Once created go and fill it up with our
texture loading and save them into "public static final" variables. We
wan them to be accessible from anywhere in the game "public static" but
we also want them to be fixed and never changed again (by accident or by
an evil hacker that uses texture hacks) aka "final".

``` {.lang:java .decode:true}
package de.spacekookie.libgdxtutorial.util;

import com.badlogic.gdx.Gdx;
import com.badlogic.gdx.graphics.Texture;
import com.badlogic.gdx.graphics.g2d.TextureRegion;

/** Class to load all assets for the game */
public class ResPack {

    public static final TextureRegion shipIdle = new TextureRegion(new Texture(
            Gdx.files.internal("USS_Pixel/ship_idle.png")), 0, 0, 64, 64);

    public static final TextureRegion shipFly1 = new TextureRegion(new Texture(
            Gdx.files.internal("USS_Pixel/ship_fly1.png")), 0, 0, 64, 64);

    public static final TextureRegion shipFly2 = new TextureRegion(new Texture(
            Gdx.files.internal("USS_Pixel/ship_fly2.png")), 0, 0, 64, 64);
}
```

Alright, that's that so far. In addition to that I've made a little
texture called "blast\_small" that we will be adding later, which is
essentially just a little laser shot. You can download it
[here](http://www.spacekookie.de/downloads/Tutorials/LibGDX1/blast_small.png)
and add it to your USS\_Pixel folder in the assets directory.

But you can already see a problem, the texture isn't in power of two
measurements and we would have to manually cut out the blast from a, say
32x32 texture. But we don't really want that, do we? We're gonna have a
lot more textures later on and if we have to cut out each one
individually we're gonna have a hard time. And that's why we have such a
handy thing called the
[TextureAtlas](http://en.wikipedia.org/wiki/Texture_atlas).

Working with TextureAtli {style="text-align: justify;"}
------------------------

A TextureAtlas is essentially a file that contains all resources in it
packed into one image and an .atlas file that keeps tabs on what
resource can be found at what exact pixel location (and it's size, etc).
To create a TextureAtlas we need a TexturePacker which isn't included in
its GUI form in the LibGDX distribution (we can learn how to use the
command-line class from within our game later). Go
[here](https://code.google.com/p/libgdx-texturepacker-gui/downloads/list)
to download the GUI and add it somewhere in your project folder, why not
inside the asset folder.

The texturepacker is a .jar that can be run as a UI application that
needs no setting up. Run it and get a look around. First we want to
create a new pack, so do that on the top-left corner of the window.
Select a project name, an input, an output directory and of course a
file-name pattern. Input is the USS\_Pixel folder in our assets folder,
the output is the assets folder itself (in my case). Leave all the other
settings as they are. Then select "Pack 'em all" and wait for a
confirmation to pop up.

![TexturePackerDemo1](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-19-at-16.39.00.png)

Go and check the output folder where you should see a .png and an .atlas
file. If you have a look at the .png you will see that all the single
textures we had in our USS\_Pixel directory have been molded into a
single file that has the power-of-two resolution so that our game won't
die on us. The .atlas file should just be a bunch of numbers and words
with parameters. We'll have a look at those in a minute. First I want
you to update Eclipse so that it sees the new files in our asset folder
and direct your attention back at the ResPack class that we started in
the beginning of this tutorial.

We'll want to create a TextureAtlas object, private, static and final
and give it the .atlas file to read. I will call mine "\_PIXEL"

*(It's my naming convention to give variables that are only used in very
very (VERY) specific context an underscore as a beginning so that they
show up first on the list of recommended variables but also to filter
them out quickly and give them somewhat of a specific look. You don't
have to do it this way, I think it's even considered bad practise. But
it's something that I like to do).*

After we have our private static and final TextureAtlas we can find
textures in it by calling "findRegion(. . .)" on it. Here is some code
as reference.

``` {.lang:java .decode:true}
 private static final TextureAtlas _PIXEL = new TextureAtlas(
            Gdx.files.internal("USS_Pixel.atlas"));

    public static final TextureRegion shipIdle = _PIXEL
            .findRegion("ship_idle");
```

As you can see we no longer have to bother around with pixel coordinates
in our textures because they've all be stored in the .atlas file by the
TexturePacker. All there is left to do now is remove the TextureRegion
calls from our Entity class and change it the fly() and idle() methods
as well.

``` {.lang:java .decode:true}
  public void loadResources() {
    if (type.equals(EntityType.PLAYER)) {

      self = new Sprite(ResPack.SHIP_IDLE);
    }
  }

  public void idle() {
    self.setRegion(ResPack.SHIP_IDLE);
  }

  public void fly() {
    int i = new Random().nextInt(2);
    if (i == 0)
      self.setRegion(ResPack.SHIP_IDLE);
    else if (i == 1)
      self.setRegion(ResPack.SHIP_FLY1);
    else if (i == 2)
      self.setRegion(ResPack.SHIP_FLY2);
  }
```

And that's that. Isn't it neat? We cleaned up our code and even made the
loading of textures easier and more efficient as well. The only downside
is that you will have to re-pack your TextureAtlas for every texture
that you add. In practise I usually have 2-3 atli that hold different
kinds of textures together to keep some orientation over the textures
involved.

For that purpose I created three more textures, the Deep\_Pixel\_Nine,
the Pixel\_Sun and Pixel\_Earth to be part of an "environment" atlas (as
well as a more low-profile space picture :p ). You can download the
whole .zip file with everything inside
[here](http://www.spacekookie.de/downloads/Tutorials/LibGDX1/world.zip)!
Go and add that to the ResPacker. You should know how ;)

After setting up your ResPacker to properly import all the
TextureRegions you should go and change the image that we're currently
using and clean up your code in a way that it won't crash and doesn't
contain calls that aren't being used anymore. With the ResPacker you
have all your resources in one place and collected in two Texture Atli.

Lastly, I went ahead and refactored the assets folder a little to be
less clustered and deleted some of the files that we didn't need any
more. Also note that I'm always keeping the raw files in case I need to
update something.

![refactored\_assets\_1](http://www.spacekookie.de/wp-content/uploads/2013/12/refactored_assets_1.png)

And that's that for our rather short issue this time (I would want to
say this week but I'm writing these so quickly right now). Next time I
want to have a look at...I'm not sure yet. Probably cameras, controlling
cameras, moving cameras around, etc. And of course some lovely camera
theory. But until then have a lovely day and keep coding!
