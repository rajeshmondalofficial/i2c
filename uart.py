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


for i in range(0, 1):
    # Wait for a second before sending the next message
    if i == 0:
        send_data = f"AT+CGSN=30012356956\r\n"
        uart.write(send_data.encode('utf-8'))
    if i == 1:
        send_data = "OK\r\n"
        uart.write(send_data.encode('utf-8'))
    time.sleep(1)
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
