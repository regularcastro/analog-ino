from pynput import keyboard
from pynput.keyboard import Controller
import keyboard as kb
import sys
import winsound as s
import time as t

s.Beep(700, 100)
s.Beep(1100, 300)

k = Controller()
pressed = False

def log ():
    log = t.strftime("%D - %H:%M:%S | ")
    return str(log)
    
def register_sound():
    s.Beep(700, 40)
    
def value1():
    print(log(),'Medir')
    register_sound()
def value2():
    print(log(),'Tarar')
    register_sound()
def value3():
    print(log(),'Zerar')
    register_sound()

def value4():
    print(log(),'Sair')
    s.Beep(1100, 100)
    s.Beep(700, 300)
    sys.exit()
    
def press(key):
    global pressed
    if kb.is_pressed("ctrl+1"):
        
        value1()  
        pressed = True
    if kb.is_pressed("ctrl+2"):
        
        value2()
        pressed = True
    if kb.is_pressed("ctrl+3"):
        
        value3()
        pressed = True
    if kb.is_pressed("ctrl+4"):
        
        value4()
        pressed = True

with keyboard.Listener(on_press=press) as listener: 
    listener.join()

#
