# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:08:53 2021

@author: Kodeskolen
"""

def midtpunkt(a, b):
    return (a+b)/2

maks_forsøk = 10
min_tall = 0
maks_tall = 100

print(f"Tenk på et tall mellom {min_tall} og {maks_tall}")

for forsøk in range(1, maks_forsøk + 1):
    gjett = int(midtpunkt(min_tall, maks_tall))
    print(f"Tenker du på {gjett}?")
    svar = input("Var dette for høyt, for lavt eller riktig?")
    if svar == "riktig":
        print(f"Jippi! Jeg klarte det på {forsøk} forsøk!")
        break
    elif svar == "for høyt":
        maks_tall = gjett
    elif svar == "for lavt":
        min_tall = gjett
    else:
        print("Jeg forstår ikke")
        print("svar 'for høyt', 'for lavt' eller 'riktig'")
    
    