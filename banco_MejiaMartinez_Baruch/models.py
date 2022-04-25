import datetime
import random, string
import numpy as np
class persona:
    def __init__(self, nombre, nacimiento, lugarNacimiento, RFC, edad, direccion, telefono, mail):
        self.nombre = nombre
        self.nacimiento = nacimiento
        self.lugarNacimiento = lugarNacimiento
        self.RFC = RFC
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono
        self.mail = mail
    # fecha = [dia,mes,año]
    def generarRFC(nombre,nacimiento):
        RFC = nombre[1][0] + nombre[1][1] + nombre[2][0] + nombre[0][0] + str(nacimiento[2][2]) + str(nacimiento[2][3]) + str(nacimiento[1]) + str(nacimiento[0]) + random.choice(string.ascii_letters) + random.choice(['0','1','2','3','4','5','6','7','8','9']) + random.choice(string.ascii_letters)
        return RFC.upper()

    def actualizarDatos(persona):
        return persona

class CuentaBancaria:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
    # posible ramification: CuentaBancaria.cliente = persona
    def ConsultarSaldo(cuentaBancaria, numero):
        cuenta = cuentaBancaria[numero]
        saldo = cuenta.saldo
        print('El saldo disponible para el usuario '+str(cuenta.cliente.nombre)+' es de: $'+str(saldo))
