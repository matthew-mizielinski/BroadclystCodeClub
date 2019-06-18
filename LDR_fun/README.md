# Light meter and Vortex speed

## Light meter

Step through constructing the [Light meter code](https://makecode.microbit.org/_180Yd9ExrUDk)
Connect Light dependent resistor (LDR) with middle cable connected to P0, the pin connected to the other end of the LDR to `3V`, and the one connected to the resistor to `GND`.

Look around room to find places with the lowest and highest readings (go outside if possible).

If possible disconnect LDR and connect it up the other way around without the students seeing to produce a "darkness" meter, i.e. brighter -> lower reading.

## Vortex cannon fun
 * Load [LDR driven timer](https://makecode.microbit.org/_hgoMTbh1bbfH) code into a microbit.
 * Connect `P0` to middle pin of first LDR, `P1` to middle pin of second LDR.
 * Connect `GND` from microbit to a penny and then ground from two sensors to the same penny
 * Connect `3V` from microbit to a penny and then +V from two sensors to this penny.
 * measure distance between LDRs
 * Check ldr 1 working using button A to get reading
 * check ldr 2 working using button B to get reading.
 * Cover both LDR with cover
 * press A+B to prime timer (shows `:-o`)
 * blow covers off with vortex cannon
 * shows `:-)` and then the time between covers coming off in milliseconds
 * add data to spreadsheet
 * repeat 4 or 5 times per distance, use 3 or 4 distances (20 to 70 cm work well)
 * gradient from spreadsheet gives vortex speed.
