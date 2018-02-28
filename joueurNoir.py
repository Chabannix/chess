from pion import Pion

class joueurNoir:
    def __init__(self):
        print "init couleur"
        self.pion1 = Pion(1,7)
        self.pion2 = Pion(2,7)
        self.pion3 = Pion(3,7)
        self.pion4 = Pion(4,7)
        self.pion5 = Pion(5,7)
        self.pion6 = Pion(6,7)
        self.pion7 = Pion(7,7)
        self.pion8 = Pion(8,7)

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
