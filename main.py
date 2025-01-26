import smbus2
import time

# I2C bus number (e.g., 1 for Raspberry Pi)
I2C_BUS = 1

# Device I2C address
DEVICE_ADDRESS = 0x40  # Replace with your device's address

# Registers or commands (replace with your specific device's registers)
REGISTER_WRITE = 0x01
REGISTER_READ = 0x02

# Initialize the I2C bus
bus = smbus2.SMBus(I2C_BUS)

try:
    # Write a value to the device
    value_to_write = 0x10  # Replace with the value you want to send
    bus.write_byte_data(DEVICE_ADDRESS, REGISTER_WRITE, value_to_write)
    print(f"Sent {value_to_write} to register {REGISTER_WRITE:#02x}")

    # Pause to ensure the device processes the command
    time.sleep(0.1)

    # Read a byte from the device
    read_value = bus.read_byte_data(DEVICE_ADDRESS, REGISTER_READ)
    print(f"Read {read_value} from register {REGISTER_READ:#02x}")

except Exception as e:
    print(f"Error during I2C communication: {e}")

finally:
    # Close the I2C bus
    bus.close()
