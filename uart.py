import serial
import time

# Configure the UART port
uart = serial.Serial(
    port='/dev/ttyAMA0',  # Replace with your UART port (e.g., COM3 for Windows)
    baudrate=9600,        # Set the baud rate
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1             # Timeout in seconds for reading
)

# Check if the UART port is open
if uart.is_open:
    print("UART port is open")

# Data to send
data_to_send = "Hello, UART!\n"

# Send data
uart.write(data_to_send.encode('utf-8'))  # Encode string to bytes
print(f"Sent: {data_to_send}")

# Wait for a moment
time.sleep(1)

# Close the UART port
uart.close()
print("UART port closed")
