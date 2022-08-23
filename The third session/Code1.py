# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 20:04:49 2022

@author: Reza
"""

def greet(name):
    return "Hello, {}".format(name)

def print_greeting(f,n):
    print(f(n))
    
print_greeting(greet,"Reza")

def F1(a):
    return a*a 

tup1 = list(map(F1,(1,2,3,4)))

list1 = [5 , 7, 22 , 97, 54, 62 ,30 ,12]
newlist = list((lambda x:x+3,list1))
print(newlist)

Tempreture_cent = (12,14,-4)
Tempreture_Kel = tuple(map(lambda x:x+273, Tempreture_cent))
print(Tempreture_Kel)

def func(x):
    if x>=3:
        return x 

y = list(filter(func, [1,2,3,4]))
print(y)

y1 = list(filter(lambda x:(x>=3), (1,2,3,4)))
print(y1)
