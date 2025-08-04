#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 22:29:40 2025

@author: barbara
"""

eta=int(input('quanti anni hai? Digita la tua età in mumeri, poi premi INVIO '))

patente=input('digita S o s, se hai la patente, altrimenti N o n e premi INVIO: ')

if eta<18 and patente=='N' or patente=='n':
    print('non puoi guidare la macchina, sei fuori?')

elif eta<18 and patente=='s' or patente=='S':
    print('torna quando avrai l'' età giusta')

elif eta>18 and patente=='S' or patente=='s':
    print('puoi noleggiare l'' auto, ma non bere')
    
else: 
    print('c' 'è qualcosa che non va, leggi bene le istruzioni, comunque io l'' auto non te la darei')
