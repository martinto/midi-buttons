"""
Implement enough of the 'pyb' Serial class to get the Midi class working.
"""

class Serial:
  def __init__(self, uart):
    self.port = uart

  def send(self, msg, timeout):
    # timeouts don't exist in the Pico UART SDK.
    if isinstance(msg, int):
      to_send = msg.to_bytes(1, 'big')
    else:
      print(type(msg))
      to_send = msg

    print("msg='{msg}' to_send='{to_send}'".format(msg = msg, to_send = to_send))
    self.port.write(to_send)
