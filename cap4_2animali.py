#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 22:58:27 2025

@author: barbara
"""

print('quale animale preferisci?')
voto=int(input('digita 1 per il GATTO oppure 2 per il CANE '))
if voto!=1:
    if voto!=2:
        print('ti ho chiesto due cazzo di numeri, sei un deficiente: scrivi 1 o 2!!!!!!') 
    else:
        print('vince il cane')
else:
    print('vince il gatto')