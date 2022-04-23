from sqlalchemy import null
import star as ST

def readData():
    data = []
    path = 'C:/Users/baruc/OneDrive - Universidad de Guanajuato/Documentos/Tareas UG/POOE/Stars_Clasification/'
    with open(path + 'data.txt', 'r') as dataShop:
        for line in dataShop:
            line = line.strip()
            line = line.split()
            data.append(line)
    return  data

def getStars( UVMag, blueMag,  AbsMag, type):
    stars = ST.star( UVMag, blueMag,  AbsMag, type)
    return stars

def Stars():
    data = readData()
    stars = {}
    for i in range(1,len(data)):
        star = null
        star = getStars(data[i][0],data[i][1],data[i][2],ST.star.typeStar(float(data[i][1]),float(data[i][2])))
        stars[i] = star
    return stars

def seeStars(stars):
    print('ID     \t UV Magnitude:\t \t Blue Magnitude: \t Absolute Mag: \t\t Type:')
    for n in stars.keys():
        
        print(str(n)+'\t|\t'+str(stars[n].UVMag)+'\t\t|\t'+str(stars[n].blueMag)+'\t\t|\t'+str(stars[n].AbsMag)+'\t\t|\t'+str(stars[n].typeStar))