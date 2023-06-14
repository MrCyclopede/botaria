import pyautogui
import time
from pynput.mouse import Button, Controller
mouse = Controller()

def hold_key(key, hold_time):
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)
    pyautogui.keyUp(key)

time.sleep(7)
for i in range(10):
    mouse.press(Button.left)
    time.sleep(0.01)
    mouse.release(Button.left)
    hold_key('a', 0.22)