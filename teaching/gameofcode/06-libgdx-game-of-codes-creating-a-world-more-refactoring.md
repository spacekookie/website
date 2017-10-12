Title: 06. (LibGDX) Game of Codes: Creating a world & more refactoring
Date: 2014-01-10 22:30
Category: Game of Codes
Tags: Guides
Slug: 06-libgdx-game-of-codes-creating-a-world-more-refactoring
Status: published

Welcome back to the Game of Codes, an introduction series to the LibGDX
framework. In the last edition we learned how to write a camera input
processor (which is really just like a normal input processor) and do
some freaky matrix calculations in order to move around. In this issue I
want to go back to the roots (so to say) and work on features. Our code
is already pretty slick but I think it can be improved in order to make
room for more features. Let’s begin!

First off we should change a few things in our Entity class. Remember
that EntityType that I added despite you shaking your and saying "what
the hell is she up to again?" Well...go in there and add some more
values into the enum. And also create a public getter for the type and a
private setter. This is only a temporary solution, in the long run we
want things to be saved in a database. But it'll do for now!

``` {.lang:java .decode:true}
  public static enum EntityType {
    PLAYER, ENEMY, STATION, PLANET, STAR;
  }

  . . .

  public EntityType getType() {
    return type;
  }

  private void setType(EntityType type) {
    this.type = type;
  }
```

