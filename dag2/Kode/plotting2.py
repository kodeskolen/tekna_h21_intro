# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 18:30:11 2021

@author: Kodeskolen
"""

from pylab import sin, arange, plot, show, xlabel, ylabel, xlim, title, cos

x = arange(0, 8, 0.1)
y = sin(x)
z = cos(x)

print(x)
print(y)

plot(x, y)
plot(x, z)
xlim(0, 7.9)
xlabel("Tid")
ylabel("Høyde")
title("Posisjon til pendel som funksjon av tid")
show()