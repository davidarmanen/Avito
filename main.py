from pynput.keyboard import Key, Listener
from pynput.keyboard import KeyCode
import pyautogui

def main():
    

def on_press(key):
    if KeyCode(vk=86):
        main()

def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()