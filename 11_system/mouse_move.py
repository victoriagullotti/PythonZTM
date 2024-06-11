import pyautogui
import time
import random

for i in range(1000):
    x = random.randint(1, 1000)
    y = random.randint(1, 1000)
    pyautogui.moveTo(x, y, duration=5)
    time.sleep(1000)
