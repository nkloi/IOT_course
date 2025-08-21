from gpiozero import Button
from signal import pause

# Button on GPIO18 (BCM numbering)
button = Button(18)

# Define what happens when button is pressed
def on_press():
    print("Button pressed!")

# Define what happens when button is released
def on_release():
    print("Button released!")

# Attach events
button.when_pressed = on_press
button.when_released = on_release

print("Waiting for button events... Press CTRL+C to exit.")

# Keep the program running to wait for events
pause()