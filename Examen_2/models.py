import random as rn
import string

class producto:
    def __init__(self, ID, marca, precio, existencias):
        self.__ID = ID
        self.__marca = marca
        self.__precio = precio
        self.__existencias = existencias

    def generarID(self):
        ID = (rn.choice(string.ascii_letters)).upper() + str(rn.randint(9)) + str(rn.randint(9)) + rn.choice(['a','e','i','o','u']) + str(rn.randint(9)) + str(rn.randint(9))
        return ID

    def actualizarExistencias(self,productos,ID):
        product = productos[ID]
        print("La cantidad de producto es " + str(product.existencias) + " elementos")
        existecias = input('Introdusca la nueva existecia: ')
        product.existencias = existecias
        productos[ID] = product
        return productos
    
    def actualizarPrecio(self,productos,ID):
        product = productos[ID]
        precioNuevo = input('Introdusca el nuevo precio: ')
        descuento = input('Indique el descuento en porcentaje: (%)')
        precioNuevo = precioNuevo - precioNuevo*descuento/100
        product.precio = precioNuevo
        productos[ID] = product
        return productos

class Cliente:
    def __init__(self, NoCliente, nombre, correo, tipoCliente):
        self.NoCliente = NoCliente
        self.nombre = nombre
        self.correo = correo
        self.tipoCliente = tipoCliente
    
    def nocliente():
        items = string.ascii_letters + str(0) + str(1) + str(2) + str(3) + str(4) + str(5) + str(6) + str(7) + str(8) + str(9)
        NoCliente =  rn.choice(items) + rn.choice(items) + rn.choice(items) + rn.choice(items) + rn.choice(items) + rn.choice(items) + rn.choice(items) + rn.choice(items)
        return NoCliente  

    def actualizarPrecio(self,NoCliente, clientes):
        cliente = clientes[NoCliente]
        correoNuevo = input('Introdusca el nuevo correo electrónico: ')
        cliente.correo = correoNuevo
        clientes[NoCliente] = cliente
        return clientes  
        
    def actualizarTipoCliente(self,NoCliente, clientes):
        cliente = clientes[NoCliente]
        print('Seleccione el tipo de cliente deseado introduciendo el número de opción')
        print('1.- Oro')
        print('2.- Plata')
        print('3.- Bronce')
        opcion = 's'
        while(opcion in [1,2,3]) == False:
            opcion = int(input('Introdusca la opción deseada: '))
        tipo = ''
        print(opcion)
        if opcion == 1:
            tipo = 'Oro'
        elif opcion == 2:
            tipo = 'Plata'
        else:
            tipo = 'Bronce'
        cliente.tipoCliente = tipo
        clientes[NoCliente] = cliente
        return clientes  

class empleado:
    def __init__(self,NoEmpleado,Nombre,FechaNacimiento,departameto,ventasActuales,ventasTotales):
        self.NoEmpleado = NoEmpleado
        self.Nombrenombre = Nombre
        self.FechaNacimiento = FechaNacimiento #[dd,mm,aaaa]
        self.departameto = departameto
        self.ventasActuales = ventasActuales
        self.ventasTotales = ventasTotales #dinero acumulado por todas las ventas
    
    def noempleado(self,nombre,departamento):
        items = string.ascii_letters + str(0) + str(1) + str(2) + str(3) + str(4) + str(5) + str(6) + str(7) + str(8) + str(9)
        NoEmpleado =  nombre[1]+nombre[1]+nombre[1]+rn.choice(items)+rn.choice(items)+rn.choice(items)+rn.choice(['a','e','i','o','u'])+rn.choice(['a','e','i','o','u'])+rn.choice(items)+rn.choice(items)+(departamento[0]).upper()
        return NoEmpleado
    
    def actualizarVentasTotales(self,NoEmpleado, empleados, importeVenta):
        empleado = empleados[NoEmpleado]
        Ventas = importeVenta + empleado.ventasTotales
        empleado.ventasTotales = Ventas
        empleados[NoEmpleado] = empleado
        return empleados  

    def calcularSueldo(self,NoEmpleado, empleados):
        empleado = empleados[NoEmpleado]
        edad = 2022 - (empleado.FechaNacimiento)[2]
        sueldoBase = float(input('Introdusca el sueldo base:'))
        ventasTotales = empleado.ventasTotales
        bonoVentas = ventasTotales*0.05
        if edad > 40 and edad < 50:
            bonoEdad = 0.03*sueldoBase
        elif edad > 50:
            bonoEdad = 0.015*sueldoBase
        elif edad < 30:
            bonoEdad = 0.035*sueldoBase
        else: bonoEdad = 0
        sueldo = sueldoBase + bonoEdad + bonoVentas
        empleado.sueldo = sueldo
        empleados[NoEmpleado] = empleado
        return empleados  

class ventas:
    def __init__(self,cantidad,producto, empleado, cliente,descuento):
        self.cantidad = cantidad
        self.producto = producto
        self.empleado = empleado #
        self.cliente = cliente
        self.descuento = descuento
        
    def calcularTotal(self,clientes,NoCliente,cantidad,productos,ID):
        if clientes[NoCliente].tipoCliente == 'Oro':
            decuentoCliente = 0.08
        elif clientes[NoCliente].tipoCliente == 'Plata':
            decuentoCliente = 0.05
        else:
            decuentoCliente = 0.03
        producto = productos[ID]
        total = cantidad*producto.precio - decuentoCliente
        return total
            



