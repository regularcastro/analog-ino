import serial
import time as t
import sys as s
import serial.tools.list_ports as st
 
def mimir():
    
    
    print("----------\nEOF")
    #t.sleep(1)
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
        baudrate=9600,
        parity=serial.PARITY_EVEN,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.SEVENBITS,
        timeout=0.5,
        rtscts=False
        )
    ser.close()
    print(f"COM {com} is available")
    #t.sleep(3)
 
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


def sendexpectserialdata():
    msg = 'SI'
    print(f"The message to be sent is: {msg}")
    #msg = input()
    #data = msg.encode().hex()
    data = msg
    if data:
        (ser.write(b'S\r\n'))
        #print((ser.write(data)).decode('ascii'))
        print("data sent!\n---data received:")
        buffer=""
        while True:
            read = ser.read(1)
            if read == b"\n":
                return buffer
            else:
                buffer +=read.decode('utf-8')
                #print(buffer)
                #measurement.append(buffer)
                
        
#print(sendexpectserialdata())
print(str(sendexpectserialdata()).strip('S S'))