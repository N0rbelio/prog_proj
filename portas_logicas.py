### Modelos desenho portas logicas
### Para circuito_gui.py
from ast import And, Not
from tkinter import *

def gates():
    AND = Canvas.create_line(108, 120, 320, 40, fill="green") 
    OR = Canvas.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")
    NOT = Canvas.create_oval(80, 30, 140, 150, fill="blue")