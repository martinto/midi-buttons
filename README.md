# MIDI Buttons

GPIO inputs are connected to buttons and there is a single LED. Pin numbers are enumerated in the `Buttons` class.

The button connected to GPIO0 toggles between global combinations and ones for the local manual. The group of eight buttons send 1-8 for global and 21-28 for manual combinations. The rest are couplers and the cancel button.

## Installation

Instal micropython, download the files and on the target rename `maintest.py` to `main.py`