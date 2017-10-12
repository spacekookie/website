Title: Open Plantb0t - Rev A
Category: Blog
Date: 2016-03-16 12:08
Tags: Dev Diary, Hardware
Illustration: banners/plantb0t_revA.png

Howdy everybody,

Spring is coming in Berlin and thus my thoughts - as every year - are with plants. And growing shit. I live in an appartment with a tiny tiny balcony so I don't have much space but that has never stopped me from wanting to cram as many plants into the space as possible to the point of starting nuclear fusion.

In addition to that I have a few house-plants and very water-sensitive trees in my appartment. My current approach is to go around with a jug of water every couple of days and water them individually - making sure the soil has a certain moisture and doesn't exceed a certain limit - but I've always had the dream of being able to automate away as much as possible. That's where the idea of `Plantb0t` started. And I want to tell you a little bit about it.

The basic idea is to have a little controller in each plant-pot that measure the moisture of the soil and reports that back to me via an ESP-12 SOM (System on a Module). The ESP has WiFi capabilities and would log to an MQTT server on my home media server. This way (when I'm at home - none of that IoT shit) I can see how my plans are doing.

### Current state

So that's what Revision A of Plantb0t is. I also added a second sensor slot which is meant to be populated by a temperature sensor but could theoretically house a second moisture sensor. In the end the probes are only sticks in the ground that have a resistance between them.

Here is a dynamic render of the board (that went into prototype production on the 29th of march, 2016).

![Plantb0t Rev A](/images/plantb0t_RevA_front.png Plantb0t Revision A)

As you can see it's powered by an ESP-12 and comes with it's own programmer (The lovely CP2102) and micro-USB header. The USB-Port is currently the only way to power the board.

In the future it is planned to bypass the USB power and only use it for the programmer and otherwise drive everything off an externla powerboard which provides 3.3V for the Plantb0t.

In the bottom you see two constant current sources that can power two analogue sensors that get multiplexed into the ADC of the ESP-12.

GPIO pin headers are included for external gismoz such as a pump to act on the moisture data as well as screwholes to mount the whole thing in a 3D printed case.

In total the board is only 5x5cm big!

### Future plans

A few things I want to realise with this project in the next coming weeks:

 - Primarily the Rev A board needs to be tested to make sure that the programmer works
 - Figure out a good way to calibrate the sensors. Maybe drive a button via GPIO?
 - Design a power board that generates 3.3V for the board (but not the programmer!) from a solar panel and a battery to decouple the entire sensor-board from all power-sockets.

For the next revision of the board (Rev B) I want to include more sensor slots. Maybe work on the part spacing a bit and increase footprint sizes. It should be easier to solder and someof the parts are ridiculously small. I mean...I have the whole back to work with?

I also have some crazy ideas for a "Plantb0t+" Version with even MOAR SENSORS (Including a pH-value sensor!). But that's all faaaaar in the future.

Either way...I'm excited for my boards to get here (hopefully in the next 7-8 days) as well as all the parts I need for the prototypes.

I leave you with a screenshot from KiCad where you get to see under the hood of the board. Cheers o/

![Plantb0t Rev A](/images/plantb0t_RevA_naked.png Plantb0t)

(The project has a [Github](https://github.com/spacekookie/open_plantb0t) repo where I will try to populate the wiki with as much info as possible)