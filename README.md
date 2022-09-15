# Midi Buttons

Midi Buttons is a micropython program for the [Rasperry PI Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/) microcontroller. It sends program change commands on Midi channel 1 (change ```MIDICHANNEL``` in the code to alter the channel) when a button is pressed.

It is intended for used for preset buttons with [Grand Orgue](https://github.com/GrandOrgue/grandorgue).

## Installation

Clone this repository and fetch the micropython midi library by updating git submodules.

```git submodule update --init --recursive```

The Pico must have [micropython loaded](https://micropython.org/download/rp2-pico/).

Run this command if hosted on Linux:

```./upload.sh```

The upload script copies midi/midi.py serial.py and main.py to the Pico using [ampy](https://mikeesto.medium.com/uploading-to-the-raspberry-pi-pico-without-thonny-53de1a10da30). Alternatives would be to use Thonny to transfer those files, all of which should be in the root of the Pico Python filesystem.

The program will start once the board is reset.

## Hardware

### You will need

 * A five pin DIN socket
 * One 33 ohm resistor
 * One 10 ohm resistor
 * Up to 24 buttons

### Wiring

 * Connect the 33 ohm resistor between Pico pin 36(3V3(OUT)) and DIN pin 4.
 * Connect the 10 ohm resistor between Pico pin 6 (UART1 TX) and DIN pin 5.
 * Connect Pico pin 38 (GND) to DIN pin 2 and the casing.
 * Connect Pico pin 36 (3V3(OUT)) to one terminal on all buttons.
 * Connect the other button terminals to GP0 through GP28 missing out GP4 and GP5 which are the UART connections for the Midi data.

## Midi Data

When a button is pressed a program change command on Midi channel 1 is sent. GP0 sends program 1, GP2 program 2 etc., up to GP28 which sends program 27.

## Midi Library

The midi library (pulled in as a submodule from [cjbarnes18/micropython-midi](https://github.com/cjbarnes18/micropython-midi)) is written for a pyboard and requires a Serial class which isn't part of the Pico SDK. The serial.py file in this project implements enough of that class to enable the sending of Midi data.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Licence

[GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](LICENSE)