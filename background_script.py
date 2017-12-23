#!/usr/bin/sudo python
import keyboard
import pyperclip
from time import sleep
from pyautogui import typewrite


clipboard = set()
clipboard = []
iterator = None
curr_location = 0

def copy_pressed():
    global curr_location
    clipboard.append(pyperclip.paste())
    curr_location = len(clipboard)-1
    print curr_location
    print clipboard


def down_pressed():
    global curr_location
    global clipboard
    curr_location = len(curr_location)-1


def left_pressed():
    global curr_location
    global clipboard
    sleep(0.1)
    print "LEFT"
    curr_location -= 1 if curr_location -1 !=-1 else 0
    typewrite(clipboard[curr_location])


def right_pressed():
    global keyboard
    global curr_location
    global clipboard
    print "RIGHT"
    sleep(0.1)
    curr_location+= 1 if curr_location+1!=len(clipboard) else 0
    typewrite(clipboard[curr_location])



keyboard.register_hotkey('ctrl+c',copy_pressed)
keyboard.register_hotkey('alt+shift+left',left_pressed)
keyboard.register_hotkey('alt+shift+right',right_pressed)
keyboard.register_hotkey('alt+shift+down',down_pressed)

keyboard.wait()