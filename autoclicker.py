from pynput.mouse import Button, Controller
from pynput import keyboard

def on_press(key):
    if key == toogle_key:
        print("'F6' pressed")
        return False

# START
__author__ = "Under3nder"
print(f"Autoclicker by {__author__}")

mouse = Controller()

frequency = 10  # clicks per second
toogle_key = keyboard.Key.f6  # key to press to start/stop clicking

RETARD = 0.045 # instruction retard

print("To start the autoclicker press 'F6'")
with keyboard.Listener(on_release=on_press) as listener:
    listener.join()

print(f"### START CLICKING ###")
run = True
while run:
    mouse.click(Button.left, 1)
    with keyboard.Events() as events:
        event = events.get(1/frequency - RETARD)
        try:
            if event.key == toogle_key:
                print("'F6' pressed")
                run = False
        except AttributeError:
            pass
    
print("### FINISH CLICKING ###")
