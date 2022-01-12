import tkinter
from tkinter.messagebox import askokcancel, showinfo
import sys

def message(sentence):
    tkinter.Tk().withdraw()
    answer = askokcancel(title='Confirmar', message=sentence, icon=None)
    if not answer:
        sys.exit()
    return None

def end_message(title, sentence):
    tkinter.Tk().withdraw()
    showinfo(title=title, message=sentence)
    return None