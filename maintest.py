from machine import Pin
from time import sleep
from buttons import Buttons
from debounce import DebouncedSwitch
import midi

MIDICHANNEL=4
MIDI_TX = 4
MIDI_RX = 5
UART_1 = 1

def handle_button_irq(x:Pin, n:int):
    DebouncedSwitch(x, button_pressed, [x, n])

def button_pressed(x):
    if x[0].value():
        print(f"{x[1]}: True")
    else:
        print(f"{x[1]}: False")

mport = midi.Midi(UART_1, tx=MIDI_TX, rx=MIDI_RX)
buttons = Buttons(handle_button_irq)

while True:
    sleep(1)