from keres import *


class Kancso(Feladat):

    def __init__(self, k, c):
        self.kezdő = k
        self.cél = c
        self.M1 = 3
        self.M2 = 5
        self.M3 = 8

    def célteszt(self, allapot):
        return allapot[0] == self.cél or allapot[1] == self.cél or allapot[2] == self.cél

    def rákövetkező(self, allapot):
        gyerek_csomopontok = list()
        a1, a2, a3 = allapot
        #tolt 1,2
        if(a1 != 0 and a2 != self.M2):
            T = min([a1, self.M2 - a2])
            gyerek_csomopontok.append(("a1-bol a2-be" ,(a1 - T, a2 + T, a3)))
        #tolt 1,3
        if(a1 != 0 and a3 != self.M3):
            T = min([a1, self.M3 - a3])
            gyerek_csomopontok.append(("a1-bol a3-be" ,(a1 - T, a2, a3 + T)))
        #tolt 2,1
        if(a2 != 0 and a1 != self.M1):
            T = min([a2, self.M1 - a1])
            gyerek_csomopontok.append(("a2-bol a1-be" ,(a1 + T, a2 - T, a3)))
        #tolt 2,3
        if(a2 != 0 and a3 != self.M3):
            T = min([a2, self.M3 - a3])
            gyerek_csomopontok.append(("a2-bol a3-be" ,(a1, a2 - T, a3 + T)))
        #tolt 3,1
        if(a3 != 0 and a1 != self.M1):
            T = min([a3, self.M1 - a1])
            gyerek_csomopontok.append(("a3-bol a1-be" ,(a1 + T, a2, a3 - T)))
        #tolt 3,2
        if(a3 != 0 and a2 != self.M2):
            T = min([a3, self.M2 - a2])
            gyerek_csomopontok.append(("a3-bol a2-be" ,(a1, a2 + T, a3 - T)))

        return gyerek_csomopontok

if __name__ == "__main__":
    korso = Kancso((0,0,8),4)
    print("Szélességi keresés")
    result = szélességi_fakeresés(korso)
    utam = result.út()
    utam.reverse()
    print(utam)

    print("Mélységi keresés")
    result = mélységi_fakeresés(korso)
    utam = result.út()
    utam.reverse()
    print(utam)