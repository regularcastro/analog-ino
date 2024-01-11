import serial
import time as t
import sys as s
import serial.tools.list_ports as st


def list_serial_ports():
    ports = st.comports()
    if not ports:
        print("no serial ports found")
        t.sleep(3)
        s.exit()
    else:
        item = 1
        print("existing serial ports:\n")
        for port in ports:
            print(f'ITEM {len(ports)}')
            print(f"device:  {port.device}")
            print(f"description: {port.description}")
            print(f"hwid: {port.hwid}")
            print(f"vid: {port.vid}")
            print(f"serial_number: {port.serial_number}")
            print(f"location: {port.location}")
            print(f"product: {port.product}")
            print(f"interface: {port.interface}\n")
            item+=1

list_serial_ports()

com = input("type a COM to perform a serial read: ")

try:
    ser = serial.Serial(
        port=f"COM{com}",
        baudrate=9600)
    ser.close()
    print(f"COM {com} is available")
    t.sleep(3)

except serial.SerialException as e:
    if "FileNotFoundError" in str(e):
        print(f"the specified COM{com} port does not exist")
        t.sleep(3)
        s.exit()
    else:
        print(f"an error occurred: {e}")
        t.sleep(3)
        s.exit()
except Exception as e:
    print(f"an unexpected error occurred: {e}")
    t.sleep(3)
    s.exit()

ser.open()
def serialdata():
    print('press crtl + C in order to exit.\n')
    t.sleep(2)
    time = [3,2,1]
    for i in time:
        print(f'processing in {i}')
        i+=-1
        t.sleep(1)
    
    try:
        while True:
            data = ser.readline().decode('utf-8')
            print(data)
    except KeyboardInterrupt:
        print('keyboard interrupt detected')
        t.sleep(3)
        s.exit()

serialdata()