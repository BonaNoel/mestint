from keres import *

class Hanoi(Feladat):

    def __init__(self, k, c):
        self.kezdő = k
        self.cél = c


    def célteszt(self, allapot):
        return allapot == self.cél


    def rákövetkező(self, allapot):
        gyerek_cs = list()
        for melyiket in range(0, 3):
            for hova in  ["P", "Q", "R"]:
                flag = True # feltetelezem hogy a operátor alkalmazható
                # Az operátor alkalmazási előfeltételének ellenörzése
                if allapot[melyiket] != hova:
                    for i in range(0, melyiket):
                        if allapot[i] != allapot[melyiket] and allapot[i] != hova:
                            flag = True
                        else:
                            flag = False
                            break
                else:
                    flag = False

                if flag:
                    tmp = list(allapot)
                    tmp[melyiket] = hova
                    e = tuple(tmp)
                    gyerek_cs.append((""+str(melyiket)+"-->" +hova, e))

        return gyerek_cs



if __name__ == "__main__":
    ha = Hanoi(('P','P','P'),('Q','Q','Q'))
    print("Szélességi keresés")
    result = szélességi_fakeresés(ha)
    utam = result.út()
    utam.reverse()
    print(utam)

    print("Mélységi keresés")
    result = mélységi_fakeresés(ha)
    utam = result.út()
    utam.reverse()
    print(utam)