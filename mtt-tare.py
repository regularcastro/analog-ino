import serial
from pynput.keyboard import Key, Controller

ser = serial.Serial(
    port=f"COM{4}",
    baudrate=9600,
    parity=serial.PARITY_EVEN,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.SEVENBITS,
    timeout=0.5,
    rtscts=False
    )
ser.close()
ser.open()

def zero():
    (ser.write(b'T\r\n')) ## recomendação: ler comandos de leitura para balanças (S: Envia leitura estável de peso atual)

zero()
ser.close()

#print(data) ## descomente a linha para verificar o retorno da função