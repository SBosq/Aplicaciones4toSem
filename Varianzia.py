import tkinter as tk
import numpy as np
import math
from tkinter import *
from tkinter.messagebox import *

main = Tk()
main.geometry('525x190')
main.resizable(False, False)
main.title('Variancia')
main.configure(background='PeachPuff')


blank0 = Entry(main)
blank1 = Entry(main)
blank2 = Entry(main)
blank3 = Entry(main)
blank4 = Entry(main)
blank5 = Entry(main)
blank6 = Entry(main)
blank7 = Entry(main)
blank8 = Entry(main)
blank9 = Entry(main)
blank10 = Entry(main)
blank11 = Entry(main)
blank12 = Entry(main)
blank13 = Entry(main)

def getinter():
    A=np.zeros(12)
    A[:]=np.nan
    counter=0
    #Ans1=0
    
    if blank0.get()!='null' or blank0.get()!=0:
        A[0]=blank0.get()
        Ans1=A[0]+0
        Ans4=math.pow(A[0],2)+0
        counter+=1
    if blank1.get()!='null' or blank1.get()!=0:
        A[1]=blank1.get()
        Ans1=Ans1+A[1]+0
        Ans4=math.pow(A[1],2)+Ans4
        counter+=1
    if blank2.get()!='null' or blank2.get()!=0:
        A[2]=blank2.get()
        Ans1=Ans1+A[2]+0
        Ans4=math.pow(A[2],2)+Ans4
        counter+=1
    if blank3.get()!='null' or blank3.get()!=0:
        A[3]=blank3.get()
        Ans1=Ans1+A[3]+0
        Ans4=math.pow(A[3],2)+Ans4
        counter+=1
    if blank4.get()!='null' or blank4.get()!=0:
        A[4]=blank4.get()
        Ans1=Ans1+A[4]+0
        Ans4=math.pow(A[4],2)+Ans4
        counter+=1
    if blank5.get()!='null' or blank5.get()!=0:
        A[5]=blank5.get()
        Ans1=Ans1+A[5]+0
        Ans4=math.pow(A[5],2)+Ans4
        counter+=1
    if blank6.get()!='null' or blank6.get()!=0:
        A[6]=blank6.get()
        Ans1=Ans1+A[6]+0
        Ans4=math.pow(A[6],2)+Ans4
        counter+=1
    if blank7.get()!='null' or blank7.get()!=0:
        A[7]=blank7.get()
        Ans1=Ans1+A[7]+0
        Ans4=math.pow(A[7],2)+Ans4
        counter+=1
    if blank8.get()!='null' or blank8.get()!=0:
        A[8]=blank8.get()
        Ans1=Ans1+A[8]+0
        Ans4=math.pow(A[8],2)+Ans4
        counter+=1
    if blank9.get()!='null' or blank9.get()!=0:
        A[9]=blank9.get()
        Ans1=Ans1+A[9]+0
        Ans4=math.pow(A[9],2)+Ans4
        counter+=1
    if blank10.get()!='null' or blank10.get()!=0:
        A[10]=blank10.get()
        Ans1=Ans1+A[10]+0
        Ans4=math.pow(A[10],2)+Ans4
        counter+=1
    if blank11.get()!='null' or blank11.get()!=0:
        A[11]=blank11.get()
        Ans1=Ans1+A[11]+0
        Ans4=math.pow(A[11],2)+Ans4
        counter+=1
    
    Ans2=math.pow(Ans1,2)
    Ans3=float(Ans2/counter)
    Ans5=float(Ans4-Ans3)
    Ans6=counter-1
    Ans7=float(Ans5/Ans6) #Variance
    Ans8=float(math.sqrt(Ans7)) #Standard Deviation
    blank12.insert(0,Ans7)
    blank13.insert(0,Ans8)
    
        
blank0.grid(row=0, column=0, pady=(25,0), padx=(12,0)) 
blank1.grid(row=0, column=1, pady=(25,0)) 
blank2.grid(row=0, column=2, pady=(25,0)) 
blank3.grid(row=0, column=3, pady=(25,0)) 

blank4.grid(row=1, column=0, padx=(12,0)) 
blank5.grid(row=1, column=1) 
blank6.grid(row=1, column=2) 
blank7.grid(row=1, column=3)  

blank8.grid(row=2, column=0, padx=(12,0)) 
blank9.grid(row=2, column=1)
blank10.grid(row=2, column=2)
blank11.grid(row=2, column=3)

blank12.grid(row=4, column=1, pady=(15,0))
blank13.grid(row=4, column=3, pady=(15,0))

Label(main, text = "Varianzia: ", font="Times 7", background='PeachPuff').grid(row=4, column=0, pady=(15,0))
Label(main, text = "Desviación Estándar: ", font="Times 7", background='PeachPuff').grid(row=4, column=2, pady=(15,0))

Button(main, text='Calcular!', command=getinter).grid(row=3, column=2, pady=(25,0))

mainloop()
