# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:04:34 2022

@author: Reza
"""

class Dog:
    
    attr1 = "Mammal"
    
    def __init__(self, name): 
        self.name = name
        
    def spaek(self):
        print("My name is {}".format(self.name))
              
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger.spaek()
