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
    sleep(200)


def on_shake():
    """
    Code to run when the accelerometer detects the
    microbit is being shaken
    """
    pass


# on start code
NPIXELS = 8
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


# show  neopixel colours
np_strip.show()

# main program loop
while True:
    # forever code
    forever()

    # shake
    if accelerometer.was_gesture('shake'):
        on_shake()
