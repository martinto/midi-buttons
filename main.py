import machine
from machine import Pin
from time import sleep
from serial import Serial
import midi

# Create a handler for a button press. There's no real
# need to debounce the buttons, multiple hits don't
# matter, it will just send repeated program change
# messages.
def make_button_handler(program_number):
  def _function(Pin):
    instrument.program_change(program_number)
  return _function

program_number = 1
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

uart = machine.UART(1,31250)
instrument = midi.Controller(Serial(uart), channel=1)

while True:
  sleep(1)
