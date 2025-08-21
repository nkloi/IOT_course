import serial
import time

# Open the serial port
ser = serial.Serial(
    port="/dev/ttyS0",   # UART device on Raspberry Pi (may be /dev/ttyAMA0 or /dev/ttyS0 depending on model)
    baudrate=9600,         # Communication speed (bits per second)
    timeout=1              # Timeout for reading (in seconds)
)
print("Serial port opened")
time.sleep(2)  # Give some time for the serial port to initialize
print("Serial port initialized")
try:
    while True:
        # Send data through UART
        ser.write(b"Hello UART!\n")
        print("Sent: Hello UART!")

        # Read data from UART (works if TX and RX are connected in loopback)
        data = ser.readline().decode("utf-8").strip()
        if data:
            print("Received:", data)

        time.sleep(1)  # Small delay before sending again
except KeyboardInterrupt:
    # Stop the program when user presses Ctrl+C
    print("Stopped by User")
finally:
    # Always close the serial port when exiting
    ser.close()