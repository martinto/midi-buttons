from machine import Pin

class Buttons:
    _DEBUG = False
    GLOBAL_TOGGLE = 9
    COMBINATION = 1
    COMBINATION_BASE_GLOBAL = 0
    COMBINATION_BASE_MANUAL = 20
    PED_GT_COUPLER = 10
    PED_SWELL_COUPLER = 11
    CANCEL = 12
    INVALID = 0

    _buttonpins = [ 0, 2, 3 ]
    _buttonpins.extend(range(6, 15))
    _ledpin = 1
    _buttons = []
    _led:Pin
    _is_global = True
    _combination_base = COMBINATION_BASE_GLOBAL

    def __init__(self, handler, handle_button_irq) -> None:
        if self._DEBUG:
            print("Buttons init")
        for b in self._buttonpins:
            if self._DEBUG:
                print(f"Buttons init pin={b}")
            p = Pin(b, Pin.IN, 0, value=1)
            self._buttons.append(0)
            p.irq(trigger = Pin.IRQ_RISING, handler = lambda p, b=b:handler(p, self._buttonpins.index(b)))
            handle_button_irq(p, self._buttonpins.index(b))
        self._led = Pin(self._ledpin, Pin.OUT)
        if self._is_global:
            self._led.high()


    def _button_type(self, n:int):
        if n == 0:
            self._is_global = not self._is_global
            if self._is_global:
                self._combination_base = Buttons.COMBINATION_BASE_GLOBAL
                self._led.high()
            else:
                self._combination_base = Buttons.COMBINATION_BASE_MANUAL
                self._led.low()
            return Buttons.INVALID
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
        if self._DEBUG:
            print(f"n={n} btn_t={btn_t}")
        pc = Buttons.INVALID
        if btn_t == Buttons.GLOBAL_TOGGLE:
            pc = Buttons.GLOBAL_TOGGLE
        elif btn_t == Buttons.COMBINATION:
            pc = n + self._combination_base
        elif btn_t == Buttons.PED_GT_COUPLER:
            pc = Buttons.PED_GT_COUPLER
        elif btn_t == Buttons.PED_SWELL_COUPLER:
            pc = Buttons.PED_SWELL_COUPLER
        elif btn_t == Buttons.CANCEL:
            pc = Buttons.CANCEL
        return pc