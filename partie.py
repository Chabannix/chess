from joueurNoir import joueurNoir
from joueurBlanc import joueurBlanc
from case import Case

class Partie:

    def __init__(self):
        print "init"
        self.joueurNoir = joueurNoir()
        self.joueurBlanc = joueurBlanc()
        x = []
        for i in range(0,8):
            y = []
            for j in range(0,8):
                case = Case()
                y.append(case)
                x.append(y)
        self.echequier = x
