from tkinter import *
from time import strftime
from tkinter.ttk import * # Inicializar widgets
from tkinter import ttk
import webbrowser
# import filedialog module
from tkinter import filedialog

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# Inicializar o GUI tkinter
main = Tk()
# Opçoes janela main
main.geometry('600x400') # Definir tamanho
main.wm_title("Design circuito") # Definir titulo da janela
main.iconbitmap("favicon.ico")

#Explorador de ficheiros
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Selecione o ficheiro com as intruções",
                                          filetypes = (("Ficheiros JSON", "*.json*"), ("Ficheiros LogicView", "*.lcvw*"), ("Todos os ficheiros", "*.*")))

#Cria janela sobre
def open_toplevel():
    top = Toplevel()
    top.geometry("500x130")
    top.title("Sobre")
    l2 = Label(top, text = "Este projeto foi criado por: Andre Oliveira, Daniel Oleksiychuk e Tiago Loureiro")
    l2.pack()

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
                        compound = TOP).pack(side = TOP)

    top.mainloop()

#Cria janela ajuda
def ajuda_aguh():
    ajuda = Toplevel()
    ajuda.geometry("500x400")
    ajuda.title("Ajuda")

    titlo = Label(ajuda, text = "Ajuda para Design Circuito", font=("Arial", 20))
    titlo.pack()

    ll1 = Label(ajuda,text ='O programa permite abrir ficheiros JSON ou LogicView para demonstrar as portas logicas num plano. ', wraplength=490)
    # using place method we can set the position of label
    ll1.place(x=5, y=50)


#Canvas desenho das logicas
C = Canvas(main, bg="white", height=340, width=590)
 
line = C.create_line(108, 120,
                     320, 40,
                     fill="green")
 
oval1 = C.create_oval(80, 30, 140,
                     150,
                     fill="blue")
 
C.pack()

#Texto em baixo
ll1 = Label(main,text ='Por favor, abra um ficheiro!')
# using place method we can set the position of label
ll1.place(x=5, y=352)
#Criar botão
btn = Button(main, text = 'Reset',
                command = main.destroy)
btn.place(x=517, y=348)

# Cria menubar
menubar = Menu(main)
# Adiciona Menu e commandos
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ficheiro', menu = file)
file.add_command(label ='Abrir...', command = browseFiles)
file.add_separator()
file.add_command(label ='Sair', command = main.destroy)
  
# Adiciona menu ajuda
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Ajuda', menu = help_)
help_.add_command(label ='Ajuda - Guia', command = ajuda_aguh)
help_.add_separator()
help_.add_command(label ='Sobre', command = open_toplevel)

# Mostrar janela (colocar sempre no final do ciclo da janela root (principal))
main.config(menu = menubar)
main.mainloop()