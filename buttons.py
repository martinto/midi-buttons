from machine import Pin

class Buttons:
    _buttonpins = [ 0, 2, 3 ]
    _buttonpins.extend(range(6, 15))
    _ledpin = 1
    _buttons = []
    _led:Pin
    _is_global = True

    GLOBAL_TOGGLE = 9
    COMBINATION = 1
    PED_GT_COUPLER = 10
    PED_SWELL_COUPLER = 11
    CANCEL = 12
    INVALID = 0

    def __init__(self, handler) -> None:
        for b in self._buttonpins:
            p = Pin(b, Pin.IN, Pin.PULL_UP)
            self._buttons.append(0)
            p.irq(trigger = Pin.IRQ_FALLING, handler = lambda p, b=b:handler(p, self._buttonpins.index(b)))
        _led = Pin(self._ledpin, Pin.OUT)
        if self._is_global:
            _led.high()


    def _button_type(self, n:int):
        if n == 0:
            return Buttons.GLOBAL_TOGGLE
        elif n < 9:
            return Buttons.COMBINATION
        elif n == 9:
            return Buttons.PED_GT_COUPLER
        elif n == 10:
            return Buttons.PED_SWELL_COUPLER
        elif n == 11:
            return Buttons.CANCEL
        else:
            return Buttons.INVALID

    def midi_pc_number(self, n:int) -> int:
        btn_t = self._button_type(n)
        pc = Buttons.INVALID
        if btn_t == Buttons.GLOBAL_TOGGLE:
            pc = Buttons.GLOBAL_TOGGLE
        elif btn_t == Buttons.COMBINATION:
            pc = n
        elif btn_t == Buttons.PED_GT_COUPLER:
            pc = Buttons.PED_GT_COUPLER
        elif btn_t == Buttons.PED_SWELL_COUPLER:
            pc = Buttons.PED_SWELL_COUPLER
        elif btn_t == Buttons.CANCEL:
            pc = Buttons.CANCEL
        return pc