from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *


def showinputs():
    if var1.get() == 1:
        e1.config(show="")
    else:
        e1.config(show="*")


def login(event=None):
    if e1.get() == "admin":
        showinfo("Login", f"Welcome back {e1.get()}")
    else:
        showerror("Login", "Your username is not valid")
        e1.delete(0, END)


root = Tk()
root.resizable(0, 0)
root.title("Login form")
width = 350
height = 200
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw / 2) - (width / 2)
y = (sh / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))

lbl = Label(root, text="Username", font=("Helvitica", 10))


var1 = IntVar()


e1 = Entry(root, show="*")
e1.bind('<Return>', login)

showinput = Checkbutton(root, text="Show input",
                        command=showinputs, variable=var1)


btn = Button(root, text="Login", width=9, command=login)

lbl.place(x=20, y=50)

e1.place(x=120, y=50)

btn.place(x=250, y=160)

showinput.place(x=20, y=120)

showinputs()
root.mainloop()
