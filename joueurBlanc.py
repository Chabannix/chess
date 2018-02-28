from pion import Pion

class joueurBlanc:
    def __init__(self):
        print "init couleur"
        self.pion1 = Pion(1,2)
        self.pion2 = Pion(2,2)
        self.pion3 = Pion(3,2)
        self.pion4 = Pion(4,2)
        self.pion5 = Pion(5,2)
        self.pion6 = Pion(6,2)
        self.pion7 = Pion(7,2)
        self.pion8 = Pion(8,2)

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
