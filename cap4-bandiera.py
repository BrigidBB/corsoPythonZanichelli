#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 22:29:45 2025

@author: barbara
"""

colore=str(input('scrivi un colore: '))
# Alternativa a riga 12
# if(colore in ['verde', 'rosso', 'bianco']):
if (colore=='verde'or colore=='rosso'or colore=='bianco'):
    print(colore, 'appartiene alla bandiera italiana')
else:
    print(colore,'non appartiene alla bandiera italiana')