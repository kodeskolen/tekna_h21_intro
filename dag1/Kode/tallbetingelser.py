# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:11:29 2021

@author: Kodeskolen
"""

tall = float(input("Skriv inn et tall: "))

if tall > 0:
    print("Tallet er positivt")
elif tall < 0:
    print("Tallet er negativt")
else:
    print("Tallet er null")