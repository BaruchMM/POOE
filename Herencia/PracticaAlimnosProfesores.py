class persona():
    def __init__(self, nombre, sexo, edad, nacimiento):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.nacimiento = nacimiento
    
    def conslulta(self):
        print('\n\nNombre: ', self.nombre, '  |  ','Sexo: ', self.sexo, '  |  ', 'Edad: ', self.edad,
        '  |  ',  'Lugar de nacimiento: ', self.nacimiento)


class destreza():
    def __init__(self, mejorMateria, peorMateria):
        self.mejorMateria = mejorMateria
        self.peorMateria = peorMateria
    
    def conslulta(self):
        print('la mejor materia es: ', self.mejorMateria,'  |  ','La peor materia es: ', self.peorMateria)

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
        print('NUA: ', self.NUA,'  |  ','Semestre: ', self.semestre,'  |  ', 'Promedio: ', 
        self.promedio,'  |  ','Carrera: ', self.carrera)

class profesor(persona, destreza):
    def __init__(self, nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, NUE, antiguedad, laboradas, grado):
        #Invocamos los atrivutos de las clases persona y destreza para heredarlos a profesor
        persona.__init__(self, nombre, sexo, edad, nacimiento)
        destreza.__init__(self,mejorMateria, peorMateria)
        # Añadimos los atributos característicos del profesor
        self.NUE = NUE
        self.antiguedad = antiguedad
        self.laboradas = laboradas
        self.grado = grado
    
    def conslulta(self):
        persona.conslulta(self)
        destreza.conslulta(self)
        print('NUE: ', self.NUE,'  |  ','Antigüedad: ', self.antiguedad,'  |  ','Horas laboradas: ', 
        self.laboradas,'  |  ','Grado: ', self.grado)

############ Inicializamos el programa ###########

# modelo:  VarAlumno = alumno(nombre, sexo, edad, nacimiento, mejorMateria, peorMateria,carrera, semestre, promedio, NUA)
VarAlumno = alumno("Juan El Sahili Martinez", "Masculino", 22, "Penjamo, Gto",
 "POOyE", "Cosmología", 'Licenciatura en Física', 8, 9.01,427086)
# Obtenemos la información del alumno:
VarAlumno.conslulta()

# modelo:  VarProfesor = profesor(nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, NUE, antiguedad, laboradas, grado)
VarProfesor = profesor('Liset Karime Mejía Hernandez' , 'Femenino', 29, 'Leon, Gto.', 'Metodos matemáticos', 'POOE', '902010', '1 año', 3200, 'Doctorado')
# Obtenemos la información del profesor:
VarProfesor.conslulta()
