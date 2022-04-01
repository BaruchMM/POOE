import matplotlib.pyplot as plt
import numpy as np
import random 

class GraficasAleatorias:
    def __init__(self):
        pass
    def graficaUno(self):
        x = np.linspace(0,10,1000)
        f_x = np.power(np.cos(x),2)
        f_y = np.sin(x)
        plt.plot(x,f_x)
        plt.plot(x,f_y)
        plt.show()
    def graficaDos(self):
        lista = []
        for i in range(100):
            lista.append(random.randint(0,500))
        plt.hist(lista,bins=20,color='red')
        plt.show()
class graficaPastel:
    def __init__(self,valores,etiquetas):
        self.valores = valores
        self.etiquetas = etiquetas

    def graficaUno(self):
        plt.pie(self.valores, labels= self.etiquetas)
        plt.show()