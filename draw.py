### Modelos desenho portas logicas
### Para circuito_gui.py
###
from tkinter import Canvas
from tkinter import *

Cop = Tk()
Cop = Canvas(bg ='white', height=340, width=590)
Cop.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')


##################
line_id = None
line_points = []
line_options = {}

def draw_line(event):
    global line_id
    line_points.extend((event.x, event.y))
    if line_id is not None:
        Cop.delete(line_id)
    line_id = Cop.create_line(line_points, **line_options)


def set_start(event):
    line_points.extend((event.x, event.y))


def end_line(event=None):
    global line_id
    line_points.clear()
    line_id = None

###########################
##OR Gate
tripontos = [150, 100, 150, 120, 180, 110]
Cop.create_polygon(tripontos, outline='black', fill='white', width=3)

#NOT Gate
#Na seguinte estrutura [x1, y1, x2, y2 ...]
tripontos = [150, 100, 150, 120, 180, 110]
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

#Função move do rato
Cop.bind('<Button-1>', set_start)
Cop.bind('<B1-Motion>', draw_line)
Cop.bind('<ButtonRelease-1>', end_line)

Cop.mainloop()