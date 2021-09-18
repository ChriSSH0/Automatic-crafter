import pyautogui
import time
import pynput
import keyboard
import random
from pynput.mouse import Button, Controller
mouse = Controller()
print("Press 'q' to confirm Synthetize button's location")
while True:
    if keyboard.read_key() == "q":
            SynthetizeX, SynthetizeY = pyautogui.position()
            break
print("Press 'e' to confirm Macro button's location")
while True:
    if keyboard.read_key() == "e":
            MacroX, MacroY = pyautogui.position()
            break
time.sleep(5)
i = 0
while True:
    try:
        i = i+1
        print("Attempting crafting number " , i)
        pyautogui.click(x=SynthetizeX, y=SynthetizeY)
        mouse.press(Button.left)
        mouse.release(Button.left)
        tempo = random.randint(3, 10)
        time.sleep(tempo)
        pyautogui.click(x=MacroX, y=MacroY)
        mouse.press(Button.left)
        mouse.release(Button.left)
        tempo = random.randint(30, 60)
        time.sleep(tempo)
    except:
        pass
