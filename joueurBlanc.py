import sys
sys.path.insert(0, "/home/damien/Documents/chess/piece/")
import pion

class joueurBlanc:
    def __init__(self):
        self.pion1 = pion.Pion(1,2)
        self.pion2 = pion.Pion(2,2)
        self.pion3 = pion.Pion(3,2)
        self.pion4 = pion.Pion(4,2)
        self.pion5 = pion.Pion(5,2)
        self.pion6 = pion.Pion(6,2)
        self.pion7 = pion.Pion(7,2)
        self.pion8 = pion.Pion(8,2)

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
