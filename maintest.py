from machine import Pin
from time import sleep
from buttons import Buttons
from debounce import DebouncedSwitch
import midi

DEBUG=False
MIDICHANNEL=4
MIDI_TX = 4
MIDI_RX = 5
UART_1 = 1

def handle_button_irq(x:Pin, n:int):
    DebouncedSwitch(x, button_pressed, [x, n])

mport = midi.Midi(UART_1, tx=MIDI_TX, rx=MIDI_RX)
buttons = Buttons(handle_button_irq)

def button_pressed(x):
    if x[0].value():
        button_number = x[1]
        pc = buttons.midi_pc_number(button_number)
        if pc != Buttons.INVALID:
            if DEBUG:
                print(f"{button_number}: {pc}")
            mport.send_program_change(MIDICHANNEL, pc)

while True:
    sleep(1)