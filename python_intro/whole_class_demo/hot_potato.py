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
# transmit on channel 99
radio.config(group=99)

# end of on start code


def forever():
    """
    Code to run again and again
    """
    radio.send('Hot potato')
    toggle_pixel(0, 0)
    sleep(2000)

    
def toggle_pixel(x, y):
    """
    If pixel is on set it to off and vice versa)
    """
    value = display.get_pixel(x, y)
    display.set_pixel(x, y, abs(9 - value))

# main program loop
while True:
    # forever code
    forever()
