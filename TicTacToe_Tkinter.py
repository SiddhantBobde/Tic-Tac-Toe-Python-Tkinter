from tkinter import *
import tkinter.messagebox
game=Tk()
game.title("Tic Tac Toe")

click=True
flag=0
def buttonclick(buttons):
    global click,flag
    if buttons["text"]=="" and click==True:
        buttons["text"]="X"
        click=False
        CheckWin()
        flag+=1
    elif buttons["text"]=="" and click==False:
        buttons["text"]="O"
        click=True
        CheckWin()
        flag+=1
    else:
        game.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

def

def disablebutton():
    b1["state"]="disabled"
    b2["state"] = "disabled"
    b3["state"] = "disabled"
    b4["state"] = "disabled"
    b5["state"] = "disabled"
    b6["state"] = "disabled"
    b7["state"] = "disabled"
    b8["state"] = "disabled"
    b9["state"] = "disabled"

def CheckWin():
    if (b1["text"]=='X' and b2["text"]=='X' and b3["text"]=='X' or
        b4["text"]=='X' and b5["text"]=='X' and b6["text"]=='X' or
        b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X' or
        b1["text"]=='X' and b4["text"]=='X' and b7["text"]=='X' or
        b2["text"]=='X' and b5["text"]=='X'and b8["text"]=='X' or
        b3["text"]=='X' and b6["text"]=='X' and b9["text"]=='X' or
        b7["text"]=='X' and b8["text"]=='X' and b9["text"]=='X' or
        b1["text"]=='X' and b5["text"]=='X' and b9["text"]=='X' or
        b3["text"]=='X' and b5["text"]=='X' and b7["text"]=='X'):
            disablebutton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player X wins")

    elif flag == 8:
        disablebutton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (b1["text"]=='O' and b2["text"]=='O' and b3["text"]=='O' or
        b4["text"]=='O' and b5["text"]=='O' and b6["text"]=='O' or
        b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O' or
        b1["text"]=='O' and b4["text"]=='O' and b7["text"]=='O' or
        b2["text"]=='O' and b5["text"]=='O' and b8["text"]=='O' or
        b3["text"]=='O' and b6["text"]=='O' and b9["text"]=='O' or
        b7["text"]=='O' and b8["text"]=='O' and b9["text"]=='O' or
        b1["text"]=='O' and b5["text"]=='O' and b9["text"]=='O' or
        b3["text"]=='O' and b5["text"]=='O' and b7["text"]=='O'):
        disablebutton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player O wins")

game.columnconfigure(0,weight=1)
game.columnconfigure(1,weight=1)
game.columnconfigure(2,weight=1)
game.rowconfigure(0,weight=1)
game.rowconfigure(1,weight=1)
game.rowconfigure(2,weight=1)

b1=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b1))
b1.grid(row=0,column=0)

b2=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b2))
b2.grid(row=0,column=1)

b3=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b3))
b3.grid(row=0,column=2)

b4=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b4))
b4.grid(row=1,column=0)

b5=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b5))
b5.grid(row=1,column=1)

b6=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b6))
b6.grid(row=1,column=2)

b7=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b7))
b7.grid(row=2,column=0)

b8=Button(game,text="",height='5',width='10',bg='grey',command=lambda : buttonclick(b8))
b8.grid(row=2,column=1)

b9=Button(game,text="",height='5',width='10',bg='grey',command=lambda :buttonclick(b9))
b9.grid(row=2,column=2)

game.mainloop()
