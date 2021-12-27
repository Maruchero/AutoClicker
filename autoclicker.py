# Import Libraries
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep


# Functions
def on_press(key):
    if key == toggle_key:
        return False


def set_toggle_key(key):
    global toggle_key
    toggle_key = key
    return False


# Globals
frequency = 10  # clicks per second
toggle_key = keyboard.Key.f6  # key to press to start/stop clicking

# START
__author__ = "Under3nder"
print(f"Autoclicker by {__author__}")

change_mode = input(f"The toggle key is set to '{toggle_key}'. Do you want to change it?[y/n] ")
while change_mode != 'y' and change_mode != 'n':
    change_mode = input(f"The toggle key is set to '{toggle_key}'. Do you want to change it?[y/n] ")

if change_mode == 'y':
    sleep(0.6)
    print("Press the key you want to set...")
    with keyboard.Listener(on_release=set_toggle_key) as _listener:
        _listener.join()
    print(f"\nThe key is now set to {toggle_key}")

mouse = Controller()

RETARD = 0.045  # instruction retard

print(f"\n### To start the autoclicker press '{toggle_key}'")
with keyboard.Listener(on_release=on_press) as listener:
    listener.join()

print(f"### START CLICKING ###")
run = True
while run:
    mouse.click(Button.left, 1)
    with keyboard.Events() as events:
        event = events.get(1/frequency - RETARD)
        try:
            if event.key == toggle_key:
                run = False
            elif event.key == keyboard.Key.esc:
                quit()
        except AttributeError:
            pass
    
print("### FINISH CLICKING ###")
