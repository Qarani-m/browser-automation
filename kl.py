import time
import pyautogui as pag
from pynput.keyboard import Key,Controller

keyboard = Controller()

pag.FAILSAFE =False

print(pag.position())