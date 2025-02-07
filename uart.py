import serial
import time

# Configure the UART port
uart = serial.Serial(
    # Replace with your UART port (e.g., COM3 for Windows)
    port='/dev/ttyAMA0',
    baudrate=9600,        # Set the baud rate
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=1             # Timeout in seconds for reading
)

uart.write("Hello From Pi3")


# try:
#     print("Reading from UART...")
#     while True:
#         if uart.in_waiting > 0:  # Check if data is available
#             data = uart.readline().decode('utf-8').strip()  # Read and decode
#             print(f"Received: {data}")
# except KeyboardInterrupt:
#     print("Exiting...")
# finally:
#     uart.close()
