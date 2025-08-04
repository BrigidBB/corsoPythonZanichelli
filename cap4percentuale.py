#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  9 23:25:06 2025

@author: barbara
"""
numero1=float(input('scrivi un numero positivo'))
numero2=float(input('scrivi un altro numero positivo'))
if numero1>numero2:
    print(numero2, ' è ',numero2*100/numero1, '% di', numero1)
else:
    print(numero1, ' è ',numero1*100/numero2, '% di', numero2)
