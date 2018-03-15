#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import partie
import re
import sys
sys.path.insert(0, "/home/damien/Documents/chess/piece/")
import pion

def map(str):
    print "debut de map"
    print str
    if   str == 'a' or str == '0':
	return 0

    elif str == 'b' or str == '1':
	return 1

    elif str == 'c' or str == '2':
	return 2

    elif str == 'd' or str == '3':
	return 3

    elif str == 'e' or str == '4':
	return 4

    elif str == 'f' or str == '5':
	return 5

    elif str == 'g' or str == '6':
	return 6

    elif str == 'h' or str == '7':
	return 7
   
    else:
	return -1


def parseCoup(str):
    
    ret = re.match("^[PTCFDR][a-h][1-8][\ ][a-h][1-8]", str)
    
    if ret == None:
        print"Erreur : taper un coup valide"
        return 0

    elif str[0] == 'P':
	x0 = map(str[1])
	x1 = map(str[4])
	y0 = map(str[2])
	y1 = map(str[5])

	monPion = pion.Pion(x0, y0)
	if monPion.mouvement(x0, x1, y0, y1) == 0:
	    print "mouvement impossible pour cette piece"
	    return 0
		
    else:
        ma_partie.echequier[1][1].statut = "occupe"
        return 1


print "***********************************"
print "**********    chess    ************"
print "***********************************"

partie_en_cours = 1
ma_partie = partie.Partie()
    
print ma_partie
while partie_en_cours:
    ret = 0
    print"\n-- Joueur blanc : à vous de jouer --"
    while ret == 0:
        coup_joueur = raw_input()
        ret = parseCoup(coup_joueur)
    
    ret = 0
    print"\n-- Joueur noir : à vous de jouer --"
    while ret == 0:
        coup_joueur = raw_input()
        ret = parseCoup(coup_joueur)
