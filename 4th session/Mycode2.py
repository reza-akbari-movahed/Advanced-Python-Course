# -*- coding: utf-8 -*-
"""
Created on Sun May  1 19:26:14 2022

@author: Reza
"""

#parent class 
class Person(object):
    def __init__(self, name, idnumber):
        self.name = name 
        self.idnumber = idnumber 
        
    def display(self):
        print(self.name)
        print(self.idnumber)
        
    def details(self):
        print("My name is {}".format(self.name))
        print("Id Number: {}".format(self.idnumber))
        
# Child class 
class Employee(Person): 
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary 
        self.post = post
        
        #invoking the __init__ of the parent class 
        Person.__init__(self, name, idnumber)
        
    def details(self):
        Person.details(self)
        print("Post: {}".format(self.post))
        
# creation of an object 
a = Employee("Reza", "987", 886012, "Intern")

a.details()
a.display()

        
        
        
        
        
        

