"""
Code to run two stepper motors via a PCF8574 I2C bus expander from a microbit.
Radio messages are to be used to modify the speeds of each motor (untested)
"""
from microbit import *
import radio

# the bit messages that need to be sent to the PCF8574
# in order to move the stepper motors
MOTORS = [[b'\x99', b'\x9C', b'\x96', b'\x93'],
          [b'\xC9', b'\xCC', b'\xC6', b'\xC3'],
          [b'\x69', b'\x6C', b'\x66', b'\x63'],
          [b'\x39', b'\x3C', b'\x36', b'\x33'],
          ]
NUM_STEPPER_STATES = 4
PCF8574_ADDRESS = 0x20


def _speed_action(i, speed, mi):
    """
    Return the index in MOTORS of the next state to be used.
    """
    # Need to avoid speeds of 1, -1 resulting in zero movement
    if i % (abs(speed) + 1) != 0:
        if speed > 0:
            result =  (mi + 1) % NUM_STEPPER_STATES
        elif speed < 0:
            result = (mi - 1) % NUM_STEPPER_STATES
    else:
        result = mi
    return result


def run(address, nsteps, speed1=6, speed2=6):
    """
    Step through the motor sequence for nsteps at
    the specified speeds by talking to the I2C 
    8bit output device at the specified address.
    """
    m1i = 0
    m2i = 0
    for i in range(nsteps):
        m1i = _speed_action(i, speed1, m1i)
        m2i = _speed_action(i, speed2, m2i)
        
        byte_to_send = MOTORS[m1i][m2i] 
        try:
            i2c.write(address, byte_to_send)
        except:
            display.show(Image.SURPRISED)
            sleep(1000)
            break
        sleep(5)


def update_speeds(speed1, speed2):
    while True:
        message = radio.receive()
        if message is None:
            break
        motor, speed = message.split()
        if motor == '1':
            speed1 = int(speed)
        elif motor == '2':
            speed2 = int(speed)
    return speed1, speed2


if __name__ == '__main__':
    # Set up I2C bus
    i2c.init()
    # Switch radio on.
    radio.on()
    #initial speeds
    speed1 = 2
    speed2 = -1
    
    # infinite loop
    while True:
        # Update speeds from any radio messages
        speed1, speed2 = update_speeds(speed1, speed2)
        # look for i2c devices
        devices = i2c.scan()
        # If the PCF8754 is found
        if PCF8574_ADDRESS in devices:
            # be happy and run for 100 steps
            display.show(Image.HAPPY)
            run(PCF8574_ADDRESS, 100, speed1=speed1, speed2=speed2)
        else:
            # show sad and sleep for a second.
            display.show(Image.SAD)
            sleep(1000)
