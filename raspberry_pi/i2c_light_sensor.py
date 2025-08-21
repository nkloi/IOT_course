import smbus
import time

# Create I2C bus
bus = smbus.SMBus(1)   # Use I2C bus 1 on Raspberry Pi

# BH1750 default address
BH1750_ADDR = 0x23

# Modes
CONT_HIGH_RES_MODE = 0x10  # Continuously H-Resolution Mode

def read_light(addr=BH1750_ADDR):
    # Send measurement command
    data = bus.read_i2c_block_data(addr, CONT_HIGH_RES_MODE, 2)
    # Convert the data (lux = raw / 1.2)
    lux = (data[0] << 8 | data[1]) / 1.2
    return lux

try:
    while True:
        light_level = read_light()
        print("Light Level: %.2f lx" % light_level)
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by User")