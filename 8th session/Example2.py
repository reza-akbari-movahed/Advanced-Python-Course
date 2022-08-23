# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:38:58 2022

@author: Reza
"""

def shout(text): 
    return text.upper()

def whisper(text): 
    return text.lower()

def greet(func): 
    greeting = func("Hi, Iam created by a function passed as an argument")
    print(greeting)
    
greet(shout)
greet(whisper)


def create_adder(x): 
    def adder(y):
        return x+y
    
    return adder 

add_15 = create_adder(15)
print(add_15(10))


   

