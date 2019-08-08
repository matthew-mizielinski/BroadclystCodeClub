# Radio control of Bessie

## Configuring BessieBitBot for radio.

[This makecode project](https://makecode.microbit.org/_CHRUs56Dz1U1) sets Bessie up to listen on radio group **21** for 
(`name`, `value`) pairs, where `name` is a string and `value` is a number.

If `name` is `"left"` or `"right"` the corresponding `value` is used to control the left or right motor. If the `value` is greater 
than a `threshold` (controlled by button "A") then the corresponding motor will move forward, if the `value` is less than 
`-1 * threshold` it will reverse. The `threshold` is included to allow a motor to be stopped without having to have the controling 
microbit perfectly level. 

## The Controllers

 1. In the `on start` block set radio group to **21**
 1. create a variable called `pitch`
 1. write a function called `get pitch`
    * set `pitch` to `map`(`rotation pitch`  from `-180`, `180` to `-10`, `10`)
 1. In the `forever` loop
    * call `get pitch` function
    * On one microbit use the radio to send name `"left"` = variable`pitch`
    * On the other send  `"right"` = variable `pitch`
    * Pause for 100 ms

Note that the behaviour of the controllers is likely to be the reverse to that expected.

https://makecode.microbit.org/_PMjLPVWC7JDi
