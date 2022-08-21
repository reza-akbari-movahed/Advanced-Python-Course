# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 19:15:56 2022

@author: Reza
"""

def shout(text): 
    return text.upper()

def return_size(text): 
    txt = "The length of the input string is {}".format(len(text))
    return txt

print(shout("Hello"))

yell = shout

print(yell("Reza"))

print(return_size("Advanced AI"))

List_of_functions = [shout, return_size]
print(List_of_functions[1]("Hello from Advanced AI channel"))






