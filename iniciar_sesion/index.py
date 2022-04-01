import libs

leer = libs.archivos()

usuarios = leer.leerArchivo('/home/baruch/Documentos/POOE/iniciar_sesion/usuarions.txt','usuarios.txt')
print(usuarios)
