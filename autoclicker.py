# Import Libraries
from pynput.mouse import Button, Controller
from pynput import keyboard
from time import sleep


# Functions
def on_press(key):
    global click, run
    if str(key) == toggle_key:
        click = True
        return False
    elif key == keyboard.Key.esc:
        run = False
        return False


def set_toggle_key(key):
    global toggle_key
    toggle_key = key
    return False


# Globals
__author__ = "Under3nder"

mouse = Controller()
RETARD = 0.01  # instruction retard

# Read Config
# configuration = {"toggle_key": keyboard.Key.f6, "cps": 10}
try:
    config = open("config.txt", 'r')

    toggle_key = config.readline()[:-1]
    cps = int(config.readline())

    config.close()
except FileNotFoundError:
    toggle_key = keyboard.Key.f6
    cps = 10

# START
print(f"Auto clicker by {__author__}")

# Change toggle key
print("#########################")
change_mode = input(f"The toggle key is set to '{toggle_key}'. Do you want to change it?[y/n] ")
while change_mode != 'y' and change_mode != 'n':
    change_mode = input(f"The toggle key is set to '{toggle_key}'. Do you want to change it?[y/n] ")

if change_mode == 'y':
    sleep(0.3)
    print("Press the key you want to set...")
    with keyboard.Listener(on_release=set_toggle_key) as _listener:
        _listener.join()
    print(f"\nThe key is now set to {toggle_key}")

# Set clicks per second
print("\n#########################")
_cps = input(f"Enter CPS(actually is {cps}): ")
try:
    cps = int(_cps)
except ValueError:
    pass
print(f"CPS = {cps}")

# Write Config
config = open("config.txt", 'w')
config.write(str(toggle_key) + '\n')
config.write(str(cps))
config.close()

# Clicking
print("\n#########################")
print(f"To start the auto clicker press '{toggle_key}'")
print("Press 'Key.esc' to close auto clicker")
run = True
click = True
while run:
    with keyboard.Listener(on_release=on_press) as listener:
        listener.join()
    if not run:
        continue

    print("Start clicking")
    while click:
        # click
        mouse.click(Button.left, 1)
        # check stop keys
        with keyboard.Events() as events:
            event = events.get(1 / cps - RETARD)
            try:
                if str(event.key) == toggle_key:
                    click = False
                elif event.key == keyboard.Key.esc:
                    click = False
                    run = False
            except AttributeError:
                pass
    print("Finish clicking\n")
    sleep(0.3)
