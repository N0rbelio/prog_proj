from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

# Inicializar o GUI tkinter
root = Tk()
app = Window(root)

# Dimensões default
root.geometry('600x380')

# Definir titulo da janela
root.wm_title("Design circuito")

# show window
root.mainloop()