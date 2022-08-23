# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:05:08 2022

@author: Reza
"""

# defining a decarotor 
def hello_decarotor(func): 
    
    # inner1 is the wrapper function 
    def inner1(): 
        
        print("Hello, this is before function execution")
        
        func()
        
        print("This is after function execution")
        
    return inner1

# defining a function, to be called inside wrapper function
 
def function_to_be_used():
    print("This is inside the function !!")
    
function_to_be_used = hello_decarotor(function_to_be_used)
function_to_be_used()
    



