import serial
import time as t
import sys as s
import serial.tools.list_ports as st

def mimir():
    print("----------\nEOF")
    t.sleep(1)
    s.exit()

def list_serial_ports():
    ports = st.comports()
    if not ports:
        print("no serial ports found")
        mimir()
    else:
        item = 0
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

com = input("type a COM port number: ")

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
        mimir()
    else:
        print(f"an error occurred: {e}")
        mimir()
except Exception as e:
    print(f"an unexpected error occurred: {e}")
    mimir()

ser.open()
def readserialdata():
    print('press crtl + C to exit.\n')
    t.sleep(2)
    time = [3,2,1]
    for i in time:
        print(f'processing in {i}')
        i+=-1
        t.sleep(0.25)
    
    try:
        while True:
            data = ser.readline().decode('utf-8')
            print(data)
    except KeyboardInterrupt:
        print('keyboard interrupt detected')
        mimir()

def sendserialdata():
    #print(f'data bytes length: {data}')
    try:
        while True:
            msg = input('type a command to send: ')
            data = ser.write(bytearray(msg,'ascii'))
            print("data sent!\n")
            
    except KeyboardInterrupt:
        print('keyboard interrupt detected')
        mimir()
        
def sendexpectserialdata():
    #print(f'data bytes length: {data}')
    try:
        while True:
            msg = input('type a command to send: ')
            data = ser.write(bytearray(msg,'ascii'))
            if data:
                print("data sent!\n")
            data = ser.readline().decode('utf-8')
            ser.close()
            print(f'data read: {data}')
    except KeyboardInterrupt:
        print('keyboard interrupt detected')
        mimir()
    
order = input("press 1 to read data, press 2 to send data, press 3 to send-expect data: ")
if order == '1':
    readserialdata()
elif order == '2':
    #mimir()
    sendserialdata()
elif order == '3':
    sendexpectserialdata()
else:
    mimir()
print("?")