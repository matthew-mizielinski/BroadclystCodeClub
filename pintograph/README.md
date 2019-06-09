# Pintograph test code

The aim of this code is to allow a receiver to be set up, connected to a PCF8574 I2C bus 
expander and two stepper motors. The receiver should read any radio messages and use them 
to modify the speed and direction of the two stepper motors.

The messages should be of the form `M S`, i.e. two space separated numbers where `M` is `1` 
or `2` and `S` is a signed integer, e.g. `-3` or `2`. The higher the number the faster the 
motors will turn. If `S` is positive then the corresponding motor should turn clockwise, 
otherwise it should turn anticlockwise. 
