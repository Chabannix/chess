import sys
sys.path.insert(0, "/home/damien/Documents/chess/piece/")
import pion


class joueurNoir:
    def __init__(self):
        self.pion1 = pion.Pion(1,7)
        self.pion2 = pion.Pion(2,7)
        self.pion3 = pion.Pion(3,7)
        self.pion4 = pion.Pion(4,7)
        self.pion5 = pion.Pion(5,7)
        self.pion6 = pion.Pion(6,7)
        self.pion7 = pion.Pion(7,7)
        self.pion8 = pion.Pion(8,7)

        self.tour1 = 1 
        self.tour2 = 1

        self.cavalier1 = 1
        self.cavalier2 = 1
        
        self.fou1 = 1 
        self.fou2 = 1
        
        self.dame = 1
        self.roi = 1

    def showStatus(self):
        print "alive !"
