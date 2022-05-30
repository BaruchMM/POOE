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
        self.equation.set("0") # texto inicial no display
        
        self.res.grid(columnspan = 4) #expandir o display em 4 espaços no grid


        # botoes numericos
        self.panel = Frame()
        self.panel.config(bg='white')
        self.one = Button(self.panel, text = "1", height = 6, width = 7,command = lambda:self.presionarBoton(1), bg = "#5F9EA0")
        self.one.grid(row = 1, column = 0)

        self.two = Button(self.panel, text = "2", height = 6, width = 7,command = lambda:self.presionarBoton(2), bg = "#5F9EA0")
        self.two.grid(row = 1, column = 1)

        self.three = Button(self.panel, text = "3", height = 6, width = 7,command = lambda:self.presionarBoton(3), bg = "#5F9EA0")
        self.three.grid(row = 1, column = 2)

        self.four = Button(self.panel, text = "4", height = 6, width = 7,command = lambda:self.presionarBoton(4), bg = "#5F9EA0")
        self.four.grid(row = 2, column = 0)

        self.five = Button(self.panel, text = "5", height = 6, width = 7,command = lambda:self.presionarBoton(5), bg = "#5F9EA0")
        self.five.grid(row= 2, column = 1)

        self.six = Button(self.panel, text = "6", height = 6, width = 7,command = lambda:self.presionarBoton(6), bg = "#5F9EA0")
        self.six.grid(row = 2, column = 2)

        self.seven = Button(self.panel, text="7", height = 6, width = 7,command = lambda:self.presionarBoton(7), bg = "#5F9EA0")
        self.seven.grid(row = 3, column = 0)

        self.eight = Button(self.panel, text="8",height = 6, width = 7,command = lambda:self.presionarBoton(8), bg = "#5F9EA0")
        self.eight.grid(row = 3, column = 1)

        self.nine = Button(self.panel, text="9", height = 6, width = 7,command = lambda:self.presionarBoton(9), bg = "#5F9EA0")
        self.nine.grid(row = 3, column = 2)

        self.zero = Button(self.panel, text = "0", height = 6, width = 7,command = lambda:self.presionarBoton(0), bg = "#5F9EA0")
        self.zero.grid(row = 4, column = 1)

        self.botonSum = Button(self.panel, text="+",height = 6, width = 7, command=self.sumar)
        self.botonSum.grid(row = 3, column = 3)
        self.botonCancel = Button(self.panel, text="AC",height = 6, width = 7, command=quit)
        self.botonCancel.grid(row = 0, column = 4)
        self.botonRetar = Button(self.panel, text="-",height = 6, width = 7, command=self.restar)
        self.botonRetar.grid(row = 3, column = 4)
        self.botonMulti = Button(self.panel, text="x",height = 6, width = 7, command=self.multiplicar)
        self.botonMulti.grid(row = 2, column = 3)
        self.botonDividir = Button(self.panel, text="÷",height = 6, width = 7, command=self.dividir)
        self.botonDividir.grid(row = 0, column = 4)
        self.panel.pack()
        

        # Se definen las posiciones de los txt, separador, label y botones
        # self.etiq1.place(x=30, y=40)
        # self.etiq2.place(x=30, y=80)
        # self.etiq3.place(x=200, y=120)
        self.app.mainloop()
    # Se definen los metodos para las distintas funciones de aritmetica
    def presionarBoton(self,numero):
        print(numero)
    def sumar(self):
        resultado = self.numero1.get() + self.numero2.get()
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado)) 

    def restar(self):
        resultado = self.numero1.get() - self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

    def multiplicar(self):
        resultado = self.numero1.get() * self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

    def dividir(self):
        resultado = self.numero1.get() / self.numero2.get()
        print(resultado)
        # se utiliza este metodo para limpiar los txt y el focus para que volver a ingresar un numero
        self.numero1.set("")
        self.numero2.set("")
        self.txt_numero1.focus_set()
        self.etiq3.configure(foreground='blue')
        self.mensaje.set(str(resultado))

def main():
    mi_app = Aplication()
    return 0

if __name__ == '__main__':
    main()