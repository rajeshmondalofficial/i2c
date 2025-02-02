import smbus2

def detect_i2c_devices(bus_num=1):
    bus = smbus2.SMBus(bus_num)
    devices = []
    
    for address in range(0x03, 0x78):  # Valid I2C addresses
        try:
            bus.read_byte(address)  # Try to read a byte
            devices.append(hex(address))
        except OSError:
            pass  # Ignore errors (device not found)
    
    bus.close()
    return devices

if __name__ == "__main__":
    detected_devices = detect_i2c_devices()
    if detected_devices:
        print("I2C devices found at addresses:", detected_devices)
    else:
        print("No I2C devices detected.")
