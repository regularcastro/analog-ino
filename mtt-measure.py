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

def sendexpectserialdata():
    (ser.write(b'S\r\n')) ## recomendação: ler comandos de leitura para balanças (S: Envia leitura estável de peso atual)
    buffer=""
    while True:
        read = ser.read(1)
        if read == b"g": ## inserido o 'g' como threshold pois não há como usar o .strip para remover o g
            return buffer
        else:
            buffer +=read.decode('utf-8')
            #print(buffer) ## descomente a linha para ver o dado agregado
          
data = str(sendexpectserialdata())
#print(data) ## descomente a linha para verificar o retorno da função

def leitura (data): ## função para cortar letras e espaços
    strip2 = data.strip('S S') ## remoção de 4 caracteres que existem em todos os retornos dos comandos que começam com S

    if 'M' in strip2:  ## remoção de unidade múltiplo, sinal algébrico '+' e inserção de aspa simples para não bugar a cabeça do excel
        strip2 = strip2.strip('M')
    #if '-' in strip2:
    #    strip2 = "'" + strip2 
    if '+' in strip2:
        strip2 = strip2.strip('+')
        
    value = strip2 ## redefinição de variável para remover caracteres não-alfanuméricos
    
    if ' ' in value:
        value = value.strip(' ')
    if '' in value:
        value = value.strip('')
    value = value.replace('.',',') ## finaliza substituindo ponto por vírgula

    #value = int(value)

    keyboard = Controller()
    keyboard.type(value)
    
ser.close()
leitura(data)