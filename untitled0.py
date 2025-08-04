#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 21:38:03 2025

@author: barbara
"""

nome='Babi'
psico='e sono deficiente'
#print('Hello world, mi chiamo',nome,psico)
#print(nome, 'è un dato di tipo', type(nome))

#massa=float(input('inserisci il valore della massa in kg\n senza unità di misura'))
#volume=float(input('inserisci il valore del volume in metricubi'))
#calcolo la densità del materiale
#print('la densità del materiale è',massa/volume,'kg/m^3')
a=7.8
print(int(a))


#sui formati e gli arrotondamenti ----> IMPORTANTE in fisica
a=3
b=4


#print('numero non formattato', a/b)
print('ARROTONDATO a una cifra decimale',format(a/b,'.1f'))
print('ARROTONDATO a due cifre decimali',format(a/b,'.2f'))
print('ARROTONDATO a tre cifre decimali',format(a/b,'.3f'))
print('come se fosse una percentuale',format(a/b,'.1%'))

c=0.735
print('ARROTONDATO a una cifra decimale',format(c,'.1f'))
print('ARROTONDATO a due cifre decimali',format(c,'.2f'))


print(4/3)
print(4%3)
