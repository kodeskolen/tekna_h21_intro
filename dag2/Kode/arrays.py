# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:05:55 2021

@author: Kodeskolen
"""

from pylab import arange, sqrt

x = arange(1, 11)
print(x)
y = x ** 2
print(y)
z = sqrt(x)
print(z)

def kvadrer(x):
    return x**2
w = kvadrer(x)
print(w)