#!/bin/bash

ampy --port /dev/ttyACM0 put midi/midi.py
ampy --port /dev/ttyACM0 put serial.py
ampy --port /dev/ttyACM0 put main.py