Right now we only have one station, one planet and one star. So if we
ever decide to create more bodies we'll have to come up with a new
system (Plot twists: I already have, I'm just not telling you ;) )

Next up we want to do something else. Go ahead and create a new package
called objects (Remember to name it with the full package-tree so that
it's a child of "libgdxtutorial" and not "src") We'll use this package
to store all our gameplay objects in here. Go ahead and drag the
"Entity" into it as well before creating a new class called "World".

This is what your project tree should look now. Well...more or less.

![LibGDX\_Tutorial\_tree](http://www.spacekookie.de/wp-content/uploads/2014/01/Screen-Shot-2014-01-10-at-22.39.30.png)

Our world class will have an overview of all entities in existence,
coordinate collision detection with the player (later maybe between
non-player entities as well) and generally just know everything
important. For that to work we need to give it all the entities there
are. So go ahead and create a new Set and a few methods to actually use
those. My code, as always, as reference below.

``` {.lang:java .decode:true}
package de.spacekookie.libgdxtutorial.objects;

import java.util.HashSet;
import java.util.Set;

import com.badlogic.gdx.Gdx;

public class World {

  private Set entities;

  public World() {
    entities = new HashSet();
  }

  public Set getEntities() {
    return entities;
  }

  public Entity getEntitityWithType(Entity.EntityType type) {
    for (Entity e : entities) {
      if(e.getType() == type)
        return e;
    }
    return null;
  }

  public void addEntity(Entity e) {
    if (!entities.contains(e))
      entities.add(e);
    else
      Gdx.app.log("World", "Entity already in Set!");
  }

  public void removeEntitity(Entity e) {
    if (entities.contains(e))
      entities.remove(e);
    else
      Gdx.app.log("World", "Error! No such entity in world!");
  }
}
```

The constructor just initializes the HashSet, we have a few getters and
setters, a way to individually add a single entity (e.g. if we're
spawning a pirate ship, maybe?) We'll be expanding on this code heavily
in the future but it's as complex as it needs to be right now. (Note how
I'm using Gdx.app.log to log two cases when adding and removing
entities. That's not required but it's a good way to keep tabs of
potential errors when playing the game or debugging something.)

Next, we should go into our main game class and start using the World
object. Make sure to actually use OUR world object, not the Box2D world
(which is great for physics and lighting and we might use it later but
not right now!)

``` {.lang:java .decode:true}
 world = new World();
    world.addEntity(new Entity(EntityType.PLAYER, new Vector2(200, 150)));
```

And we of course need to teach our InputProcessor to use the world to
handle input!

``` {.lang:java .decode:true}
 handler = new InputHandler(world);
```

And in the InputHandler we need to change the constructor and some
methods.

``` {.lang:java .decode:true title="Constructor"}
  public InputHandler(Object o) {

    if (o instanceof World && o != null)
      this.world = (World) o;

    if (o instanceof Entity && o != null) {
      this.e = (Entity) o;
      return;
    }

    for (Entity e : world.getEntities()) {
      if (e.getType() == EntityType.PLAYER) {
        this.e = e;
      }
      else {
        Gdx.app.log("InputHandler", "NO PLAYER IN WORLD!");
      }
    }
  }
```

(Be sure to rename the entity in that class to "e")

And that should be all the changes we need to make. If I missed anything
or something is unclear, just leave me a comment below and I'll get back
to you. If you compile this it should still be the same game as before,
with the difference that under the hood it has a lot more horsepower
(kilowatts) and we'll be able to do some really cool things with this in
a moment.

Here is an idea. Why don't we go ahead and plan our solar system a
little. I know, I know, you're lazy again. I get it. You just wanna read
these, absorb the knowledge via a USB3 port in your skull and eat
Cheerios all night. Still. I hope you can be bothered to check out the
picture below :)

![Each grid square is exactly 100x100
pixels](http://www.spacekookie.de/wp-content/uploads/2013/12/Screen-Shot-2013-12-20-at-13.04.57.png)

You can see the background image that is currently our game world and
our other objects scattered around the world. The grid lines in
Photoshop (Adjustable under Preferences --\> Guides, Grids &
Sliders --\> Grid) will give us a little help when trying to find places
to place these objects. But for that to happen we need to add a little
more to our Entity class.

See, right now we just check if the EntityType is the player and if it
is we draw the space ship. But what we really want to do is also take a
set of coordinates in the constructor to pass down to the rendering. In
fact, we kinda want the pixel coordinate to be saved in the object
itself rather than having to check the sprite for information. Because
that's what the object is for, to hold all the information needed and
provide a sort of "interface" to access and store the information. We
don't want to be digging around in a sub-object or OpenGL logic object
to get information.

So I added a new vector called position, created a new constructor that
now also takes a vector (left the old one to not break things) and
created a method called "updatePosition()" that takes the position
vector and gives the coordinates to the sprite.

``` {.lang:java .decode:true}
  private Vector2 position;

  public Entity(EntityType type) {
    this.type = type;
    moveVector.scl(speed);
    position = new Vector2();
  }

  public Entity(EntityType type, Vector2 position) {
    this.type = type;
    this.position = position;
    moveVector.scl(speed);
    updatePosition();
  }

  public void updatePosition() {
    self.setPosition(position.x, position.y);
  }

  . . .

  public Vector2 getPosition() {
    return position;
  }

  public void setPosition(Vector2 position) {
    this.position = position;
  }
```

Next up we want the loadResources method to be able to not just load the
ship textures but check all the EntityTypes and load textures
accordingly. For that I changed the whole thing to a Switch statement.
If you're not familiar with Switch...get familiar with
[Switch](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html).
It's awesome!

``` {.lang:java .decode:true}
  public void loadResources() {
    switch (type) {
    case PLAYER:
      self = new Sprite(ResPack.SHIP_IDLE);
      break;
    case PLANET:
      self = new Sprite(ResPack.WORLD_EARTH);
      self.setScale(2f);
      break;
    case STATION:
      self = new Sprite(ResPack.WORLD_STATION1);
      self.setScale(1.5f);
      break;
    case STAR:
      self = new Sprite(ResPack.WORLD_SUN);
      self.setScale(2f);
      break;

    default:
      Gdx.app.log("Entity", "EntityType not found!");
      break;
    }
  }
```

I added the "setScale" in order to simulate size. A star should
be \*slightly\* larger than a space station. This is only a temporary
measure but I think it'll look better this way. You can of course leave
it out.

There is one thing we'll have to do to restore the game as it was before
and that is to actually use the "updatePosition" method that we created.
So in the input processor, instead of calling "setPosition" on the
sprite we should use our object methods.

``` {.lang:java .decode:true}
 if (moving) {
      Vector2 temp = new Vector2(e.getPosition().x, e.getPosition().y);
      temp.add(e.getMovement());
      e.setPosition(temp);
      e.updatePosition();
      e.fly();
    }
```

So far so good. Our code can now handle different types of objects,
though we will still need to create the objects at some point. And
because we want the world to keep tabs on everything going on we'll have
to update some code in our world method. See, we can add entities by
calling that 2nd lovely constructor and passing them into our world
object. We do that by calling.

``` {.lang:java .decode:true}
world.addEntity(new Entity(ENTITY_TYPE, ENTITY_POSITION));
```

Where Type and Position are of course one of our lovely EntityTypes that
we defined and the position is a Vector2 object. And where will we use
this dark magic you ask? Well simple. Where do we already add the player
to our world.

``` {.lang:java .mark:8-10 .decode:true}
  @Override
  public void create() {
    float w = Gdx.graphics.getWidth();
    float h = Gdx.graphics.getHeight();

    world = new World();
    world.addEntity(new Entity(EntityType.PLAYER, new Vector2(200, 150)));
    world.addEntity(new Entity(EntityType.STATION, new Vector2(600, 300)));
    world.addEntity(new Entity(EntityType.PLANET, new Vector2(1200, 600)));
    world.addEntity(new Entity(EntityType.STAR, new Vector2(650, 750)));
  }
```

In our main game create() method. Now render this and marvel at its
glory. You can of course change the coordinates. Note that those are
camera-world coordinates, not pixel-coordinates. Compile this, it
shouldn't throw any errors. (Unless I forget to mention something in the
post ;)

 

And well...that's it for this time, really. I hope that you learned a
thing or two and have also seen that the BEST way of implementing a new
feature is often to take a step back, look at the big picture and then
think about how it would be easiest to do something. Next issue I want
to show you how to UI which is an important thing when it comes to
creating a game. Also note, that all of my source code can be viewed on
my open repository on
[BITBUCKET](https://bitbucket.org/LaGemiNi/star-chaser "BITBUCKET") (which
is the name I've given to this name). There is also a video on my
[youtube](http://www.youtube.com/watch?v=ocYqXyM9v2Y "youtube") channel
from a week ago or so. Go check both things out.

Sorry that it took me a bit longer to get this one out. I had a lot on
my plate the last week. I'll try bring out two posts on here per week. I
have something slightly special planned for next Tuesday. Hint, it
involves a lot of hardware, FreeBSD and a RAID :)

But until next time, keep coding!
