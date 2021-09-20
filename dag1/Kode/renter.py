# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:56:07 2021

@author: Kodeskolen
"""

# Erik setter inn 10 000 kr på BSU med 2.85 rente
# Hvor mye er det etter 10 år?

penger = 10000
rente = 1.0285
antall_år = 10

for år in range(1, antall_år+1):
    penger *= rente
    print(f"Etter {år:2} år er det {penger:.2f} kr")