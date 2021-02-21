from tkinter import *
from tkinter import ttk


def red_checked():
    dict['red'] = not dict['red']


def green_checked():
    dict['green'] = not dict['green']


def blue_checked():
    dict['blue'] = not dict['blue']


def frame_color():
    if dict['red'] and dict['blue'] and dict['green']:
        frame.config(background='white')
    elif dict['red'] and dict['blue']:
        frame.config(bg='white')
    elif dict['red'] and dict['green']:
        frame.config(bg='yellow')
    elif dict['blue'] and dict['green']:
        frame.config(bg='#064e40')
    elif dict['blue']:
        frame.config(bg='blue')
    elif dict['green']:
        frame.config(bg='green')
    elif dict['red']:
        frame.config(bg='red')
    else:
        frame.config(bg='black')


window = Tk()

window.title('RGB')
window.geometry('450x320+30+90')
window.resizable(False, False)

dict = {'red': False, 'green': False, 'blue': False}

checkbuttonR = Checkbutton(window, text='წითელი', command=red_checked)
checkbuttonR.pack()

checkbuttonG = Checkbutton(window, text='მწვანე', command=green_checked)
checkbuttonG.pack()

checkbuttonB = Checkbutton(window, text='ლურჯი', command=blue_checked)
checkbuttonB.pack()

frame = Frame(window, width=300, height=300, relief=GROOVE)
frame.pack(side='bottom')

submitButton = ttk.Button(window, text='SUBMIT', command=frame_color)
submitButton.place(x=370, y=19)

window.mainloop()