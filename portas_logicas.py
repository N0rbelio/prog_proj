### Modelos desenho portas logicas
### Para circuito_gui.py
###
from copy import copy
from tkinter import Canvas

def gates():
    Cop = Canvas(bg ='white', height=340, width=590)
    Cop.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    AND = Cop.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3) 
    OR = Cop.create_polygon(0, 0, 20, 25, 0, 40, outline='black', fill='white', width=5)
    NOT = Cop.create_arc(180, 150, 120, 133, start=0, extent=220, fill="green")