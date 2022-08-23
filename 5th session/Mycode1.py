# -*- coding: utf-8 -*-
"""
Created on Sun May 15 08:59:50 2022

@author: Reza
"""

class India():
    def capital(self):
        print("New Delhi is the capital of India")
        
    def language(self):
        print("Hindi is the most widely spoken language of India")
        
    def type(self):
        print("India is a developing country.")
        
class USA(): 
    def capital(self):
        print("Washington, D.C. is the capital of USA")
        
    def language(self):
        print("English is the primary language of USA")
        
    def type(self): 
        print("USA is a developed country.")
        
obj_ind = India() 
obj_usa = USA()

for counrty in (obj_ind,obj_usa):
    counrty.capital()
    counrty.language()
    counrty.type()
    print("------------")
    
def func(obj): 
    obj.capital()
    obj.language()
    obj.type()

func(obj_ind)
func(obj_usa)
