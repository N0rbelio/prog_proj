### Modelos desenho portas logicas
### Para circuito_gui.py
###
from tkinter import *

def gates():
    main = Tk()
    C = Canvas(main, bg="yellow", height=250, width=300)
    AND = C.create_line(108, 120, 320, 40, fill="green") 
    OR = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")
    NOT = C.create_oval(80, 30, 140, 150, fill="blue")
    C.pack()
    mainloop()