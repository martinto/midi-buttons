from machine import Pin

class Buttons:
    _buttonpins = [ 0, 2, 3 ]
    _buttonpins.extend(range(6, 15))
    _ledpin = 1
    _buttons = []
    _led:Pin
    _is_global = True

    def __init__(self, handler) -> None:
        for b in self._buttonpins:
            p = Pin(b, Pin.IN, Pin.PULL_UP)
            self._buttons.append(0)
            p.irq(trigger = Pin.IRQ_FALLING, handler = lambda p, b=b:handler(p, self._buttonpins.index(b)))
        _led = Pin(self._ledpin, Pin.OUT)
        if self._is_global:
            _led.high()

