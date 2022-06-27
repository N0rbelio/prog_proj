### Modelos desenho portas logicas
### Para circuito_gui.py
###
from tkinter import Canvas

def gates():
    Cop = Canvas(bg ='white', height=340, width=590)
    Cop.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    ##AND Gate
    Cop.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3) 
    ##OR Gate
    Cop.create_arc(180, 150, 120, 133, start=0, extent=220, fill="green")
    #NOT Gate
    #Na seguinte estrutura [x1, y1, x2, y2 ...]
    tripontos = [150, 100, 150, 120, 180, 110]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    circpontos = [175,105,185,115]
    Cop.create_oval(circpontos, outline='black', fill='white', width=3)
    Cop.create_line(186,110,200,110, fill="green", width=3)
    Cop.create_line(135,110,149,110, fill="green", width=3)