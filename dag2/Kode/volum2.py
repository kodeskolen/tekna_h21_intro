# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 17:25:16 2021

@author: Kodeskolen
"""

pi = 3.14

radius_klinkekule = 1 #cm
radius_tennisball = 2.5 #cm
radius_bowlingball = 7 #cm

def kulevolum(radius):
    return (4/3)*pi*radius**3

volum_klinkekule = kulevolum(radius_klinkekule)
volum_tennisball = kulevolum(radius_tennisball)
volum_bowlingball = kulevolum(radius_bowlingball)