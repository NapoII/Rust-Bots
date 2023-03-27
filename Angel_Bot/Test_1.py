################################################################################################################################
#Test_1
from Imports import*
import keyboard
#config_dir = file_path +"/config.ini

hotkey = pyautogui.prompt(text='HOTKEY für abfrage Zeitraum bestimmen.', title=' X und Y Coredinate der Maus bestimmen' , default='p')

while True:
    if keyboard.is_pressed(hotkey):
        Slot_key = 2
        pyautogui.press(str(Slot_key))


