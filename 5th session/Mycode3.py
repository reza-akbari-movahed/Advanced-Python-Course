# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:37:13 2022

@author: Reza
"""

class Employee: 
    # Constructor
    def __init__(self, name, salary): 
        self.name = name  # Public data member 
        self.__salary = salary  # Private data member
        
    # A public method for displaying Private data member
    def show(self):
        print("Name: ",self.name,'\t', "Salary: ", self.__salary)
        
emp = Employee("Reza", 10000)
# accessing private data member using a public method 
emp.show()

print("Name: ", emp.name)
# direct access to private member using name mangling 
print("Salary: ", emp._Employee__salary)







        
        
