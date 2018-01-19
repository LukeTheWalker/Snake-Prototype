from Tkinter import *
from os import system
import string
import sys
from random import *
import pygame
from pygame.locals import *
import time


master=Tk()
master.title("My fuckin' GUI")

entry = []
check_butt = []
label = []
titoli = ["Neuroni in input","Neuroni in output","Lunghezza simulazione","Altezza simulazione","MARGIN","Numero di robot","Numero di sessioni","Grafica","Durata esecuzione","Step","Aumenta le mutazioni","range valori nel codice","Range +/- di mutazioni","Step del range di mutazioni","KEEP","Dimensione robot","Fattore di scala per i motori","Distanza fra le ruote","Angolo apertura sens distanza","Numero di sensori di distanza","Numero sensori di colore","Numero sensori di tocco","Numero di layer"]
boolean_var = 4
n = 23
j = 0

def Close():
  sys.exit()

def donothing ():
  messagebox.showinfo("Work in progress", "Non ancora implementato!")

def thefinalcountdown():
  exec(open("./snake.py").read())

menubar = Menu(master)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Sesssion", command=donothing, accelerator = "Command+N")
filemenu.add_command(label="Open Data file", command=donothing, accelerator = "Command+S")
filemenu.add_command(label="Save in Data file", command=thefinalcountdown, accelerator = "Command+S")
filemenu.add_command(label="Close", command=Close, accelerator = "Command+W")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Close, accelerator = "Command+Q")
menubar.add_cascade(label="File", menu=filemenu)


editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing, accelerator = "Command+Z")
editmenu.add_command(label="Redo", command=donothing, accelerator = "Shift+Command+Z")
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing, accelerator = "Command+X")
editmenu.add_command(label="Copy", command=donothing, accelerator = "Command+C")
editmenu.add_command(label="Paste", command=donothing, accelerator = "Command+V")
editmenu.add_command(label="Select All", command=donothing, accelerator = "Command+A")
menubar.add_cascade(label="Edit", menu=editmenu)

variablesmenu = Menu(menubar, tearoff = 0)
variablesmenu.add_command(label = "Hidden Array", command=donothing, accelerator = "Shift+Command+H")
variablesmenu.add_checkbutton(label = "LTM", onvalue =  1, offvalue = 0, variable  = j)
variablesmenu.add_checkbutton(label = "STS", onvalue = 1, offvalue = 0,variable = j)
variablesmenu.add_checkbutton(label = "EVER_BEST", onvalue = 1, offvalue = 0,variable = j)
variablesmenu.add_checkbutton(label = "MY_CODE", onvalue = 1, offvalue = 0,variable = j)
menubar.add_cascade(label = "Variables", menu = variablesmenu)

master.config(menu=menubar)

finish= Button(master,text= "Start", command =thefinalcountdown)
finish.grid(row=3000,column=3000)

master.mainloop()

       
    
