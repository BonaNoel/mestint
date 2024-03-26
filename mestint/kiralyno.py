from keres import *

class Kiralyno(Feladat):


    def __init__(self, k, c):
        self.kezdő = k
        self.cél = c
        self.N = 8


    def célteszt(self, allapot):
        return allapot[self.N] == self.cél


    def rákövetkező(self, allapot):
        gyerek_cs = list()

        s = allapot[self.N]

        for i in range(0,self.N):
            flag = True
            # az operator alkalmazasi elofeltetele
            for m in range(0, s):
                if allapot[m] != i and abs(m - s) != abs(allapot[m] - i):
                    flag = True
                else:
                    flag = False
                    break

            # az operator alkalmazasi fuggvenye
            if flag:
                tmp = list(allapot)
                tmp[s] = i
                tmp[self.N] = tmp[self.N] + 1
                result = tuple(tmp)

                gyerek_cs.append(("lerak(" + str(s) + "," + str(i) + ")", result))

        return gyerek_cs



if __name__ == "__main__":
    kiralyno = Kiralyno((-1, -1, -1, -1, -1, -1, -1, -1, 0), 8)

    print("Szélességi keresés")
    result = szélességi_fakeresés(kiralyno)
    utam = result.út()
    utam.reverse()
    print(utam)

    print("Mélységi keresés")
    result = mélységi_fakeresés(kiralyno)
    utam = result.út()
    utam.reverse()
    print(utam)
