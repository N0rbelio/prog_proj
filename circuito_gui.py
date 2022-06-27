import webbrowser, os, sys
from tkinter import *
from tkinter.tix import LabelEntry
from tkinter.ttk import *
from tkinter import ttk, filedialog
from portas_logicas import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# Inicializar o GUI tkinter
main = Tk()
# Opçoes janela main
main.geometry('605x405') # Definir tamanho
main.wm_title("Design circuito") # Definir titulo da janela
main.iconbitmap("favicon.ico")
main.resizable(False, False)
#iniciar blank canvas
C = Canvas(main, bg="white", height=340, width=590)
C.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')

#Explorador de ficheiros
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Selecione o ficheiro com as intruções",
                                          filetypes = (("Ficheiros JSON", "*.json*"), ("Ficheiros LogicView", "*.lcvw*"), ("Todos os ficheiros", "*.*")))

#Cria janela sobre
def open_toplevel():
    top = Toplevel()
    top.geometry("450x130")
    top.title("Sobre")
    top.resizable(False, False)
    l2 = Label(top, text = "    Este projeto foi criado por: Andre Oliveira, Daniel Oleksiychuk e Tiago Loureiro")
    l2.grid()

    #url
    url = "https://github.com/N0rbelio/prog_proj"
    #Abrir pagina web
    def openweb():
        webbrowser.open(url,new=1)

    # Creating a photoimage object to use image
    photo = PhotoImage(file = r"GitHub_Logo.png")
    # Resizing image to fit on button
    photoimage = photo.subsample(3, 3)
    # image on LEFT side of button
    Button(top, text = 'Abrir Repositorio', command = openweb, image = photoimage,
                        compound = TOP).grid()

    top.mainloop()

#demo
def demo():
    C = Canvas(main, bg="white", height=340, width=590)
    C.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    AND = C.create_line(108, 120, 320, 40, fill="green") 
    OR = C.create_arc(180, 150, 80, 210, start=0, extent=220, fill="red")
    NOT = C.create_oval(80, 30, 140, 150, fill="blue")

#Reset programa
def erase_design():
     os.execv(sys.executable, ['python'] + sys.argv)

#Apagar canvas
def limpar_canva():
    C = Canvas(main, bg="white", height=340, width=590)
    C.grid(row=1, column=0, pady = 5, padx = 5, sticky ='w')
    C.delete('all')

#Importar de outro demo
def import_demo():
    C.delete('all')
    gates()

#Cria janela ajuda
def ajuda_janela():
    ajuda = Toplevel()
    ajuda.geometry("500x400")
    ajuda.title("Ajuda")
    ajuda.resizable(False, False)

    # Creating a photoimage object to use image
    photo = PhotoImage(file = r"ajuda.png")
    # Resizing image to fit on button
    photoimage = photo.subsample(2, 2)
    # image on LEFT side of button
    Button(ajuda, command = None, image = photoimage,
                        compound = CENTER).grid()

    titlo = Label(ajuda, text = "Ajuda para Design Circuito", font=("Arial", 20))
    titlo.place(relx = 0.55, rely = 0.04, anchor = 'n')

    ll1 = Label(ajuda,text ='O que é o Design Circuito?', font=("Arial Rounded MT Bold", 10))
    ll1.place(x=5, y=80)

    ll1 = Label(ajuda,text ='O Design circuito é programa que permite abrir ficheiros JSON ou LogicView para demonstrar as portas logicas num plano. Os ficheiros podem ser customisados a gosto e manualmente com IDEs populares', wraplength=494)
    # using place method we can set the position of label
    ll1.place(x=5, y=100)

    ajuda.mainloop()

#Texto label debaixo
labeltext = 'Por favor, abra um ficheiro JSON ou LogicView!'
#Texto posição
ll1 = Label(main, text = labeltext)
ll1.place(x=7, y=357)

#Criar botões
btnreset = Button(main, text = 'Reset', command = erase_design)
btnreset.place(x=520, y=353)
btnlimpa = Button(main, text = 'Limpar', command = limpar_canva)
btnlimpa.place(x=440, y=353)
btncalcular = Button(main, text = 'Calcular', command = import_demo)
btncalcular.place(x=360, y=353)

# Cria menubar
menubar = Menu(main)
# Adiciona Menu e commandos
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ficheiro', menu = file)
file.add_command(label ='Abrir...', command = browseFiles)
file.add_command(label ='Modo DEMO', command = demo)
file.add_separator()
file.add_command(label ='Sair', command = main.destroy)
  
# Adiciona menu ajuda
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ajuda', menu = help_)
help_.add_command(label ='Ajuda - Guia', command = ajuda_janela)
help_.add_separator()
help_.add_command(label ='Sobre', command = open_toplevel)

ll1 = Label(main,text = labeltext)
ll1.place(x=7, y=357)

# Mostrar janela (colocar sempre no final do ciclo da janela root (principal))
main.config(menu = menubar)
main.mainloop()
