# -*- coding: utf-8 -*-

def fib(n): 
    a,b = 0,1 
    while b < n: 
        yield b 
        b,a = a+b, b 

#fib = [1,2]

#while fib[-1] < 4000000:
#    fib.append(fib[-1] + fib[-2])
    
print(sum([x for x in fib(4e6) if (x % 2 == 0)])) 
