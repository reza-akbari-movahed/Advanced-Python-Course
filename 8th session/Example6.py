# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 21:08:34 2022

@author: Reza
"""

# Chaining Decorators
def decor1(func):
    def inner():
        x = func()
        return x * x 
    return inner 

def decor(func): 
    def inner():
        x = func()
        return 2*x 
    return inner

@decor1
@decor
def num(): 
    return 10 


print(num())



    
    

