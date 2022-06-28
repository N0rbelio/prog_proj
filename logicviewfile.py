### LogicView modelo desenho portas logicas
### Para circuito_gui.py
###
from tkinter import Canvas

def gates():
    Cop = Canvas(bg ='white', height=340, width=590)
    Cop.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    
    ##OR Gate
    #Cop.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3) 
    tripontos = [150, 250, 155, 275, 150, 300, 180, 297, 190, 294, 210, 275, 192, 260, 180, 255]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    Cop.create_line(210, 275, 229, 275, fill="green", width=3)
    #entrada linhas
    Cop.create_line(132, 265, 152, 265, fill="green", width=3)
    Cop.create_line(132, 285, 152, 285, fill="green", width=3)

    #NOT Gate
    #Na seguinte estrutura [x1, y1, x2, y2 ...]
    tripontos = [150, 100, 150, 120, 180, 110,]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    circpontos = [175,105,185,115]
    Cop.create_oval(circpontos, outline='black', fill='white', width=3)
    Cop.create_line(186,110,200,110, fill="green", width=3)
    Cop.create_line(135,110,149,110, fill="green", width=3)
    
    ##AND Gate
    Cop.create_arc(130, 150, 180, 190, start=270, extent=180, fill="white", width=3)
    Cop.create_rectangle(135, 150, 155, 190, fill='white', outline='black', width=3)
    Cop.create_line(155, 152, 155, 189, fill="white", width=3)
    #saida linhas
    Cop.create_line(181,170,200,170, fill="green", width=3)
    #entrada linhas
    Cop.create_line(115,160,134,160, fill="green", width=3)
    Cop.create_line(115,180,134,180, fill="green", width=3)