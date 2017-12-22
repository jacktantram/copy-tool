import keyboard
import pyperclip


clipboard = set()

def on_press(key):
    print key
    if keyboard.is_pressed('ctrl+c'):
       clipboard.add(pyperclip.paste())
       print clipboard
    if keyboard.is_pressed('ctrl+shift+left'):
        print "LEFT"

keyboard.on_press(on_press)

keyboard.wait()