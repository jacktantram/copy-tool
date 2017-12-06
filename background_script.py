import pyxhook
import time
import pyperclip

clipboard = []

control_pressed = False
alt_pressed = False
shift_pressed = False
current_position = 0
# This function is called every time a key is presssed
def kbevent(event):
    global control_pressed
    global  clipboard
    global alt_pressed
    global shift_pressed
    global current_position
    # print key info
    print  event.Ascii

    # If the ascii value matches spacebar, terminate the while loop
    if event.Ascii == 227 or control_pressed:
        control_pressed = True
        if event.Ascii == 99:
            print "Ctrl C"
            clipboard.append(pyperclip.paste())
            current_position = len(clipboard)-1
    else:
        control_pressed = False

    if event.Ascii == 225 or shift_pressed:
        shift_pressed = True
        if event.Ascii == 233 or alt_pressed:
            alt_pressed = True

            if event.Ascii == 81:
                print clipboard[current_position]
                current_position-=1


        else:
            alt_pressed = False

    else:
        shift_pressed = False


# Create hookmanager
hookman = pyxhook.HookManager()
# Define our callback to fire when a key is pressed down
hookman.KeyDown = kbevent
# Hook the keyboard
hookman.HookKeyboard()
# Start our listener
hookman.start()

# Create a loop to keep the application running
running = True
while running:
    time.sleep(0.1)

# Close the listener when we are done
hookman.cancel()