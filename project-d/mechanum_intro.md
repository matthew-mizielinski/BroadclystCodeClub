# Project D

Project `D`, just `D` hereafter, is the fourth rover I've built after 
 * Audrey (Raspberry pi zero + camera & 2 wheels, dismantled), 
 * Bessie (microbit + 2 wheels)
 * Charlie (Raspberry Pi Zero + caterpilar tracks + servos & camera)
`D` will be given a name later in the year via a naming competition

`D` is controlled via a microbit and has 4 motors driving a set of ``mechanum`` wheels.
[Mechanum wheels](https://en.wikipedia.org/wiki/Mecanum_wheel) are interesting in that they 
consist of a set of rollers on the face of each wheel set at 45 degrees to the edge of the
wheel, and when rotated the overall effect is a force pushing perpendicular to the rollers,
i.e. at 45 degrees.

A set of mechanum wheels consists of two pairs of slightly different wheels one set being a mirror 
image of the other, with opposite corners having the same orientation.

There is a really nice set of diagrams of this [here](https://jellyfishbbhs.com/2018/11/30/mecanum-wheels/) (Team Jelly Fish blog)

![](https://jellyfishbbhs.com/wp-content/uploads/2018/11/mecanum1-1-e1548174009492.png "Team Jelly Fish ")

So by controlling each motor independently a host of different motions can be obtained.

To control all four motors would require 8 output pins on the microbit, which is more than it can comfortably provide. I've used an
I2C IO expander, essentially an 8-bit register than can be written to or read from using the I2C protocol, which is run of a dedicated
pair of pins from the microbit.

This protocol is really simple; send a number in a particular form to a particular address. The I2C io expander has a default address of
`0x20` for writing (`32` in decimal) so sending an 8 bit unsigned integer to it is sufficient to set the state of all four motors.
The motors are connected up in the following order (from most to least significant bits); front left, rear left, rear, right, front right
with two bits for each. For example, forward would be

 | Front left |     | Rear left |     | Rear right |     | Front right |     | control number  |
 | ---------- | --- | --------- | --- | ---------- | --- | ----------- | --- | --------------- |
 | 1          | 0   | 1         | 0   | 1          | 0   | 1           | 0   | = 170           |

As noted above the wheels provide driving force at 45 degrees


An example simple program that can run a sequence of different movements
Code: https://makecode.microbit.org/_iDEHRkKefX8L

<!---
<div style="position:relative;height:calc(300px + 5em);width:100%;overflow:hidden;"><iframe style="position:absolute;top:0;left:0;width:100%;height:100%;" src="https://makecode.microbit.org/---codeembed#pub:_iDEHRkKefX8L" allowfullscreen="allowfullscreen" frameborder="0" sandbox="allow-scripts allow-same-origin"></iframe></div>
---!>
