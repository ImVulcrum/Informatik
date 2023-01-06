# Author: Deine Mom
import sys
rot = 0
blau = 1
gelb = 2
grün = 3
Würfel_3 = [rot, grün, rot, grün, blau, gelb] 
Würfel_2 = [rot, gelb, grün, gelb, rot, blau]
Würfel_1 = [grün, grün, rot, gelb, blau, blau]
Würfel_4 = [gelb, gelb, grün, blau, gelb, rot]
Turm = [Würfel_1, Würfel_2, Würfel_3, Würfel_4]
def rotateRight(Würfel):
    temp_5 = Würfel[5]
    temp_2 = Würfel[2]
    temp_3 = Würfel[3]
    temp_4 = Würfel[4]
    Würfel[5] = temp_2
    Würfel[2] = temp_3
    Würfel[3] = temp_4
    Würfel[4] = temp_5
    return Würfel

def rotateUp(Würfel):
    temp_0 = Würfel[0]
    temp_2 = Würfel[2]
    temp_1 = Würfel[1]
    temp_4 = Würfel[4]
    Würfel[2] = temp_0
    Würfel[1] = temp_2
    Würfel[0] = temp_4
    Würfel[4] = temp_1
    return Würfel
def check(Tower):
    count = 0
    for i in range(2, 6):
        liste = [Tower[0][i], Tower[1][i], Tower[2][i], Tower[3][i]]
        if len(liste) == len(set(liste)):
            count += 1
    if count == 4:
        return True
    return False
befehle = [rotateUp, rotateUp, rotateUp, rotateUp, rotateRight, rotateUp, rotateUp, rotateUp, rotateUp, rotateRight, rotateUp, rotateUp, rotateUp, rotateUp, rotateRight, rotateUp, rotateUp, rotateUp, rotateUp, rotateRight, rotateUp, rotateRight, rotateRight, rotateRight, rotateRight,  rotateUp, rotateRight, rotateRight, rotateRight, rotateRight]
count = 0
# wahrscheinlich der innefiz8ienteste weg aber egal
for i in range(len(befehle)):
    Würfel_1 = befehle[i](Würfel_1)
    for j in range(len(befehle)):
        Würfel_2 = befehle[j](Würfel_2)
        for k in range(len(befehle)):
            Würfel_3 = befehle[k](Würfel_3)
            for l in range(len(befehle)):
                Würfel_4 = befehle[l](Würfel_4)
                count += 1
                if check(Turm):
                    for q in range(len(Turm)):
                        for a in range(len(Turm[q])):
                            if Turm[q][a] == 0:
                                Turm[q][a] = "rot"
                            if Turm[q][a] == 1:
                                Turm[q][a] = "blau"
                            if Turm[q][a] == 2:
                                Turm[q][a] = "gelb"
                            if Turm[q][a] == 3:
                                Turm[q][a] = "grün"
                    print(f"{Turm=}")
                    print("IT WORKED")
                    print(f"{Würfel_1=},\n{Würfel_2=},\n{Würfel_3=},\n{Würfel_4=}")
                    print("count =", count)
                    sys.exit()







