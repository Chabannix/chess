class Pion:
    def __init__(self, x, y):
        self.position = [x,y]
        self.status = "vivant"
        
    def mouvement(self, x0, x1, y0, y1):
	print "debut mouvemtn"
	print x0
	print x1
	print y0
	print y1

	if x0 == x1 and y1-y0 == 1:
	    return 1
	else:
	    return 0
