from gpiozero import LED
from signal import pause

led = LED(27)
# LED blinks: 1s ON, 1s OFF
led.blink(on_time=1, off_time=1)

pause()  # Keep the program running