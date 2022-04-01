class archivos:
    def _init_(self,path,fileName):
        self.path = path
        self.fileNme = fileName
    def leerArchivo(self,path,fileName):
        usuarios = {}
        with open(path + fileName, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(":")
                usuarios[line[0]] = line[1]
        return usuarios