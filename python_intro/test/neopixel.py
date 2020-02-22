# Documentation can be found via 
# https://microbit-micropython.readthedocs.io

# Load routines that allow us to use the microbit
from microbit import *
# load radio library if we need it
# import radio
# load neopixel library if we need it
import neopixel


def forever():
    """
    Code to run again and again
    """
    rotate(direction)
    sleep(200)


def on_shake():
    """
    Code to run when the accelerometer detects the
    microbit is being shaken
    """
    direction = -1 * direction


def rotate(n):
    """
    Rotate neopixels by n places
    """
    # get current state of neopixels
    pixel_colours = []
    for i in range(NPIXEL):
        pixel_colours.append(np_strip[i])
    
    if n == 1:
        # get colour of last pixel
        last_colour = pixel_colours.pop(-1)
        # put it at the front of the list
        pixel_colours.insert(0, last_colour)
    elif n == -1:
        # get colour of first pixel
        first_colour = pixel_colours.pop(0)
        # put it at the end of the list
        pixel_colours.append(first_colour)
    
    # put colours back on strip
    for i in range(NPIXEL):
        np_strip[i] = pixel_colours[i]
    
    # show colours
    np_strip.show()
    
# on start code

# how many pixels do we have
NPIXELS = 8

# set up "strip" object attached to pin 0
np_strip = neopixel.NeoPixel(pin0, NPIXELS)

# Colours for the neopixels
brightness = 100
# colour = (red, green, blue)
# Primary
RED = (brightness, 0, 0)
GREEN = (0, brightness, 0)
BLUE = (0, 0, brightness)

# Secondary
YELLOW = (brightness // 2, brightness // 2, 0)
MAGENTA = (brightness // 2, 0, brightness // 2)
CYAN = (0, brightness // 2, brightness // 2)

# Other
WHITE = (brightness // 3, brightness // 3, brightness //3)
BLACK = (0, 0, 0)

ORANGE = (brightness * 2 // 3, brightness // 3, 0)
PINK = (brightness * 2 // 3, 0, brightness // 3)
VIOLET = (brightness // 3, 0, brightness * 2 // 3)
INDIGO = (0, brightness // 3, brightness * 2 // 3)
SPRING_GREEN = (0, brightness * 2 // 3, brightness // 3)

colour_list = [
   RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, WHITE
]

# Code to set initial colours
# this will set the first pixel on the strip to the first colour in the list
# and the set the second pixel to the second colour, etc.
np_strip[:] = colour_list

# send information on the neopixel colours to the strip
np_strip.show()

# define a variable to control which direction to shift the neopixels;
direction = 1

# main program loop
while True:
    # forever code
    forever()

    # shake
    if accelerometer.was_gesture('shake'):
        on_shake()
