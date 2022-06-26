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
main.geometry('600x380') # Definir tamanho
main.wm_title("Design circuito") # Definir titulo da janela

#Explorador de ficheiros
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))

#Cria janela sobre
def open_toplevel():
    top = Toplevel()
    top.geometry("500x100")
    top.title("Squirt")
    l2 = Label(top, text = "Este projeto foi criado por: Andre Oliveira, Daniel Oleksiychuk e David Lameiro")
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
    Button(top, text = '  Clit !', command = openweb, image = photoimage,
                        compound = LEFT).pack(side = TOP)

    top.mainloop()

# Cria menubar
menubar = Menu(main)
# Adiciona Menu e commandos
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='Open...', command = browseFiles)
file.add_separator()
file.add_command(label ='Exit', command = main.destroy)
  
# Adiciona menu ajuda
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Ajuda', command = None)
help_.add_separator()
help_.add_command(label ='Sobre', command = open_toplevel)

# Mostrar janela (colocar sempre no final do ciclo da janela root (principal))
main.config(menu = menubar)
main.mainloop()