from pynput import keyboard
from pynput.keyboard import Controller
import sys

pressed = False
k = Controller()
def on_press(key): 
    global pressed
    if not pressed and key == keyboard.Key.f1: # only if key is not held
        print('Key %s pressed' % key) 
        pressed = True # key is held
    if not pressed and key == keyboard.Key.f2: # only if key is not held
        print('Key %s pressed' % key) 
        pressed = True # key is held
    if not pressed and key == keyboard.Key.f3: # only if key is not held
        print('Key %s pressed' % key) 
        pressed = True # key is held

def on_release(key):
    global pressed
    if key == keyboard.Key.f1:
        print('Key %s released' %key) 
        pressed = False # key is released
    if key == keyboard.Key.f2:
        print('Key %s released' %key) 
        pressed = False # key is released
    if key == keyboard.Key.f3:
        print('Key %s released' %key) 
        pressed = False # key is released
    if key == keyboard.Key.f4:
        sys.exit()

with keyboard.Listener( on_press=on_press, on_release=on_release) as listener: 
    listener.join()

#