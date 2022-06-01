from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk, font  # Carga ttk (para widgets nuevos 8.5+)
import getpass

class Aplication():
    def __init__(self):
        self.app = Tk()
        self.app.geometry("370x400")
        self.app.config(bg='gray')
        self.app.title("Calculadora Python")

        self.show = ""  #variavel que vai mudar o texto

        self.equation = StringVar() #variavel que vai mostrar o texto

        self.d = Frame()
        self.d.config(bg='white')
        self.d.pack()
        self.d.config(width=350, height=50)
        self.display = Frame()
        self.display.config(bg='white')
        # self.display.pack()
        self.display.config(width=350, height=50)
        self.display.place(x=175,y=20)
        self.res = Label(self.display, textvariable = self.equation,bg='white') # label para o display do texto
        self.result = str(0)
        self.equation.set(self.result) # texto inicial no display
        self.ans = ''
        self.res.grid(columnspan = 4) #expandir o display em 4 espaços no grid
        self.numeros = []

        # botoes numericos
        self.panel = Frame()
        self.panel.config(bg='white')
        self.one = Button(self.panel, text = "1", height = 4, width = 7,command = lambda:self.presionarBoton(1), bg = "gray")
        self.one.grid(row = 1, column = 0)

        self.two = Button(self.panel, text = "2", height = 4, width = 7,command = lambda:self.presionarBoton(2), bg = "gray")
        self.two.grid(row = 1, column = 1)

        self.three = Button(self.panel, text = "3", height = 4, width = 7,command = lambda:self.presionarBoton(3), bg = "gray")
        self.three.grid(row = 1, column = 2)

        self.four = Button(self.panel, text = "4", height = 4, width = 7,command = lambda:self.presionarBoton(4), bg = "gray")
        self.four.grid(row = 2, column = 0)

        self.five = Button(self.panel, text = "5", height = 4, width = 7,command = lambda:self.presionarBoton(5), bg = "gray")
        self.five.grid(row= 2, column = 1)

        self.six = Button(self.panel, text = "6", height = 4, width = 7,command = lambda:self.presionarBoton(6), bg = "gray")
        self.six.grid(row = 2, column = 2)

        self.seven = Button(self.panel, text="7", height = 4, width = 7,command = lambda:self.presionarBoton(7), bg = "gray")
        self.seven.grid(row = 3, column = 0)

        self.eight = Button(self.panel, text="8",height = 4, width = 7,command = lambda:self.presionarBoton(8), bg = "gray")
        self.eight.grid(row = 3, column = 1)

        self.nine = Button(self.panel, text="9", height = 4, width = 7,command = lambda:self.presionarBoton(9), bg = "gray")
        self.nine.grid(row = 3, column = 2)

        self.zero = Button(self.panel, text = "0", height = 4, width = 7,command = lambda:self.presionarBoton(0), bg = "gray")
        self.zero.grid(row = 4, column = 0)

        self.botonSum = Button(self.panel, text="+",height = 4, width = 7, command=self.sumar)
        self.botonSum.grid(row = 3, column = 3)
        self.botonCancel = Button(self.panel, text="AC",height = 4, width = 7, command=self.restart, bg = "red")
        self.botonCancel.grid(row = 1, column = 4)
        self.botonDel = Button(self.panel, text="Del",height = 4, width = 7, command=self.delete, bg = "red")
        self.botonDel.grid(row = 1, column = 3)
        self.botonRetar = Button(self.panel, text="-",height = 4, width = 7, command=self.restar)
        self.botonRetar.grid(row = 3, column = 4)
        self.botonMulti = Button(self.panel, text="x",height = 4, width = 7, command=self.multiplicar)
        self.botonMulti.grid(row = 2, column = 3)
        self.botonDividir = Button(self.panel, text="÷",height = 4, width = 7, command=self.dividir)
        self.botonDividir.grid(row = 2, column = 4)
        self.botonANS = Button(self.panel, text="ANS",height = 4, width = 7, command=self.dividir)
        self.botonANS.grid(row = 4, column = 3)
        self.botonEqual = Button(self.panel, text="=",height = 4, width = 7, command=self.calcular)
        self.botonEqual.grid(row = 4, column = 4)
        self.botonExp = Button(self.panel, text="10^x",height = 4, width = 7, command=self.dividir)
        self.botonExp.grid(row = 4, column = 2)
        self.botonDot = Button(self.panel, text=".",height = 4, width = 7,command = lambda:self.presionarBoton('.'))
        self.botonDot.grid(row = 4, column = 1)
        self.panel.pack()
        
        self.app.mainloop()
    def restart(self):
        self.result = '0'
        self.equation.set(self.result)

    def delete(self):
        if len(self.result) <= 1:
            self.result = '0'
            self.equation.set(self.result)
        elif self.result[-1] == ' ':
            self.result = self.result[:-1]
            self.result = self.result[:-1]
            self.equation.set(self.result)
        else:
            self.result = self.result[:-1]
            self.equation.set(self.result)

    def presionarBoton(self,num):  
        if self.result == '0':
            if num == ".":
                pass
            else:
                self.result = ""
        self.result = self.result + str(num)
        self.equation.set(self.result)

    def sumar(self):
       self.result = self.result +' '+ '+' +' '
       self.equation.set(self.result)

    def restar(self):
        self.result = self.result +' '+ '-' +' '
        self.equation.set(self.result)

    def multiplicar(self):
        self.result = self.result +' '+ 'x' +' '
        self.equation.set(self.result)

    def dividir(self):
        self.result = self.result +' '+ '÷' +' '
        self.equation.set(self.result)
    
  
    def calcular(self):
        self.result += ' ñ'
        self.result = self.result.split(" ")
        final = False
        i = 0
        while final != True:
            print(self.result)
            if self.result[i] == 'ñ':
                self.result.pop(i)
                final = True
            else:
                if self.result[i] == 'x':
                    res = float(self.result[i-1])*float(self.result[i+1])
                    self.result[i] = res
                    self.result.pop(i-1)
                    self.result.pop(i)
                    i -= 1
                elif self.result[i] == '÷':
                    res = float(self.result[i-1])/float(self.result[i+1])
                    self.result[i] = res
                    self.result.pop(i-1)
                    self.result.pop(i)
                    i -= 1
                elif self.result[i] == '+':
                    res = float(self.result[i-1])+float(self.result[i+1])
                    self.result[i] = res
                    self.result.pop(i-1)
                    self.result.pop(i)
                    i -= 1
                elif self.result[i] == '-':
                    res = float(self.result[i-1])-float(self.result[i+1])
                    self.result[i] = res
                    self.result.pop(i-1)
                    self.result.pop(i)
                    i -= 1
            i += 1
            self.equation.set(self.result)
        
        

def main():
    mi_app = Aplication()

if __name__ == '__main__':
    main()