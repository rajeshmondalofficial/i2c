import smbus2

# Define I2C parameters
I2C_BUS = 1  # Change to 0 if using older Raspberry Pi models
LM75A_ADDRESS = 0x48  # Default I2C address of LM75A
TEMP_REGISTER = 0x01  # Temperature register

def read_lm75a_temp():
    bus = smbus2.SMBus(I2C_BUS)
    
    try:
        # Read two bytes from the temperature register
        raw_data = bus.read_word_data(LM75A_ADDRESS, TEMP_REGISTER)
        
        # Convert to correct byte order (LM75A sends MSB first)
        raw_data = ((raw_data << 8) & 0xFF00) | (raw_data >> 8)
        
        # Extract temperature value (11-bit resolution, two's complement)
        temp = raw_data >> 5  # Shift right to remove unused bits
        if temp & 0x0400:  # Check if negative (11th bit is sign)
            temp -= 8192  # Convert to negative value (two's complement)
        
        temperature_celsius = temp * 0.125  # Each step is 0.125°C
        
        return raw_data
    except OSError:
        print("Failed to read from LM75A sensor")
        return None
    finally:
        bus.close()

# Read temperature and print
temperature = read_lm75a_temp()
if temperature is not None:
    print(f"Temperature: {temperature:.2f} °C")


# import smbus2
# import time

# SLAVE_ADDR = 0x08  # Must match Pico's address
# bus = smbus2.SMBus(1)

# while True:
#     message = "Hi Pico"
#     data = [ord(c) for c in message]  # Convert string to ASCII bytes
#     bus.write_i2c_block_data(SLAVE_ADDR, 0, data)
#     print("Sent:", message)
#     time.sleep(1)
