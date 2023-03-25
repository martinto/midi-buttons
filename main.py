import machine
from machine import Pin
from time import sleep
from serial import Serial
import midi

# If UARTNUMBER is changed then the wiring will have to change
# along with the ranges for the for loops which set up the
# button GPIO pins.
UARTNUMBER=1
# This can safely be changed.
MIDICHANNEL=4
BUTTONS=[None]*29
BUTTON_STATE=[1]*29

uart = machine.UART(UARTNUMBER,31250)
INSTRUMENT = midi.Controller(Serial(uart), channel=MIDICHANNEL)

for pinno in range(0, 4): # pin 0-3
  BUTTONS[pinno] = Pin(pinno, Pin.IN, Pin.PULL_UP)
for pinno in range(6, 29): # pin 6-28
  BUTTONS[pinno] = Pin(pinno, Pin.IN, Pin.PULL_UP)

while True:
  for pinno in range(0, 4): # pin 0-3
    if BUTTONS[pinno].value() != BUTTON_STATE[pinno]:
      BUTTON_STATE[pinno] = BUTTONS[pinno].value()
      if BUTTON_STATE[pinno] == 0:
        print("Global ", pinno, " down")
        INSTRUMENT.control_change(pinno + 1, 1)
  for pinno in range(6, 9): # pin 6-8
    if BUTTONS[pinno].value() != BUTTON_STATE[pinno]:
      BUTTON_STATE[pinno] = BUTTONS[pinno].value()
      if BUTTON_STATE[pinno] == 0:
        print("Global ", pinno, " down")
        INSTRUMENT.control_change(pinno + 1, 1)
  for pinno in range(9, 12): # pin 9-11
    if BUTTONS[pinno].value() != BUTTON_STATE[pinno]:
      BUTTON_STATE[pinno] = BUTTONS[pinno].value()
      if BUTTON_STATE[pinno] == 0:
        print("Coupler ", pinno, " down")
        INSTRUMENT.program_change(pinno + 1)
  sleep(0.001)
