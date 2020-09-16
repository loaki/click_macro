import time
import sys
import pyautogui
import re
import mouse
import msvcrt
import keyboard

def get_pos(name):
    pos = input('point the '+str(name+1)+' button and press enter')
    return pyautogui.position()

def init_data(d):
    d.max = int(input('enter the number of actions\n'))
    d.sleep = int(input('enter the delay between actions\n'))
    for i in range(0, d.max):
        d.button[i] = pos()
        d.button[i] = get_pos(i)

def action(d):
    for i in range(0, d.max):
        pyautogui.click(d.button[i].x, d.button[i].y)
        time.sleep(d.sleep)
    return 0

class pos():
    x = 0
    y = 0

class data():
    max = 0
    sleep = 0
    button = {}

if __name__ == "__main__":
    d = data()
    init_data(d)
    print('\npress esc to quit')
    ex = 0
    while ex != 1:
        ex = action(d)
        if keyboard.is_pressed('escape') == True:
            print('exiting...')
            ex = 1