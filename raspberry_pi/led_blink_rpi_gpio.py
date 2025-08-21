import RPi.GPIO as GPIO
import time

# Use BCM GPIO numbering
GPIO.setmode(GPIO.BCM)

LED_PIN = 27  # GPIO17 (Pin 11 on the board)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        time.sleep(1)                    # Wait 1 second
        print("LED ON")
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED OFF
        time.sleep(1)                    # Wait 1 second
        print("LED OFF")
except KeyboardInterrupt:
    print("Stopped by User")
finally:
    GPIO.cleanup()  # Reset GPIO settings when program exits