from tkinter import *

from tkinter import messagebox
bx1 = "1"
bx2 = "2"
bx3 = "3"
bx4 = "4"
bx5 = "5"
bx6 = "6"
bx7 = "7"
bx8 = "8"
bx9 = "9"
root=Tk()
root.geometry=("290x258")

button1 = Button(root, text = "  ", command = lambda: activate(1))
button1.grid(row="0",column="0",ipadx="40",ipady="30")
button2 = Button(root, text = "  ", command = lambda: activate(2))
button2.grid(row="0",column="1",ipadx="40",ipady="30")
button3 = Button(root, text = "  ", command = lambda: activate(3))
button3.grid(row="0",column="2",ipadx="40",ipady="30")
button4 = Button(root, text = "  ", command = lambda: activate(4))
button4.grid(row="1",column="0",ipadx="40",ipady="30")
button5 = Button(root, text = "  ", command = lambda: activate(5))
button5.grid(row="1",column="1",ipadx="40",ipady="30")
button6 = Button(root, text = "  ", command = lambda: activate(6))
button6.grid(row="1",column="2",ipadx="40",ipady="30")
button7 = Button(root, text = "  ", command = lambda: activate(7))
button7.grid(row="2",column="0",ipadx="40",ipady="30")
button8 = Button(root, text = "  ", command = lambda: activate(8))
button8.grid(row="2",column="1",ipadx="40",ipady="30")
button9 = Button(root, text = "  ", command = lambda: activate(9))
button9.grid(row="2",column="2",ipadx="40",ipady="30")
player=1
cnt=0
def activate(box):
    global player
    global cnt
    global bx1
    global bx2
    global bx3
    global bx4
    global bx5
    global bx6
    global bx7
    global bx8
    global bx9
    cnt=cnt+1
    if box == 1 and player == 1:
        button1.config(text="0")
        player = 2
        bx1="0"
    elif box == 1 and player == 2:
        button1.config(text="X")
        player = 1
        bx1="X"
    elif box == 2 and player == 1:
        button2.config(text="0")
        player = 2
        bx2 = "0"
    elif box == 2 and player == 2:
        button2.config(text="X")
        player = 1
        bx2 = "X"
    elif box == 3 and player == 1:
        button3.config(text="0")
        player = 2
        bx3="0"
    elif box == 3 and player == 2:
        button3.config(text="X")
        player = 1
        bx3="X"
    elif box == 4 and player == 1:
        button4.config(text="0")
        player = 2
        bx4="0"
    elif box == 4 and player == 2:
        button4.config(text="X")
        player = 1
        bx4="X"
    elif box == 5 and player == 1:
        button5.config(text="0")
        player = 2
        bx5="0"
    elif box == 5 and player == 2:
        button5.config(text="X")
        player = 1
        bx5="X"
    elif box == 6 and player == 1:
        button6.config(text="0")
        player = 2
        bx6="0"
    elif box == 6 and player == 2:
        button6.config(text="X")
        player = 1
        bx6="X"
    elif box == 7 and player == 1:
        button7.config(text="0")
        player = 2
        bx7="0"
    elif box == 7 and player == 2:
        button7.config(text="X")
        player = 1
        bx7="X"
    elif box == 8 and player == 1:
        button8.config(text="0")
        player = 2
        bx8="0"
    elif box == 8 and player == 2:
        button8.config(text="X")
        player = 1
        bx8="X"
    elif box == 9 and player == 1:
        button9.config(text="0")
        player = 2
        bx9="0"
    elif box == 9 and player == 2:
        button9.config(text="X")
        player = 1
        bx9="X"

    if bx1 == bx2 == bx3 == "0" or bx4 == bx5 == bx6 == "0" or bx7 == bx8 == bx9 == "0":
        player = "0"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif bx1 == bx2 == bx3 == "X" or bx4 == bx5 == bx6 == "X" or bx7 == bx8 == bx9 == "X":
        player = "0"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif bx1 == bx4 == bx7 == "0" or bx2 == bx5 == bx8 == "0" or bx3 == bx6 == bx9 == "0":
        player = "0"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif bx1 == bx4 == bx7 == "X" or bx2 == bx5 == bx8 == "X" or bx3 == bx6 == bx9 == "X":
        player = "X"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif bx1 == bx5 == bx9 == "0" or bx3 == bx5 == bx7 == "0":
        player = "0"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif bx1 == bx5 == bx9 == "X" or bx3 == bx5 == bx7 == "X":
        player = "X"
        messagebox._show("Game Ends! ", "Player " + player + " wins")
        exit(0)
    elif cnt == 9:
        message_.box("Game Ends! ", " Draw")
        exit(0)
root.mainloop()

