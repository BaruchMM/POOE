
# %% 

import mensajes as msj
import random as rn
import graficas_basicas as graf
m = msj.Mensajes()


# %% 

def generarSaludoHorario():
    hora = rn.randint(0,23)
    minutos = rn.randint(0,59)
    if (hora < 12):
        print('Hora actual: '+str(hora)+':'+str(minutos))
        m.saludoMatutino()
    if (hora >= 12) and (hora<19):
        print('Hora actual: '+str(hora)+':'+str(minutos))
        m.saludoMedioDia
    if (hora >= 19):
        print('Hora actual: '+str(hora)+':'+str(minutos))
        m.saludoNoche()
    print('_________________________________________________________________________')
for i in range(5):
    generarSaludoHorario()



# %% 

g = graf.GraficasAleatorias()
g.graficaUno()
g.graficaDos()

# %% 

valores = [15,20,13,28,12]
etiquetas = ['UNO', 'DOS', 'TRES', 'CUATRO', 'CINCO']
gP = graf.graficaPastel(valores,etiquetas)
gP.graficaUno()
# %%
