# -*- coding: utf-8 -*-
#Rechner
#20.02.2012 13:32:03
#Jonarhan Wendler
#ein test von isaak

from math import sqrt
print "******************************"
print "*T A S C H E N R E C H N E R*"
print "*                 v1.0                   *"
print "******************************"
print "\n"+"von Jonathan Wendler"
print "\n\n"
not_exit=1
while (not_exit==1):
    print "Wähle :"
    print "(A)ddieren, (S)ubtrahieren, (M)ultiplizieren, (D)ividieren,(W)urzel"
    print "(B)eenden:",
    Art=raw_input()
    if (Art=="A"):
        print "Zahl 1:",
        Z1 = input()
        print "Zahl 2:",
        Z2 = input()
        print "Ergebniss: "+str(Z1)+"+"+str(Z2)+"="+str(Z1+Z2)
    elif (Art=="S"):
        print "Zahl 1:",
        Z1 = input()
        print "Zahl 2:",
        Z2 = input()
        print "Ergebniss: "+str(Z1)+"-"+str(Z2)+"="+str(Z1-Z2)
    elif (Art=="M"):
        print "Zahl 1:",
        Z1 = input()
        print "Zahl 2:",
        Z2 = input()
        print "Ergebniss: "+str(Z1)+"*"+str(Z2)+"="+str(Z1*Z2)
    elif (Art=="D"):
        print "Zahl 1:",
        Z1 = input()
        print "Zahl 2:",
        Z2 = input()
        print "Ergebniss: "+str(Z1)+":"+str(Z2)+"="+str(Z1/Z2)
    elif (Art=="W"):
        print "Zahl:",
        Z1 = input()
        print "Ergebniss: "+"Wurzel("+str(Z1)+")="+str(sqrt(Z1))
    elif (Art=="B"):
        not_exit=0
    else:
        print "Falsches Zeichen"

