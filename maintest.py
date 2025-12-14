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
    if DEBUG:
        print(f"Button IRQ: {n} value:{x.value()}")
    DebouncedSwitch(x, button_pressed, [x, n], delay = 25)

def button_pressed(x):
    if DEBUG:
        print(f"button_pressed x={x} value:{x[0].value()} n={x[1]}")
    if x[0].value():
        button_number = x[1]
        pc = buttons.midi_pc_number(button_number)
        if DEBUG:
            print(f"button_pressed pc={pc}")
        if pc != Buttons.INVALID:
            if DEBUG:
                print(f"{button_number}: {pc} value:{x[0].value()}")
            mport.send_program_change(MIDICHANNEL, pc)

mport = midi.Midi(UART_1, tx=MIDI_TX, rx=MIDI_RX)
buttons = Buttons(handle_button_irq, handle_button_irq)

while True:
    sleep(1)