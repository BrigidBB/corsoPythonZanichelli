#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 21:43:19 2025

@author: barbara
"""

cell=float(input('inserisci il prezzo del cell'))
cover=float(input('inserisci il prezzo della cover'))
auri=float(input('inserisci il prezzo degli auricolari'))
budget=float(input('inserisci quanti soldi hai'))
prezzo=cell+cover+auri

if(prezzo>budget):
    print('budget superato di',prezzo-budget,'euro')
else:     
    print('il costo totale è pari a',prezzo,'euro')
      