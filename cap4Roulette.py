#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 22:18:23 2025

@author: barbara
"""

print('inserisci il risultato del lancio')

lancio=input('R rosso, N nero oppure Z zero : ')

if lancio=='R':
    print('è uscito il rosso')
    
elif lancio =='N':
    print('è uscito il nero')
    
elif lancio =='Z':
    print('è uscito lo zero')
    
else:
    print('input non valido, leggi bene')