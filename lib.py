# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 06:37:29 2016

@author: robbie
"""

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]
    

def prime_factors(n, num_primes = 999):
    i = 0
    factor_list = []
    for i in primes(num_primes):
        modu = n % i
        if modu == 0:
            factor_list.append(i) 
            factor_list += prime_factors(n/i,num_primes)
            break
    return factor_list
            