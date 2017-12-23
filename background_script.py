#!/usr/bin/sudo python
import keyboard
import pyperclip
from time import sleep
from pyautogui import typewrite
from orderedset import OrderedSet


clipboard_set = OrderedSet()
clipboard = []
iterator = None
curr_location = 0

def copy_pressed():
    global curr_location
    global clipboard
    global clipboard_set
    print "copy"
    sleep(0.2)
    print pyperclip.paste()
    clipboard_set.add(pyperclip.paste())
    clipboard = list(clipboard_set)
    curr_location = len(clipboard)-1
    print clipboard



def down_pressed():
    global curr_location
    curr_location = len(clipboard)-1




def left_pressed():
    global curr_location
    sleep(0.2)
    print "LEFT"
    curr_location -= 1 if curr_location -1 !=-1 else 0
    typewrite(clipboard[curr_location])


def right_pressed():
    global curr_location
    print "RIGHT"
    sleep(0.2)
    curr_location+= 1 if curr_location+1!=len(clipboard) else 0
    typewrite(clipboard[curr_location])



keyboard.register_hotkey('ctrl+c',copy_pressed)
keyboard.register_hotkey('alt+shift+left',left_pressed)
keyboard.register_hotkey('alt+shift+right',right_pressed)
keyboard.register_hotkey('alt+shift+down',down_pressed)

keyboard.wait()
