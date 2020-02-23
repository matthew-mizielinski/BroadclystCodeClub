# Documentation can be found via 
# https://microbit-micropython.readthedocs.io

# Load routines that allow us to use the microbit
from microbit import *
# load radio library if we need it
import radio
# load neopixel library if we need it
# import neopixel


def forever():
    """
    Code to run again and again
    """
    radio.send('Hot potato')
    sleep(sleep_time)


def on_button_A():
    """
    Code to run when button A is pressed on its own
    """
    sleep_time -= 1000


def on_button_B():
    """
    Code to run when button B is pressed on its own
    """
    sleep_time += 1000


def on_button_AB():
    """
    Code to run when button A+B are pressed together
    """
    sleep_time = 5000


# Code to run on start
radio.on()
# transmit on channel 99
radio.config(group=99)

sleep_time = 5000

# end of on start code

# main program loop
while True:
    # forever code
    forever()
    # buttons
    if button_a.is_pressed() and button_b.is_pressed():
        on_button_AB()
    elif button_a.is_pressed():
        on_button_A()
    elif button_b.is_pressed():
        on_button_B()
