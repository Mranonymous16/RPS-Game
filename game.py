from tkinter import *
import random

root = Tk()
root.title("Rock_Paper_Scissor")
root.geometry('500x500+20+10')
Label(root, text="ROCK PAPER SCISSOR", fg='red',
      font=("Bold", 23)).pack()
b1 = Button(root, text="Rock", width=10, height=3, command=lambda: game(1))
b2 = Button(root, text="Paper", width=10, height=3, command=lambda: game(2))
b3 = Button(root, text="Scissor", width=10, height=3, command=lambda: game(3))
b1.place(x=100, y=50)
b2.place(x=200, y=50)
b3.place(x=300, y=50)
l1 = Label(root, text="Your choice: ")
l1.place(x=30, y=150)
e1 = Entry(root, bd=5, width=15)
e1.place(x=105, y=150)

l2 = Label(root, text="Computer choice: ")
l2.place(x=260, y=150)
e2 = Entry(root, bd=5, width=15)
e2.place(x=360, y=150)

l3 = Label(root, text="Result: ").place(x=150, y=220)
e3 = Entry(root, bd=5, width=15)
e3.place(x=200, y=220)


def game(args):
    if args == 1:
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e1.insert(END, "Rock")
        e2.insert(END, random.choices(["Rock", "Paper", "Scissor"]))
    if args == 2:
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e1.insert(END, "Paper")
        e2.insert(END, random.choices(["Rock", "Paper", "Scissor"]))
    if args == 3:
        e1.delete(0, 'end')
        e2.delete(0, 'end')
        e1.insert(END, "Scissor")
        e2.insert(END, random.choices(["Rock", "Paper", "Scissor"]))

    v1 = e1.get()
    v2 = e2.get()

    if v1 == 'Rock':
        if v2 == 'Scissor':
            e3.delete(0, 'end')
            e3.insert(END, "Player wins")
        elif v2 == 'Paper':
            e3.delete(0, 'end')
            e3.insert(END, "Computer wins")
        else:
            e3.delete(0, 'end')
            e3.insert(END, "Tie")
    if v1 == 'Paper':
        if v2 == 'Scissor':
            e3.delete(0, 'end')
            e3.insert(END, "Computer wins")
        elif v2 == 'Rock':
            e3.delete(0, 'end')
            e3.insert(END, "Player wins")
        else:
            e3.delete(0, 'end')
            e3.insert(END, "Tie")
    if v1 == 'Scissor':
        if v2 == 'Rock':
            e3.delete(0, 'end')
            e3.insert(END, "Computer wins")
        elif v2 == 'Paper':
            e3.delete(0, 'end')
            e3.insert(END, "Player wins")
        else:
            e3.delete(0, 'end')
            e3.insert(END, "Tie")
root.mainloop()