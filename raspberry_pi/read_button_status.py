import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set up GPIO18 as input with internal pull-up disabled (since you use external 10kΩ pull-up)
GPIO.setup(18, GPIO.IN)

print("Press the button (CTRL+C to exit)")

try:
    while True:
        # Read button state
        button_state = GPIO.input(18)  # HIGH = not pressed, LOW = pressed
        if button_state == GPIO.LOW:
            print("Button Pressed")
        else:
            print("Button Released")

        time.sleep(0.2)  # Small delay to avoid spamming output

except KeyboardInterrupt:
    print("Exiting...")

finally:
    GPIO.cleanup()