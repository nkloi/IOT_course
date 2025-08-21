from gpiozero import LED, Button
from signal import pause

led = LED(27)       # LED on GPIO27 (Pin 13)
button = Button(2)  # Button on GPIO2 (Pin 3)

# Link button state directly to LED
button.when_pressed = led.on
button.when_released = led.off

pause()  # Keep program running