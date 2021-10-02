# OpenSalami

Open source game console

## Hardware

* Raspberry Pi Pico
* 1.3" 128x64 SH1106 OLED Display
* 2x 4.7 uF Capacitor
* 2x 10kOhm Resistor
* 2x 3.7kOhm Resistor
* 2 buttons
And a whole lotta jumper cables

## Firmware

To install:
* Make sure you have MicroPython on the Pi
* Upload the files in `upload-contents-to-pico` to the root of the RPi Pico filesystem via Thonny

The current version has experimental code in `firmware-src`. `upload-contents-to-pico` contains an older version of the code that blinks a triangle on the title screen, and that's it.

I am not a professional developer. I learn many of the concepts myself and thus the code is unlikely to be up to many standards. Feel free to make your own fork if you want to.
