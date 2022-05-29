from tkinter import *
from math import sqrt

app = Tk()

app.resizable(0,0)

app.title("Calculadora Python")

show = ""  #variavel que vai mudar o texto

equation = StringVar() #variavel que vai mostrar o texto

display = Label(app, textvariable = equation) # label para o display do texto

equation.set("0") # texto inicial no display

display.grid(columnspan = 4) #expandir o display em 4 espaços no grid


#Função que adiciona o valor do botao pressionado ao display
def btnPress(num):  
    global show
    if show == '0':
        if num == ".":
            pass
        else:
            show = ""
    show = show + str(num)
    equation.set(show)

# função que faz o calculo da equação
def evaluate():
    global show
    equation.set(show)
    total = str(eval(show))
    if len(total) > 20:
        total = str(total[0:20])
    equation.set(total)
    show= ""

#Função que limpa o display
def clear():
    global show
    show = "0"
    equation.set(show)

def fatorial(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return num * fatorial(num - 1)

def val_fat():
    global show
    show = int(show)
    v = fatorial(show)
    show = str(v)
    if len(show) > 20:
        show = str(show[0:20])
    equation.set(show)
    show = ""

def root():
    global show
    show = float(show)
    show = sqrt(show)
    show = str(show)
    equation.set(show)
    show = ""

    


# botoes numericos
one = Button(app, text = "1", command = lambda:btnPress(1), bg = "#5F9EA0")
one.grid(row = 1, column = 0)

two = Button(app, text = "2", command = lambda:btnPress(2), bg = "#5F9EA0")
two.grid(row = 1, column = 1)

three = Button(app, text = "3", command = lambda:btnPress(3), bg = "#5F9EA0")
three.grid(row = 1, column = 2)

four = Button(app, text = "4", command = lambda:btnPress(4), bg = "#5F9EA0")
four.grid(row = 2, column = 0)

five = Button(app, text = "5", command = lambda:btnPress(5), bg = "#5F9EA0")
five.grid(row= 2, column = 1)

six = Button(app, text = "6", command = lambda:btnPress(6), bg = "#5F9EA0")
six.grid(row = 2, column = 2)

seven = Button(app, text="7", command = lambda:btnPress(7), bg = "#5F9EA0")
seven.grid(row = 3, column = 0)

eight = Button(app, text="8", command = lambda:btnPress(8), bg = "#5F9EA0")
eight.grid(row = 3, column = 1)

nine = Button(app, text="9", command = lambda:btnPress(9), bg = "#5F9EA0")
nine.grid(row = 3, column = 2)

zero = Button(app, text = "0", command = lambda:btnPress(0), bg = "#5F9EA0")
zero.grid(row = 4, column = 1)

#Botoes de operadores

plus = Button(app, text = "+", command = lambda:btnPress("+"), bg = "#4682B4")
plus.grid(row = 1, column = 3)

minus = Button(app, text = "-", command = lambda:btnPress("-"), bg = "#4682B4")
minus.grid(row = 2, column = 3)

div = Button(app, text = "/", command = lambda:btnPress("/"), bg = "#4682B4")
div.grid(row = 3, column = 3)

mult = Button(app, text = "x", command = lambda:btnPress("*"), bg = "#4682B4")
mult.grid(row = 4, column = 3)


equal = Button(app, text = "=", command =  evaluate, bg = '#4169E1')
equal.grid(row = 5, column = 3)

clear = Button(app, text = "C", command = clear, bg = "red", fg = "white")
clear.grid(row= 4, column = 0)

dot = Button(app, text = ".", command = lambda:btnPress("."), bg = "#6495ED")
dot.grid(row = 5, column = 0)

pot = Button(app, text = "x²", command = lambda:btnPress("**"), bg = "#6495ED")
pot.grid(row = 5, column = 1)

fat = Button(app, text = "n!", command = val_fat, bg = "#6495ED")
fat.grid(row = 5, column = 2)

raiz = Button(app, text = "rt", command = root, bg = "#6495ED")
raiz.grid(row = 4, column = 2)

app.mainloop()