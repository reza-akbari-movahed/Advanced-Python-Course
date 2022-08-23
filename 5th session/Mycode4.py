# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:51:36 2022

@author: Reza
"""

# base class
class Company: 
    def __init__(self):
        self._project = "NLP" #Protected member 
        
# Child class 
class Employee(Company): 
    def __init__(self, name): 
        self.name = name 
        Company.__init__(self)
        
    def show(self): 
        print("Employee name: ", self.name)
        print("Working on project ", self._project)
        
c = Employee("Jessa")
c.show()

# Direct access to protected data members 
print("Project: ", c._project)

        

        
        