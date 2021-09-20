# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:31:49 2021

@author: Kodeskolen
"""

# Vi skal lage en gjettelek
# Vi tenker på et tall mellom 0 og 100
# Brukeren får 10 forsøk 
# For hvert forsøk skal brukeren gjette et tall
# Vi sier ifra om tallet er rikig, for stort eller for lite
# Dersom antall forsøk er brukt opp er spillet over og brukeren har tapt

fasit = 37
maks_forsøk = 10

for forsøk in range(1, maks_forsøk + 1):
    print(f"Forsøk nr. {forsøk}")
    gjett = int(input("Gjett et tall mellom 0 og 100:"))
    if gjett == fasit:
        print("Du klarte det :D")
        break
    elif gjett > fasit:
        print("Det er for høyt!")
    else:
        print("Det er for lavt!")
if gjett != fasit:
    print(f"Du har brukt opp dine {maks_forsøk} forsøk.")
    print("GAME OVER :(")
    
    