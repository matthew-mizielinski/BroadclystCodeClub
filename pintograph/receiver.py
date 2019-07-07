"""
Code to run two stepper motors via a PCF8574 I2C bus expander from a microbit.
Radio messages are to be used to modify the speeds of each motor (untested)
"""
from microbit import *
import radio
import ustruct

# MOTORS contains the bit messages that need to be sent to the PCF8574
# in order to move the stepper motors.
# Each hex digit, or word, indicates the state on the four pins used by the 
# ULN2003 driver;
# word : pin states
# 9    : 1 0 0 1
# C    : 1 1 0 0
# 6    : 0 1 1 0
# 3    : 0 0 1 1
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
    result = mi
    # Need to avoid speeds of 1, -1 resulting in zero movement
    if i % (abs(speed) + 1) != 0:
        if speed > 0:
            result = (mi + 1) % NUM_STEPPER_STATES
        elif speed < 0:
            result = (mi - 1) % NUM_STEPPER_STATES

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
        message = radio.receive_full()()
        if message is None:
            break
        motor, speed = interpret_packet_value_pair(message[0])
        if motor is None:
            return speed1, speed2
        if motor == 'left':
            speed2 = int(speed)
        elif motor == 'right':
            speed1 = int(speed)
    return speed1, speed2


def interpret_packet_value_pair(data):
    """
    Return a name, value pair extracted from the 
    data packet sent by Makecode Radio.
    Adapted from https://github.com/rhubarbdog/microbit-radio/blob/master/make_radio.py
    
    Paramters
    ---------
    data : bytes
        Packet payload
        
    Returns
    -------
    : str
        Name of value (or None if not a value 
        pair packet)
    : float
        Value (or None if not a value pair packet)
    """
    if data is None:
        return None, None
    packet_type = int.from_bytes(data[3:4], 'little')
    name = value = None
    if packet_type == 5:
        name = str(data[21:29], 'ascii').strip()
        value = ustruct.unpack('<d', data[12:20])[0]
    return name, value


if __name__ == '__main__':
    # Set up I2C bus
    i2c.init()
    # Switch radio on.
    radio.on()
    radio.config(group=42)
    #initial speeds
    speed1 = 2
    speed2 = -1
    
    # infinite loop
    while True:
        # Update speeds from any radio messages
        speed1, speed2 = update_speeds(speed1, speed2)
        print(speed1, speed2)
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
