from pynput.mouse import Listener, Button, Controller as MouseController
from pynput.keyboard import Controller as KeyboardController
import pyautogui as pa
import time
pa.FAILSAFE = False

def pyauto(point, write):
    pa.moveTo(point["x"], point["y"], duration=.1)
    pa.click(button="left", clicks=1)
    if write:
        pa.click(button="left", clicks=2)
        pa.typewrite(point["text"])

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def py():
    with Listener(on_click=on_click) as listener:
        listener.join()

list = [
    { "x": 553, "y": 435, "text": "chuong dep trai" },
    { "x": 620, "y": 515, "text": "vai ca lon" },
    { "x": 443, "y": 637, "text": "placeholder" }
]

if __name__ == "__main__":
    for i in range(len(list)-1):
        pyauto(list[i], write=True)
    pyauto(list[2], write=False)