# %% 
import read_txt as read
import numpy as np
import matplotlib.pyplot as plt
# %% 
path = '/home/baruch/Documentos/GitHub/POOE/Practica_2_parcial_2/'
fileName = 'text.txt'
texto = read.archivos(path,fileName)
# %%
text = texto.readText()
# %%
hist = {'the':0, 'and':0, 'it':0, 'in':0, 'on':0}
# %%
for i in text:
  palabras = i.strip()
  for palabra in palabras.split():
    if palabra in hist.keys(): hist[palabra] += 1


# %%
plt.bar(x=hist.keys(), height=hist.values(), width=1, edgecolor="black")

# %%
text = texto.readText()
vocales = {'a':0, 'e':0, 'i':0, 'o':0,'u':0}
for i in text:
    for letra in i:
        letra = letra.lower()
        if letra in vocales.keys():
            vocales[letra] += 1 
print(vocales)
tot_voc = 0
for i in vocales.values(): 
  tot_voc += i
print('Total de vocales: ' +str(tot_voc))

# %%
text = texto.readText()
frases = 0
for parrafo in text:
  frases += len(parrafo.split('.'))
print('Total de frases: ' +str(frases))
# %%
text = texto.readText()
mayus = 0
for parrafo in text:
  for letra in parrafo:
    if letra.isupper() == True:
      mayus += 1
print('Total de mayusculas: ' +str(mayus))

# %%
