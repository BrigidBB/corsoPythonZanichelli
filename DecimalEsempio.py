#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 10:16:26 2025

@author: barbara
"""

from decimal import * # fondamentale per utilizzare Decimal, significa "dal file 'decimal' importa tutto"


"""
Cos'è getcontext? getcontext è una funzione che dice al programma come utilizzare i Decimal

print(getcontext())

Ciò che viene stampato su console:

Context(
        prec=28, // cifre significative del risultato di un'operazione generica'
        rounding=ROUND_HALF_EVEN, // come vengono arontondati i numeri Decimal
        Emin=-999999, // l'esponente massimo che un Decimal può memorizzare
        Emax=999999, // l'esponente minimo che un Decimal può memorizare
        capitals=1, // per la scrittura in notazione scientifica: 1 per utilizzare 'E', 0 per utilizzare 'e'
        clamp=0, // per la scrittura in notazione scientifica: clamp=0 non cambia niente, clamp=1 scrive Emax o Emin al posto dell'esponente se questo non rientra nell'intervallo [Emin; Emax] (evita scritture tipo Infinity o Nan)
        flags=[], // è la lista di cose che succedono al numero: se viene arrotondato, se viene troncato ecc.
        traps=[InvalidOperation, DivisionByZero, Overflow] // dà errore se una di queste cose succede
        )
"""

# ---ESEMPI---

# Ricordati di inserire questa riga all'inizio del programma: from decimal import *


# Come arrotondo un Decimal?

getcontext().rounding = ROUND_HALF_UP # Dico al programma di arrotondare per eccesso

stringa_numerica = '0.735'

nuovo_decimale = Decimal(stringa_numerica)

decimale_arrotondato = nuovo_decimale.quantize(Decimal('0.01')) # Con Decimal('0.01') gli dico di arrotondare il numero a 2 cifre decimali

print("Decimal('0.375') arrotondato a 2 cifre decimali: ", decimale_arrotondato)



# Decimal conserva le cifre significative?

print("Decimal('12.000'): ", Decimal('12.000'))



# Come si fanno le operazioni tra Decimal?

getcontext().prec = 100 # Voglio che il risultato di un'operazione sia preciso, così salvo massimo 100 cifre significative dopo un'operazione

risultato = Decimal('0.375') * Decimal('5')

print("Risultato (con massimo 100 cifre significative)", risultato)
