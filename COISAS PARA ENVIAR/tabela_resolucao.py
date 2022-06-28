#Separador para resolução das instruções JSON 
#para circuito_gui
from tkinter import *
from tkinter import ttk

def tabela():
    tabela = Tk()
    tabela.geometry("450x250")
    tabela.title("Tabela de resolução")
    tabela.resizable(False, False)
    tabela['bg'] = 'blue'

    game_frame = Frame(tabela)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('link_id', 'link_value', 'link_go')

    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("link_id",anchor=CENTER, width=80)
    my_game.column("link_value",anchor=CENTER,width=80)
    my_game.column("link_go",anchor=CENTER,width=80)

    my_game.heading("#0",text="",anchor=CENTER)
    my_game.heading("link_id",text="ID (Gate)",anchor=CENTER)
    my_game.heading("link_value",text="Value",anchor=CENTER)
    my_game.heading("link_go",text="Go to",anchor=CENTER)

    my_game.insert(parent='',index='end',iid=0,text='',
    values=('1 (AND)','F','ID3_NOT'))
    my_game.insert(parent='',index='end',iid=1,text='',
    values=('2 (OR)','T','ID4_AND'))
    my_game.insert(parent='',index='end',iid=2,text='',
    values=('3 (NOT)','T','ID5_OR'))
    my_game.insert(parent='',index='end',iid=3,text='',
    values=('4 (AND)','F','ID5_OR'))
    my_game.insert(parent='',index='end',iid=4,text='',
    values=('5 (OR)','T','Value_Exit=T'))

    my_game.pack()
    tabela.mainloop()