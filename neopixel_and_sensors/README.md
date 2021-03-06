# Neopixel activity with rotation sensors

## First activity : Coding

* Introduce the neopixel: a set of coloured leds that can be controlled with a single wire (+ power)
* The micro:bit has a great set of components; bluetooth, radio communications, accelerometer and compass are all built in
* the accelerometer on the microbit can be used to work out the "pitch" and "roll" angles of the microbit

 1. "Import" the neopixel extension
 1. On start : set the neopixel strip to have a single led connected to `P0`
 1. create `pitch` and `roll` variables
 1. create a function to get the pitch (input.. more section, look for `rotation` block) and map the number from -180..180 to 0..120 *
 1. copy get pitch function to get roll, changing the variable that is updated `pitch` -> `roll` and the angle read by the `rotation` block  
 1. In forever loop
   * get pitch
   * get roll
   * from "neopixel" add strip "show color" block, replace color with "red green blue" block from neopixel..more section.
   * set green to zero, blue to `pitch` and red to `roll`
   * from "neopixel" add the strip "show" block
   * pause for 100 ms

Connect the neopixel to the crocodile clip on the side with `+` `G` and `In` next to the pins; `+` to 3V, `G` to `GND` and `In` to pin 0.

Tilting the micro:bit with this programme should vary the colour from red to blue via purple.

Change the code by moving the `pitch` and `roll` variables to different elements of the `red green blue` block used to set the neopixel colour.

*This number was chosen to avoid the brightness of the micro:bit blinding me!

See [makecode page](https://makecode.microbit.org/_FqsY89Jpgas4) or [javascript code](neopixel_pitch_and_roll.js)

## Second activity : Amazing radio

Another feature of the microbit is the way that the radio can be used to pass information between micro:bits.

In [this makecode project](https://makecode.microbit.org/_7LiF20KJx0Ld) I've set up the microbit to use the same code to read the pitch and roll, but this is sent over radio to another microbit, which then sets the colour of the microbit.

The intention is to create pairs of microbits, in different radio groups, that are sending messages to each other and then ask the students to explain what is going on. Once they've worked it out show the code!

[javascript code](neopixel_radio.js)

## Another radio activity

With one microbit connected to the ZIP Halo (24 neopixel ring) and loaded with [this code](https://makecode.microbit.org/_h5R0XMYfWeXx)
adjust the code from the first activity to send a radio message containing the "colour" and the value of the "roll" variable each cycle of the forever loop ([green example](https://makecode.microbit.org/_KWwaLt9TXCkX)). Then with three microbits sending messages with colour set to either `red`, `green` or `blue`.
