import smbus2
import time

# I2C bus and device address
I2C_BUS = 1
I2C_SLAVE_ADDR = 0x42  # Must match the Pico's slave address

# Initialize I2C bus
bus = smbus2.SMBus(I2C_BUS)

try:
    while True:
        # Write data to the Pico
        data_to_send = [0x10, 0x20, 0x30]  # Example data
        bus.write_i2c_block_data(I2C_SLAVE_ADDR, 0x00, data_to_send)
        print(f"Sent: {data_to_send}")

        time.sleep(1)

        # Read response from the Pico
        response = bus.read_i2c_block_data(I2C_SLAVE_ADDR, 0x00, 10)  # Read 10 bytes
        print(f"Received: {response}")

        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    bus.close()
