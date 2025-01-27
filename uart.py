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

try:
    print("Reading from UART...")
    while True:
        if uart.in_waiting > 0:  # Check if data is available
            data = uart.readline().decode('utf-8').strip()  # Read and decode
            print(f"Received: {data}")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    uart.close()
