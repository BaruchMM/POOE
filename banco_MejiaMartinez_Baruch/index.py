
# %% 
from pydoc import cli
import models as md
import components as co
import random, string
import numpy as np

clientes = {}
clientes = co.inicializarUsuarios()
co.mostarClientes(clientes)
co.registrarCliente(clientes)
co.mostarClientes(clientes)

