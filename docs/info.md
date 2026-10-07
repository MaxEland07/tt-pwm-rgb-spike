## How it works

Three PWM channels share one counter that counts 0, 1, 2. A colour output is high while the counter is below that colour's level, so level 3 is always on and level 0 is off.

## How to test

Set ui[1:0], ui[3:2] and ui[5:4] to the red, green and blue levels (0 to 3) and watch uo[2:0].

## External hardware

An RGB LED on uo[0], uo[1] and uo[2].
