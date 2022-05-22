class persona():
    def __init__(self, nombre, sexo, edad, nacimiento):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.nacimiento = nacimiento
    
    def conslulta(self):
        print('Nombre: ',self.nombre,           
                '\nGenero: ',self.sexo,             
                '\nEdad: ',self.edad,               
                '\nLugar de Nacimiento: ',self.nacimiento)


class destreza():
    def __init__(self, mejorMateria, peorMateria):
        self.mejorMateria = mejorMateria
        self.peorMateria = peorMateria
    
    def conslulta(self):
        print('\nMateria con mejor rendimiento: ',self.mejorMateria,
                '\nMateria con menor rendimiento: ',self.peorMateria,)

class trabajo(persona):
    def __init__(self, pago, area, horas):
        self.pago = pago
        self.area = area
        self.horas = horas
    def conslulta(self):
        print('\nSalario: ',self.pago,
                '\nArea o departamento: ',self.area,
                '\nHoras de tranajo por semana: ',self.horas,)

class alumno(persona, destreza):
    def __init__(self, nombre, sexo, edad, nacimiento, mejorMateria, peorMateria,carrera, semestre, promedio, NUA ):
        #Invocamos los atrivutos de las clases persona y destreza para heredarlos a alumno
        persona.__init__(self, nombre, sexo, edad, nacimiento)
        destreza.__init__(self,mejorMateria, peorMateria)
        # Añadimos los atributos característicos del alumno
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.NUA = NUA
    
    def conslulta(self):
        persona.conslulta(self)
        destreza.conslulta(self)
        print('NUA: ', self.NUA,
            '\nSemestre: ', self.semestre,
            '\nPromedio: ', self.promedio,
            '\nCarrera: ', self.carrera)

class profesor(persona, destreza):
    def __init__(self, nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, NUE, antiguedad, grado, pago, area, horas):
        #Invocamos los atrivutos de las clases persona y destreza para heredarlos a profesor
        persona.__init__(self, nombre, sexo, edad, nacimiento)
        destreza.__init__(self,mejorMateria, peorMateria)
        trabajo.__init__(self,pago, area, horas)
        # Añadimos los atributos característicos del profesor
        self.NUE = NUE
        self.antiguedad = antiguedad
        self.grado = grado
    def conslulta(self):
        persona.conslulta(self)
        destreza.conslulta(self)
        trabajo.conslulta(self)
# nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, 
# NUE, antiguedad, grado, pago, area, horas
        print('\nGrado: ',self.grado,
                '\nNUE: ',self.NUE,
                '\nAntigüedad: ',self.antiguedad)


        


############ Inicializamos el programa ###########

# # modelo:  VarAlumno = alumno(nombre, sexo, edad, nacimiento, mejorMateria, peorMateria,carrera, semestre, promedio, NUA)
# VarAlumno = alumno("Juan El Sahili Martinez", "Masculino", 22, "Penjamo, Gto",
#  "POOyE", "Cosmología", 'Licenciatura en Física', 8, 9.01,427086)
# # Obtenemos la información del alumno:
# VarAlumno.conslulta()

# # modelo:  VarProfesor = profesor(nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, NUE, antiguedad, laboradas, grado)
# VarProfesor = profesor('Liset Karime Mejía Hernandez' , 'Femenino', 29, 'Leon, Gto.', 'Metodos matemáticos', 'POOE', '902010', '1 año', 3200, 'Doctorado')
# # Obtenemos la información del profesor:
# VarProfesor.conslulta()
