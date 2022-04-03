# %% 
import read_txt as read
import numpy as np
import matplotlib.pyplot as plt
# %% 
path = '/home/baruch/Documentos/GitHub/POOE/Practica_2_parcial_2/'
fileName = 'text.txt'

# %%
text = open(path + fileName, encoding="utf8") 
print(text)
# %%
hist = {'the':0, 'and':0, 'it':0, 'in':0, 'on':0}
# %%
for i in text:
    for letra in i:
        letra = letra.lower()
        if letra in hist.keys():
            hist[letra] += 1 

# %%
plt.bar(x=hist.keys(), height=hist.values(), width=1, edgecolor="black")

# %%
