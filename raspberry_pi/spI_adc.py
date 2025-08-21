import spidev
import time

# Create SPI instance
spi = spidev.SpiDev()
spi.open(0, 0)   # Open bus 0, device 0 (CE0)
spi.max_speed_hz = 1350000  # 1.35 MHz

def read_channel(channel):
    # MCP3008 has 8 channels (0-7)
    # Send start bit, single-ended mode, channel (bits packed)
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    # Convert to 10-bit value
    data = ((adc[1] & 3) << 8) | adc[2]
    return data

try:
    while True:
        value = read_channel(0)  # Read channel 0
        voltage = (value * 3.3) / 1023  # Convert to voltage
        print(f"Raw Value: {value}, Voltage: {voltage:.2f}V")
        time.sleep(1)
except KeyboardInterrupt:
    spi.close()
    print("Stopped by User")