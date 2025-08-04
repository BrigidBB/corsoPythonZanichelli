#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 22:11:31 2025

@author: barbara
"""

print('quale animali preferisci')

voto=int(input('Digita 1 per GATTO o 2 per CANE, poi premi INVIO '))

if voto==1 or voto==2:
    if voto==1:
        print('vince il gatto)')
    else:
        print('vince il cane')
        
else:
    print('voto non valido; devi digitare o 1 o 2, cazzo!!!!')
