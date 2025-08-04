#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 23:11:00 2025

@author: barbara
"""

num=(input('scrivi un numero qualunque, anche negativo, e premi INVIO: '))

numero=float(num)

if numero<0.0 or numero>0.0:
    
    if numero<0.0:
        print(numero, 'è negativo')
    
    else:
        print(numero, 'è positivo')
        
else:
    print('hai scritto zero')