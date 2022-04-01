class archivos:
    def __init__(self,path,fileName):
        self.path = path
        self.fileName = fileName

    def readData(self):
        usuarios = {}
        with open(self.path + self.fileName, "r") as file:
            for line in file:
                line = line.strip()
                line = line.split(":")
                usuarios[line[0]] = line[1]
        return usuarios
    def readText(self):
        text = open(self.path + self.fileName, encoding="utf8") 
        return text
