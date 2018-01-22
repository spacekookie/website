Title: WS2812b LED breakouts
Category: OldBlog
Date: 2016-03-16 12:08
Tags: Dev Diary, Hardware

You all know I have a fetish for [ws2812b RGB-LEDs](http://rgb-123.com/wp-content/uploads/2013/08/PinLayout.jpg). I admit that. They're just awesome. And recently I've found myself wanting to do some projects with them (*cough* programmable alarm clock *cough*). But I dislike the strips, although they're pretty cheap they are usually just very messy and horrible. And making a PCB for every project can be weird. Especially if gigantic PCBs would be required.

So I designed this little doodad.

![ws2812b Single Mount](/images/ws_2812b_single.png ws2812b Single Mount)

The idea is the following: Sometimes you just need a few ws2812b (I'm saying that word too often in this post) somewhere. But you don't want to lay a strip. Or make a big PCB for it.
So here is an alternative. Easily make ~800 of these for 25$, screw them to a surface, connect **PRETTY** wires between them, such as [Ribbon cables](http://cdn.usdigital.com/assets/images/galleries/ca-c10-f-c10_0.jpg) and boom. You're done.

### One to rule many

Now...I mentioned that programmable alarm clock earlier. And while I'm not quite done designing what will go into it all, I do know that I want to have a ~ 21x9 Pixel display, each individually addressable. And instead of building a way too big PCB that will be insanely expensive to manufacture...why not split them up? Then I have these "tiles" of LEDs that I screw to a backplate, wire everything together and from the outside you can't tell the difference.

With 21:9 (Aspect ratio and pixels) in mind, this is my prototype:

<TO BE CONTINUED>