from sqlalchemy import null
import pandas as pd
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

def groupStars(stars):
    groups = {'O5': 0,'BO':0,'B5':0,'AO':0,'A5':0,'F0':0,'F5':0,'GO':0,'G5':0,'KO':0,'K5':0,'MO':0,'M5':0,'M8':0}
    for n in stars.keys():
        if (stars[n].typeStar == 'O5'):
            groups['O5'] += 1
        elif (stars[n].typeStar == 'BO'):
            groups['BO']
        elif (stars[n].typeStar == 'B5'):
            groups['B5'] += 1
        elif (stars[n].typeStar == 'AO'):
            groups['AO'] += 1
        elif (stars[n].typeStar == 'A5'):
            groups['A5'] += 1
        elif (stars[n].typeStar == 'F0'):
            groups['F0'] += 1
        elif (stars[n].typeStar == 'F5'):
            groups['F5'] += 1
        elif (stars[n].typeStar == 'GO'):
            groups['GO'] += 1
        elif (stars[n].typeStar == 'G5'):
            groups['G5'] += 1
        elif (stars[n].typeStar == 'KO'):
            groups['KO'] += 1
        elif (stars[n].typeStar == 'K5'):
            groups['K5'] += 1
        elif (stars[n].typeStar == 'MO'):
            groups['MO'] += 1
        elif (stars[n].typeStar == 'M5'):
            ['M5']
        else:
            groups['M8'] += 1
    print(groups)
    return groups

def biuldDataFrame(stars,groups):
    magnitudes = []
    starstypes = []
    for n in stars.keys():
        magnitudes.append(stars[n].AbsMag)
        starstypes.append(stars[n].typeStar)
    df = pd.DataFrame(magnitudes,starstypes)
    print(df)
    return df
def Hertzsprung_Russell_Diagram():
    print('s')