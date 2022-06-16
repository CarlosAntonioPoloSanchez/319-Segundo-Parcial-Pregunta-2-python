# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fibonacci(b): 
    z = "0, 1, "
    x = 0
    y = 1
    for i in range (b-2):
        c= x+y
        z=z+calc(conc,str(c))
        x=y
        y=c
    return z
conc = lambda a="": a+", "
calc = lambda funcion,  a="": funcion(a)
print ("insertar un numero")
a=int(input())
print(calc(conc,str(a)))
print(fibonacci(a))
