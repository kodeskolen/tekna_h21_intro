# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:35:59 2021

@author: Kodeskolen
"""

def maks(tall1, tall2):
    if tall1 > tall2:
        størst = tall1
    else:
        størst = tall2
    return størst

print(maks(1, 3))