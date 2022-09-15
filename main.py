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
MIDICHANNEL=1

# Create a handler for a button press. There's no real
# need to debounce the buttons, multiple hits don't
# matter, it will just send repeated program change
# messages.
def make_button_handler(program_number):
  def _function(Pin):
    instrument.program_change(program_number)
  return _function

program_number = 0
def setup_handler(pin, program_number):
  handler = make_button_handler(program_number)
  button = Pin(pin, Pin.IN, Pin.PULL_DOWN)
  button.irq(trigger=Pin.IRQ_RISING, handler=handler)

for pin in range(0, 4): # pin 0-3
  setup_handler(pin, program_number)
  program_number += 1

for pin in range(6, 29): # pin 6-28
  setup_handler(pin, program_number)
  program_number += 1

uart = machine.UART(UARTNUMBER,31250)
instrument = midi.Controller(Serial(uart), channel=MIDICHANNEL)

while True:
  sleep(1)
