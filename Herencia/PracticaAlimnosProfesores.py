class persona():
    def __init__(self, nombre, sexo, edad, nacimiento):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.nacimiento = nacimiento
    
    def info(self):
        print("\nNombre: ", self.nombre,"\nSexo: ", self.sexo,"\nEdad: ", self.edad,
        "\nLugar de nacimiento: ", self.nacimiento)


class destreza():
    def __init__(self, mejorMateria, peorMateria):
        self.mejorMateria = mejorMateria
        self.peorMateria = peorMateria
    
    def info(self):
        print('\nla mejor materia es: ', self.mejor_materia,'\nLa peor materia es: ', self.peor_materia)

class alumno(persona, destreza):
    def __init__(self, carrera, semestre, promedio, NUA ):
        self.carrera = carrera
        self.semestre = semestre
        self.promedio = promedio
        self.NUA = NUA
    
    def info(self):
        persona.info(self)
        destreza.info(self)
        print('\nNUA: ', self.NUA,'  |  ','\nSemestre: ', self.semestre,'  |  ',
            '\nPromedio: ', self.promedio,'  |  ','\nCarrera: ', self.carrera)

class profesor(persona, destreza):
    def __init__(self, NUE, antiguedad, horasLab, grado = "DESCONOCIDO", *args, **kwargs):
        self.NUE = NUE
        self.antiguedad = antiguedad
        self.horasLab = horasLab
        self.grado = grado
        super(profesor, self).__init__(*args, **kwargs)
    
    def info(self):
        persona.info(self)
        destreza.info(self)
        print(
            "\nNUE: ", self.NUE,
            "\nAntigüedad: ", self.antiguedad,
            "\nHoras laboradas: ", self.horasLab,
            "\nGrado: ", self.grado
        )


alumno1 = alumno(427086, 8, 9.01, "Licenciatura en Física", "Uriel Chávez Flores", "Masculino", 21, "Aguascalientes, Aguascalientes", "POOyE", "Cosmología")

alumno1.info()

profesor1 = profesor(301580, 4, 15, "Maestría", "Eric Ruiz Flores", "Masculino", 24, "Aguascalientes, Aguascalientes", "Sistemas Lineales", "POOyE")

profesor1.info()