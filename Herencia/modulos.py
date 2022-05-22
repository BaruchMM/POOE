import models

def datosPersona():
    nombre = input('Nombre completo: ')
    sexo = input('Sexo: ') 
    edad = input('Edad: ') 
    nacimiento = input('Lugar de nacimiento: ')
    return [nombre, sexo, edad, nacimiento]

def datosTrabajo():
     pago = input('Ingrese el sueldo bruto: ') 
     area = input('Ingrese el área o departamento: ') 
     horas = input('Ingrese las horas de trabajo por semana:')
     return [pago,area,horas]

def datosEstudiante():
    NUA = input('NUA: ')
    semestre = input('Semestre en curso: ')
    promedio = input('Promedio inmediato anterior: ')
    carrera = input('Carrera: ')
    mejorMat = input('Materia con mejor rendimiento: ')
    peorMat = input('Materia con peor rendimiento: ')
    return [mejorMat, peorMat,carrera, semestre, promedio, NUA]

def guardarAlumno(al,path):
    res = (al.nombre + '\t' + al.sexo + '\t' + al.edad +
            '\t' + al.nacimiento + '\t' + al.mejorMateria + '\t' + al.peorMateria + 
            '\t' + al.carrera + '\t' + al.semestre + '\t' + al.promedio + '\t' + al.NUA)
    f = open(path,'a')
    f.write('\n'+res)
    f.close

def createStudent():
    datos = datosPersona()
    datos += datosEstudiante()
    student = models.alumno(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9])
    student.conslulta()
    path = '/home/baruch/Documentos/GitHub/POOE/Herencia/datosAl.txt'
    guardarAlumno(student,path)

def datosProfesor():
    mejorMateria = input('Materia con mejor rendimiento: ') 
    peorMateria = input('Materia con peor rendimiento: ')
    NUE = input('NUE: ') 
    antiguedad = input('Antigüedad: ')
    grado = input('Grado académico: ')
    return [mejorMateria, peorMateria, NUE, antiguedad, grado]

#profesor(nombre, sexo, edad, nacimiento, mejorMateria, peorMateria, NUE, antiguedad, grado, pago, area, horas)
def guardarProf(per,path):
    res = (per.nombre + '\t' + per.sexo + '\t' + per.edad + '\t' + per.nacimiento + 
            '\t' + per.mejorMateria + '\t' + per.peorMateria + '\t' + per.NUE + '\t' + 
            per.antiguedad + '\t' + per.grado + '\t' + per.pago + '\t' + per.area + '\t' + per.horas )
    f = open(path,'a')
    f.write('\n'+res)
    f.close

def createTeacher():
    datos = datosPersona()
    datos += datosProfesor()
    datos += datosTrabajo()
    print(datos)
    teacher = models.profesor(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8],datos[9],datos[10],datos[11])
    teacher.conslulta()
    path = '/home/baruch/Documentos/GitHub/POOE/Herencia/datosProf.txt'
    guardarProf(teacher,path)


