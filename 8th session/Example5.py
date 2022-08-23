# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:52:35 2022

@author: Reza
"""

def decorator(func): 
    
    def inner1(*args, **kwargs):
        
        print("before execution")
        
        returned_value = func(*args, **kwargs)
        
        print("after execution")
        
        return returned_value
    
    return inner1 

@decorator
def sum_two_numbers(a,b):
    print("Inside the function")
    return a+b 


a,b = 1,2 
print(sum_two_numbers(a,b))
        
        