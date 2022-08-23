# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:31:23 2022

@author: Reza
"""

"""
find out the exexution time of a function using a decorator
"""

import time
import math

def calculate_time(func): 
    
    def inner1(*args, **kwargs):
        
        begin = time.time()
        
        func(*args, **kwargs)
        
        end = time.time() 
        
        print("Total time taken in: ", func.__name__, end-begin)
        
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))
    
factorial(10)
    


# def factorial(num):
#     time.sleep(2)
#     print(math.factorial(num))
    
# mt_factorial = calculate_time(factorial)
# mt_factorial(5)

        
        
        
        