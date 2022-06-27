### Modelos desenho portas logicas
### Para circuito_gui.py
###
from copy import copy
from tkinter import Canvas

def gates():
    C = Canvas(bg ='white', height=340, width=590)
    C.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    AND = C.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3)
    OR = C.create_rectangle(20, 20, 50, 70, fill='white', outline='red', width=3)
    NOT = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="green")
    tags='calculate'