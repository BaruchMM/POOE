from cgitb import reset
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk, font  # Carga ttk (para widgets nuevos 8.5+)
import getpass



app = Tk()
app.geometry("370x400")
app.resizable(0,0)
app.config(bg='gray')
app.title("Calculadora Python")

show = ""  #variavel que vai mudar o texto

equation = StringVar() #variavel que vai mostrar o texto

d = Frame()
d.config(bg='white')
d.pack()
d.config(width=350, height=50)
display = Frame()
display.config(bg='white')
display.pack()
display.config(width=350, height=50)
display.place(x=175,y=20)
res = Label(display, textvariable = equation,bg='white') # label para o display do texto
equation.set("0") # texto inicial no display

res.grid(columnspan = 4) #expandir o display em 4 espaços no grid

asdfasfsdagtasergfasdfERWEFsdf
app.mainloop()