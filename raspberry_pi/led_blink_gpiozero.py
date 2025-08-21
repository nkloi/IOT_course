from gpiozero import LED
from time import sleep

# Create LED object on GPIO17 (Pin 13 on the board)
led = LED(27)

try:
    while True:
        led.on()       # Turn LED ON
        sleep(1)       # Wait 1 second
        led.off()      # Turn LED OFF
        sleep(1)       # Wait 1 second
except KeyboardInterrupt:
    print("Stopped by User")