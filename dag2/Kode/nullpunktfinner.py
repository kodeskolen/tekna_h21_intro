# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 19:25:57 2021

@author: Kodeskolen
"""
from pylab import log, sign
def f(x):
    return -((x/100)**5 - 0.1*log((x+1)/100) - 0.5)

def midtpunkt(a, b):
    return (a+b)/2

maks_tall = 100
min_tall = 0
maks_forsøk = 100
feilterskel = 0.000001

for forsøk in range(1, maks_forsøk+1):
    gjett = midtpunkt(min_tall, maks_tall)
    print(f"Jeg gjetter {gjett}!")
    print(f"f({gjett}) = {f(gjett)}")
    if abs(f(gjett)) < feilterskel:
        print("Jippi! Jeg er en flink maskin!")
        print(f"Jeg greide det på {forsøk} forsøk")
        break
    elif sign(f(gjett)) == sign(f(maks_tall)):
        maks_tall = gjett 
    else:
        min_tall = gjett

if abs(f(gjett)) >= feilterskel:
    print(f"Jeg brukte opp alle {maks_forsøk} forsøk")