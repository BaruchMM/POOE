# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2,4,80)
funcion = x**(-3*x+1)
print(np.array([x,funcion]))
plt.plot(x,funcion)

# %%
