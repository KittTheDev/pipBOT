import pydirectinput
import time
import random
import threading
import tkinter.font as font
import tkinter as tk
from tkinter import *

stop_loop = False

#### ALL DIFFERENT BOT ####
"""Code different type of bot"""

def pipAFK():
    global stop_loop
    while not stop_loop:
        time.sleep(random.randint(5, 15))
        pydirectinput.press('Tab')

def FrogAFK():
    global stop_loop
    while not stop_loop:
        time.sleep(random.randint(5, 15))
        pydirectinput.press('Space')


### STARTING BOT FUNCTIONS (for Tkinter) ###
'''Use the bot in a different Thread (preventing crash)'''
def start_FrogAFK():
    global stop_loop
    stop_loop = False
    threading.Thread(target=FrogAFK).start()

def start_pipAFK():
    global stop_loop
    stop_loop = False
    threading.Thread(target=pipAFK).start()

# STOP BOTTING FUNCTIONS #
def stop_loop_function():
    global stop_loop
    stop_loop = True


## APP FALLOUT pipBOT +- ##
root = Tk()
root.geometry('404x404')
root.title('pipBOT')
root['bg'] = 'black'
root.resizable(height=False, width=False)
root.iconphoto(False, tk.PhotoImage(file=f'asset\icon.png'))

myFont = font.Font(family='Classic Console Neue')

bg = PhotoImage(file =r'asset\bg.png')
label1 = Label(image = bg)
label1.place(x = 0, y = 0)

# FrogAFK BUTTON
FrogAFKButton = Button(root, text="START", font=myFont, bg='#e5880d', fg='#42270e', command=start_FrogAFK)
FrogAFKButton.place(x='280', y='145')

# pipAFK BUTTON
pipAFKButton = Button(root, text="START", font=myFont, bg='#e5880d', fg='#42270e', command=start_pipAFK)
pipAFKButton.place(x='280', y='238')

# Stop Botting BUTTON
stopButton = Button(root, text="STOP", font=myFont, bg='red', fg='white', command=stop_loop_function)
stopButton.place(x='182', y='350')

root.mainloop()

# python -m nuitka --disable-console pipbot.py (for exe with Nuitka)