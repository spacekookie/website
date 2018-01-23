Title: Jolly Christmas Decoration
Category: Blog
Date: 2015-09-17 15:30
Tags: /dev/diary, hardware

Christmas is getting closer (not really but let's just roll with it) and I wanted to learn [KiCad](www.kicad-pcb.com) a software that let's you create circuits and design PCB for manufacture.

I found a tutorial series online by a guy named [Ashley Mills](https://www.youtube.com/channel/UCaBNA-lmg35Wfx2eh2oDkWg) (with quite a legendary beard) who showed off a simple circuit using a 555-timer, a shift register and an XOR gate made from NPN transistors and resistors to display and repeat a pattern on several LED's.

The series focused on getting to know KiCad and all it's features. And while I did that in the first revision of my board, I've diverged from it since. I can however recommend his videos on KiCad to anyone who wants to dive into PCB design, has no clue about the software and could use a little chuckle while also learning some really awesome software (youtube channel link above).

# My Christmas Bauble

So this is what I've got.

![Kookies Christmas Bauble](/images/christmas_bauble_pcb.png "Kookies Christmas Bauble")

As you can see it's a round PCB with simple 5mm LED's around the edges. It no longer uses NPN transistors but rather a single SMD XOR gate. Much easier to wire up, cheaper and less prone to errors as well.

In general I've switched the entire design over to primarily use SMD components as they're smaller and more elegant. And it theoretically allowed me to get the footprint of the board down to something that isn't too excruciatingly expensive to produce.

It took me two more revisions to get the board to a state where it's not too complex and actually fit on a single layer (!) with no vias except for the holes for the LED's obviously.

It uses a round cell battery on the back of the board to hide it away and has a hole at the top to actually hang off a christmas tree. Theoretically the battery should lasta few days, so maybe have a few spare ones around in the christmas season.

# What now?

I haven't manufactured this yet. I am still thinking about refining the design slightly. I have the **entire** back to work with and add things. I was thinking about adding a simple bluetooth chip so that patterns could be pushed to the device via an android app. But that's the future. For now it should actually be functional and maybe I'll order some `Revision 3` boards just to see that everything worked.

Here is a dynamic render from KiCad as well.
![Kookies Christmas Bauble Rendered](/images/christmas_bauble_render.png "Kookies Christmas Bauble Rendered")

And be sure to checkout my Github repo for the project if you want the KiCad files. Either to play around with them or to manufacture some baubles yourself. If you do, I'd be interested in pictures of the decorations on your christmas trees so I can add them to this article as a slideshow 😊
