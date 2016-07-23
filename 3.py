# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:37:11 2016

@author: robbie
"""
import lib

n = 600851475143
i = 0

for i in lib.primes(999):
    modu = n % i
    print(str(i) + ' ' + str(modu))
    if modu == 0:
        print(i)
        quit()
        