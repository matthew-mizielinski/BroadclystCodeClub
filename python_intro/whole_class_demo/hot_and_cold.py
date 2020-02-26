# Documentation can be found via 
# https://microbit-micropython.readthedocs.io

# Load routines that allow us to use the microbit
from microbit import *
# load radio library if we need it
import radio
# load neopixel library if we need it
# import neopixel

# Code to run on start
radio.on()
# listen on channel 99
radio.config(group=99)

# end of on start code


def forever():
    """
    Code to run again and again
    """
    details = radio.receive_full()
    if details is not None:
        message, strength, timestamp = details
        update_display(strength)


def update_display(strength):
    """
    update display depending on strength
    """
    num_pixels = int(0.5 * (strength - 90))
    display.clear()
    for i in range(num_pixels):
        x = i % 5
        y = i // 5
        display.set_pixel(x, y, 9)


# main program loop
while True:
    # forever code
    forever()
