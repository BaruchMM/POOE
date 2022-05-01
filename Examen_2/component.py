import models as md
import random as rn
import csv

import numpy as np

# txt
def readData(path):
    data = []
    with open(path, 'r') as dataShop:
        for line in dataShop:
            line = line.strip()
            line = line.split()
            data.append(line)
    return  data

def readCSV(path):
    file = open(path)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    n = 0
    for row in csvreader:
        rows.append(row)
        n += 1
    data = rows
    file.close()
    return data

##################  client ######################
def getClient(NoCliente, nombre, correo, tipoCliente):
    cliente = md.Cliente(NoCliente, nombre, correo, tipoCliente)
    return cliente

def AllClients():
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allClients.csv'
    data = readCSV(path)
    clientes = {}
    print(data)
    for i in range(len(data)):
        NoCliente = data[i][0]
        print(data[i][0])
        cliente = getClient(NoCliente,data[i][1],data[i][2],data[i][3])
        clientes[NoCliente] = cliente
    return clientes

def viewClients(clientes):
    print('ID     \t Nombre:\t \t Mail: \t TipoCliente:')
    for n in clientes.keys():
        print(str(n)+'|'+str(clientes[n].nombre)+'|'+str(clientes[n].correo)+'|'+str(clientes[n].tipoCliente))

def newClient(clientes):
    NoCliente = md.Cliente.nocliente()
    nombre = input('Introduzca el nombre del cliente: ')
    mail = input('Introduzca el correo electrónico del cliente: ')
    tipo = 0
    print('Tipos de cliente:')
    print('\t1.- Oro')
    print('\t2.- Plata')
    print('\t3.- Bronce')
    while (tipo in ['1','2','3']) == False:
        tipo = input('Introduzca el número de la opción deseada por el cliente: ')
    if tipo == '1':
        tipoCliente = 'Oro'
    elif tipo == '2':
        tipoCliente = 'Plata'
    else:
        tipoCliente = 'Bronce'
    cliente = getClient(NoCliente,nombre,mail,tipoCliente)
    clientes[NoCliente] = cliente
    return clientes

def finDiaClientes(clientes):
    from datetime import date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allClients.csv'
    data = []
    header = ['NoCliente', 'nombre', 'mail', 'tipoCliente']
    for n in clientes.keys():
        data.append([clientes[n].NoCliente,clientes[n].nombre,clientes[n].correo,clientes[n].tipoCliente])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
##################  employees ######################

def getEmployees(NoEmpleado,Nombre,FechaNacimiento,departameto,ventasTotales):
    cliente = md.empleado(NoEmpleado,Nombre,FechaNacimiento,departameto,ventasTotales)
    return cliente

def AllEmployees():
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allEmployees.csv'
    data = [
        []
    ]
    empleados = {}
    print(data)
    for i in range(len(data)):
        NoEmpleado = data[i][0]
        empleado = getClient(NoEmpleado,data[i][1],data[i][2],data[i][3],data[i][4])
        empleados[NoEmpleado] = empleado
    return empleados

def viewEmployees(empleados):
    print('ID     \t Nombre:\t \t FechaNacimiento: \t departameto:\t ventasTotales:')
    for n in empleados.keys():
        print(str(n)+'|'+str(empleados[n].Nombre)+'|'+str(empleados[n].FechaNacimiento)+'|'+str(empleados[n].departameto)+'|'+str(empleados[n].ventasTotales))

def newEmployees(empleados,data):
    for i in range(len(data)):
        nombre = data[i][0]
        FechaNacimiento = []
        FechaNacimiento.append(data[i][1])
        FechaNacimiento.append(data[i][2])
        FechaNacimiento.append(data[i][3])
        departamento = (data[i][4])
        ventasTotales = data[i][5]
        NoEmpleado = md.empleado.noempleado(nombre,departamento)
        empleado = getEmployees(NoEmpleado,nombre,FechaNacimiento,departamento,ventasTotales)
        empleados[NoEmpleado] = empleado
    return empleados

def finDiaEmployees(empleados):
    from datetime import date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allEmployees.csv'
    data = []
    header = ['NoEmpleado', 'nombre','FechaNacimiento','departameto', 'ventasTotales']
    for n in empleados.keys():
        data.append([empleados[n].NoEmpleado,empleados[n].nombre,empleados[n].FechaNacimiento,empleados[n].departameto,empleados[n].ventasTotales])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


##################  producto ######################
def getProducto(ID,marca,precio,existencias):
    cliente = md.empleado(ID,marca,precio,existencias)
    return cliente

def AllProducto():
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allProducto.csv'
    data = readCSV(path)
    productos = {}
    print(data)
    for i in range(len(data)):
        ID = data[i][0]
        producto = getClient(ID,data[i][1],data[i][2],data[i][3])
        productos[ID] = producto
    return productos

def viewProducto(productos):
    print('ID     \t Marca:\t \t Precio: \t Existencias:')
    for n in productos.keys():
        print(str(n)+'|'+str(productos[n].marca)+'|'+str(productos[n].precio)+'|'+str(productos[n].existencias))

def newProducto(productos):
    marca = input('Introduzca la marca: ')
    precio = input('Ingrese el precio: ')
    existencias = input('Ingrese las existencias: ')
    ID = md.producto.generarID()
    producto = getClient(ID,marca,precio,existencias)
    productos[ID] = producto
    return productos

def finDiaProducto(productos):
    from datetime import date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allProducto.csv'
    data = []
    header = ['NoEmpleado', 'nombre','FechaNacimiento','departameto', 'ventasTotales']
    for n in productos.keys():
        data.append([productos[n].ID,productos[n].marca,productos[n].precio,productos[n].existencias])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)

##################  Ventas ######################
def getVentas(cantidad,producto, empleado, cliente,descuento):
    venta = md.ventas(cantidad,producto, empleado, cliente,descuento)
    return venta

def newVentas(ventas,clientes,productos,empleados):
    cantidad = input('Introduzca la cantidad: ')
    ID = input('Id del producto: ')
    NoEmpleado = input('Ingrese el NoEmpleado: ')
    NoCliente = input('Ingrese el NoCliente: ')
    total,decuentoCliente = md.ventas.calcularTotal(clientes,NoCliente,cantidad,productos,ID)
    venta = getClient(cantidad,ID, NoEmpleado, NoCliente,decuentoCliente)
    ventas[ID] = venta
    empleados = md.empleado.actualizarVentasTotales(NoEmpleado, empleados, total)
    return ventas,empleados

def viewVentas(productos):
    print('ID     \t Marca:\t \t Precio: \t Existencias:')
    for n in productos.keys():
        print(str(n)+'|'+str(productos[n].marca)+'|'+str(productos[n].precio)+'|'+str(productos[n].existencias))



def finDiaVentas(productos):
    from datetime import date
    today = date.today()
    d = today.strftime("%b-%d-%Y")
    path = '/home/baruch/Documentos/GitHub/POOE/Examen_2/allProducto.csv'
    data = []
    header = ['NoEmpleado', 'nombre','FechaNacimiento','departameto', 'ventasTotales']
    for n in productos.keys():
        data.append([productos[n].ID,productos[n].marca,productos[n].precio,productos[n].existencias])
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)
