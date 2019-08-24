# Dummies guide to setting up micropython fireflies on microbit

1. Open https://python.microbit.org and clear all text in the editor
1. Copy code from https://microbit-micropython.readthedocs.io/en/v1.0.1/tutorials/radio.html#fireflies and paste into 
   the "Micro:bit - python editor" page
1. Change the "Script name" to `micropython-fireflies.hex`
1. Click on "Download" and copy the resulting file to the microbit

## Running fireflies

As noted in the fireflies tutorial page above, when button A is pressed the microbit sends a signal to other microbits
over the radio, which then flash after a short random length delay. 
There is then a 1 in 10 chance that the microbit will send the signal again.
If only a few microbits are powered then you are unlikely to see a second flash, but as the number of microbits approaches
10 it becomes more likely. With more than 10 microbits at once the flashing can go on for quite a long time!

It is possible to separate the microbits into smaller groups which only trigger flashes within the group. To do this add 
the line
```
radio.config(channel=21)
```
after the `radio.on()` line. This will set those microbits with the extra line to only listen on channel 21 -- change this
number as required for the different groups. 

For smaller groups it could be useful to get the signal sent again with a higher than 1 in 10 chance. To do this alter
```
    if random.randint(0, 9) == 0:
```
to
```
    if random.randint(0, 3) == 0:
```
which will give a 1 in 4 chance (if a random number chosen from `0`, `1`, `2`, `3` is `0` then send the signal again).
