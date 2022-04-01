# %%
import numpy as np
import matplotlib.pyplot as plt
# %%
function = [[1,2,2,1,5,0],[3,5,2,2,6,1]]
x = np.linspace(-5, 5, 1000)

# %%

def CompuFunc(x,n):
    f_x = function[n][1]*(x**function[n][0])+function[n][2]*(x**function[n][3])+function[n][4]*(x*function[n][5])
    return f_x

# %%
def ploting(x,f_x,leg):
    with plt.style.context('Solarize_Light2'):
        plt.plot(x,f_x,label = leg)
        plt.grid()
        plt.title('Funciones')
        plt.legend()
    
# %%
f_x = []
#first function
n=0
fir_F = CompuFunc(x,n)
f_x.append(fir_F)
#second function
n=1
sec_F = CompuFunc(x,n)
f_x.append(sec_F)

# %%
plt.plot(x,fir_F)
# %%
leg = ['First function','Second function']
for i in range(len(f_x)):
    ploting(x,f_x[i],leg[i])
# %%
