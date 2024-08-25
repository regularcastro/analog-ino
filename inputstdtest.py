from pynput import keyboard
from pynput.keyboard import Controller
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
    s.Beep(700, 40)
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

def press(key): 
    global pressed
    if not pressed and key == keyboard.Key.f2:
        #print('%sp' % key) 
        pressed = True
    if not pressed and key == keyboard.Key.f3:
        #print('%sp' % key) 
        pressed = True
    if not pressed and key == keyboard.Key.f4:
        #print('%sp' % key) 
        pressed = True

def release(key):
    global pressed
    if key == keyboard.Key.f2:
        value1()
        pressed = False # key is released
    if key == keyboard.Key.f3:
        #print('%sr' %key)
        value2()
        pressed = False # key is released
    if key == keyboard.Key.f4:
        #print('%sr' %key) 
        value3()  
        pressed = False # key is released
    if key == keyboard.Key.f6:
        print(log(),'Sair')
        s.Beep(1100, 100)
        s.Beep(700, 300)
        sys.exit()

with keyboard.Listener( on_press=press, on_release=release) as listener: 
    listener.join()

#