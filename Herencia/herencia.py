class Veiculo(object):
    def __init__(self,marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelerando = False
        self.frenando = False
    def arrancar(self):
        self.enMarcha = True
    def acelera(self):
        self.acelerando = True
    def frena(self):
        self.frenando = True
    def estado(self):
        print('Marca:',self.marca,'\nModelo: ',self.modelo,'\nEn Marcha:',self.enMarcha,
        '\nAcelerando: ',self.acelerando,'\nFrenando: ', self.frenando)

# class Moto(Veiculo):    Sobrescritura de metodos
#     pass
class Moto(Veiculo):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = 'Ajua!!!'
    def estado(self):
        print('Marca:',self.marca,'\nModelo: ',self.modelo,'\nEn Marcha:',self.enMarcha,
        '\nAcelerando: ',self.acelerando,'\nFrenando: ', self.frenando,'\ncaballito?',self.hcaballito)
miMoto = Moto("Apple","iMotoPro")
miMoto.caballito()
miMoto.estado()

# # # # # # # # # # # # Camioneta # # # # # # # # # # # # 
class Camioneta(Veiculo):
    carga = 0
    def Carga(self, carga):
        self.carga = carga
    def estado(self):
        print('Marca:',self.marca,'\nModelo: ',self.modelo,'\nEn Marcha:',self.enMarcha,
        '\nAcelerando: ',self.acelerando,'\nFrenando: ', self.frenando,'\nCarga:',self.carga)

laTroca = Camioneta('Jeep','Compas')
laTroca.Carga('1.4 Tn')
laTroca.estado()