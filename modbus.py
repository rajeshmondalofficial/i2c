from pymodbus.client import ModbusSerialClient

import serial.tools.list_ports

# Get a list of all available serial ports
ports = serial.tools.list_ports.comports()

if not ports:
    print("No serial ports found.")
else:
    print("Available serial ports:")
    for port in ports:
        print(f"Port: {port.device} - {port.description}")


# Define Modbus serial details
client = ModbusSerialClient(
    framer='rtu',
    port='COM6',  # Replace with your serial port
    baudrate=9600,
    timeout=1,
    stopbits=1,
    bytesize=8,
    parity='N'
)

client.connect()


# Read 5 coils starting from address 0
response = client.close() # 'unit' is the slave ID
print(response)

# if response.isError():
#     print("Error reading coils:", response)
# else:
#     print("Coil values:", response.bits)

# Close the connection
client.close()
