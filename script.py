#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import partie
import re

def parseCoup(str):
    
    ret = re.match("^[PTCFDR][a-h][1-8][\ ][a-h][1-8]", str)
    
    if ret == None:
        print"Erreur : taper un coup valide"
        return 0

    elif str[0] == 'P':
        if str[1] != str[4]:
            print"Erreur : un pion ne bouge qu'en ligne droite, taper un coup valide"
            return 0
        elif int(str[5]) - int(str[2]) != 1:
            print"Erreur : un pion ne peut avancer que d'une case, taper un coup valide"
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
