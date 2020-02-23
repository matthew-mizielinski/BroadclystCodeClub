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
    details = radio.receive_full()
    if details is not None:
        message, strength, timestamp = details
        update_display(strength)


def update_display(strength):
    min_strength = -30
    max_strength = 0
    strength_range = max_strength - min_strength
    
    num_pixels = 25 * (strength - min_strength) / strength_range

    for i in range(num_pixels):
        x = i % 5
        y = i // 5
        display.set_pixel(x, y, 9)


def on_button_A():
    """
    Code to run when button A is pressed on its own
    """
    pass


def on_button_B():
    """
    Code to run when button B is pressed on its own
    """
    pass


def on_button_AB():
    """
    Code to run when button A+B are pressed together
    """
    pass


def on_shake():
    """
    Code to run when the accelerometer detects the
    microbit is being shaken
    """
    pass


# Code to run on start
radio.on()
# listen on channel 99
radio.config(group=99)

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
