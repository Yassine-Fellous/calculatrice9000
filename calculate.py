import tkinter
from tkinter import *

root=Tk()
root.title("Simple calculator")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#03224c")

input_string = ""
def add_number(number):
    global input_string
    input_string += str(number)
    echo.config(text=input_string)

def add_point(point):
    global input_string
    input_string += point
    echo.config(text=input_string)

def dele():
    global input_string
    input_string = ""
    echo.config(text=input_string)

def add():
    global input_string
    input_string += "+"
    echo.config(text=input_string)

def subtract():
    global input_string
    input_string += "-"
    echo.config(text=input_string)

def multi():
    global input_string
    input_string += "*"
    echo.config(text=input_string)

def divi():
    global input_string
    input_string += "/"
    echo.config(text=input_string)

def carre():
    global input_string
    input_string += "** 0.5"
    echo.config(text=input_string)

def calculate():
    global input_string
    result = eval(input_string)
    input_string = str(result)
    echo.config(text=input_string)

def pourc():
    global input_string
    result = eval(input_string) / 100
    input_string = str(result)
    echo.config(text=input_string)

echo= Label(root, text="",width=25, height=2, font=('arial', 30,))#la ou les calcule et les resultats font s'afficher
echo.pack()

Button(root, text="1", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(1)).place(x=10, y=200)
Button(root, text="2", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(2)).place(x=150, y=200)
Button(root, text="3", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(3)).place(x=290, y=200)
Button(root, text="C", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=dele).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(4)).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(5)).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(6)).place(x=290, y=300)
Button(root, text="+", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'),command=add).place(x=430, y=300)

Button(root, text="7", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(7)).place(x=10, y=400)
Button(root, text="8", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(8)).place(x=150, y=400)
Button(root, text="9", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(9)).place(x=290, y=400)
Button(root, text="-", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=subtract).place(x=430, y=400)

Button(root, text="0", width=11, height=1, font=('arial', 30, 'bold'), command=lambda: add_number(0)).place(x=10, y=500)
Button(root, text=".", width=5, height=1, font=('arial', 30, 'bold'), command=lambda: add_point(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=calculate).place(x=430, y=500)

Button(root, text="*", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=multi).place(x=10, y=100)
Button(root, text="/", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=divi).place(x=150, y=100)
Button(root, text="%", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=pourc).place(x=290, y=100)
Button(root, text="√", width=5, height=1, bg='#ff7f00', fg='#FFFFFF', font=('arial', 30, 'bold'), command=carre).place(x=430, y=100)


root.mainloop()