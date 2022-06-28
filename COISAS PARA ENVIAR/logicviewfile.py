### LogicView modelo desenho portas logicas
### Para circuito_gui.py
###
from tkinter import Canvas
from tkinter import Label

def gates():
    Cop = Canvas(bg ='white', height=340, width=590)
    Cop.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    
    ##AND Gate
    posAND1 = -70
    Cop.create_arc(130+posAND1, 150+posAND1, 180+posAND1, 190+posAND1, start=270, extent=180, fill="white", width=3)
    Cop.create_rectangle(135+posAND1, 150+posAND1, 155+posAND1, 190+posAND1, fill='white', outline='black', width=3)
    Cop.create_line(155+posAND1, 152+posAND1, 155+posAND1, 189+posAND1, fill="white", width=3)
    #saida linhas
    Cop.create_line(181+posAND1,170+posAND1,200+posAND1,170+posAND1, fill="green", width=3)
    #entrada linhas
    Cop.create_line(115+posAND1,160+posAND1,134+posAND1,160+posAND1, fill="green", width=3)
    Cop.create_line(115+posAND1,180+posAND1,134+posAND1,180+posAND1, fill="green", width=3)

    ##OR Gate
    #Cop.create_rectangle(10, 10, 70, 70, fill='white', outline='blue', width=3) 
    posOR1 = -85
    tripontos = [150+posOR1, 250+posOR1, 155+posOR1, 275+posOR1, 150+posOR1, 300+posOR1, 180+posOR1, 297+posOR1, 190+posOR1, 294+posOR1, 210+posOR1, 275+posOR1, 192+posOR1, 260+posOR1, 180+posOR1, 255+posOR1]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    #saida linha
    Cop.create_line(210+posOR1, 275+posOR1, 229+posOR1, 275+posOR1, fill="green", width=3)
    #entrada linhas
    Cop.create_line(132+posOR1, 265+posOR1, 152+posOR1, 265+posOR1, fill="green", width=3)
    Cop.create_line(132+posOR1, 285+posOR1, 152+posOR1, 285+posOR1, fill="green", width=3)

    #NOT Gate
    #Na seguinte estrutura [x1, y1, x2, y2 ...]
    posNOT1 = -10
    tripontos = [150+posNOT1, 100+posNOT1, 150+posNOT1, 120+posNOT1, 180+posNOT1, 110+posNOT1]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    circpontos = [175+posNOT1,105+posNOT1,185+posNOT1,115+posNOT1]
    Cop.create_oval(circpontos, outline='black', fill='white', width=3)
    Cop.create_line(186+posNOT1,110+posNOT1,200+posNOT1,110+posNOT1, fill="green", width=3)
    Cop.create_line(135+posNOT1,110+posNOT1,149+posNOT1,110+posNOT1, fill="green", width=3)

    ##AND 2 Gate
    posAND1 = +30
    Cop.create_arc(130+posAND1, 150+posAND1, 180+posAND1, 190+posAND1, start=270, extent=180, fill="white", width=3)
    Cop.create_rectangle(135+posAND1, 150+posAND1, 155+posAND1, 190+posAND1, fill='white', outline='black', width=3)
    Cop.create_line(155+posAND1, 152+posAND1, 155+posAND1, 189+posAND1, fill="white", width=3)
    #saida linhas
    Cop.create_line(181+posAND1,170+posAND1,200+posAND1,170+posAND1, fill="green", width=3)
    #entrada linhas
    Cop.create_line(115+posAND1,160+posAND1,134+posAND1,160+posAND1, fill="green", width=3)
    Cop.create_line(115+posAND1,180+posAND1,134+posAND1,180+posAND1, fill="green", width=3)

    ##OR 2 Gate
    posOR1 = -120
    tripontos = [380+posOR1, 250+posOR1, 385+posOR1, 275+posOR1, 380+posOR1, 300+posOR1, 410+posOR1, 297+posOR1, 420+posOR1, 294+posOR1, 440+posOR1, 275+posOR1, 422+posOR1, 260+posOR1, 410+posOR1, 255+posOR1]
    Cop.create_polygon(tripontos, outline='black', fill='white', width=3)
    #saida linhas
    Cop.create_line(440+posOR1, 275+posOR1, 459+posOR1, 275+posOR1, fill="green", width=3)
    #entrada linhas
    Cop.create_line(382+posOR1, 265+posOR1, 362+posOR1, 265+posOR1, fill="green", width=3)
    Cop.create_line(382+posOR1, 285+posOR1, 362+posOR1, 285+posOR1, fill="green", width=3)

    #Ligação ao OR 2 Gate
    Cop.create_line(200+posNOT1,110+posNOT1,362+posOR1, 265+posOR1, fill="green", width=3)
    Cop.create_line(200+posAND1,170+posAND1,362+posOR1, 285+posOR1, fill="green", width=3)

    ##LABELS
    label_info = Label(Cop, text = "T", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=70)
    label_info = Label(Cop, text = "1", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=50)
    label_info = Label(Cop, text = "2", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=80)
    label_info = Label(Cop, text = "F", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=100)
    label_info = Label(Cop, text = "F", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=120, y=70)
    label_info = Label(Cop, text = "T", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=180, y=70)
    label_info = Label(Cop, text = "F", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=215, y=170)
    label_info = Label(Cop, text = "T", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=170)
    label_info = Label(Cop, text = "F", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=20, y=190)
    label_info = Label(Cop, text = "F", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=130, y=200)
    label_info = Label(Cop, text = "T", font=("Arial Rounded MT Bold", 10))
    label_info.place(x=320, y=135)