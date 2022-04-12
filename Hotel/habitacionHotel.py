# -*- coding: utf-8 -*-
"""
@author: Irazu
"""

class HabitacionHotel:
    __estatus = False

    def __init__(self, numero, cliente, camas, serviciosIncluidos, serviciosAdicionales):
        self.__numero = numero
        self.cliente = cliente
        self.__camas = camas
        self.__serviciosIncluidos = serviciosIncluidos
        self.serviciosAdicionales = serviciosAdicionales
        if(self.cliente == ""):
            self.__estatus = False
        else:
            self.__estatus = True

    def ocuparHabitacion(self, cliente):
        if(not self.__estatus):
            self.__estatus = True
            self.cliente = cliente
            return True
        else:
            return False

    def getSerIncl(self):
        return self.__serviciosIncluidos
        
    def dejarHabitacion(self):
        if(self.__estatus):
            self.__estatus = False
            self.cliente = ""
            return True
        else:
            return False
    
    def solicitarServicioAdicional(self, servicio):
        self.serviciosAdicionales.append(servicio)
    
    def getCamas(self):
        return self.__camas

    def getNumero(self):
        return self.__numero

    def getEstatus(self):
        return self.__estatus