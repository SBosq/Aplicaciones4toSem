import tkinter as tk
import math
from fractions import Fraction as frac
from tkinter import *
from tkinter.messagebox import *

def show_answer():
    prob1=float(num1.get())
    prob2=float(num2.get())
    aproxVal1=float(num3.get())
    aproxVal2=float(num4.get())
    val1=float(prob1 * aproxVal1)
    val2=float(prob2 * aproxVal2)
    VE=float(val1 + val2)
    blank.insert(0, VE)    

main = Tk()
main.geometry('400x450')
main.resizable(False, False)
main.title('Probabilidad Basica')
main.configure(background='PeachPuff')

Label(main, text = "Probabilidad de Evento A: ", background='PeachPuff').grid(row=2, pady=(25,0))
Label(main, text = "Valor estimado de Evento A: ", background='PeachPuff').grid(row=5, pady=(25,0))
Label(main, text = "El Valor Esperado es: ", background='PeachPuff').grid(row=8, pady=(50,0))

num1 = Entry(main)
num2 = Entry(main)
num3 = Entry(main)
num4 = Entry(main)
blank = Entry(main)

num1.grid(row=1, column=1, pady=(25,0), padx=(50,0))
num2.grid(row=3, column=1, pady=(20,0), padx=(50,0))

num3.grid(row=4, column=1, pady=(25,0), padx=(50,0))
num4.grid(row=6, column=1, pady=(20,0), padx=(50,0))

blank.grid(row=8, column=1, pady=(50,0), padx=(50,0))

Button(main, text='Calcular!', command=show_answer).grid(row=15, column=0, pady=20)

mainloop()
