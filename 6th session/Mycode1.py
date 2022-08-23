# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:56:34 2022

@author: Reza
"""
# x = 10 
# try:
#     print(x)
# except:
#     print("An exception occured")

#x = ["Reza",True,9+4j,20.54]
# try: 
#     print(x)
# except: 
#     print("Something else went wrong")
# finally: 
#     print("The 'try except' is finished")
    
# """ Try to open and write to a file that is not writable"""

try:
    f = open("demofile.txt",'w')
    try:
        f.write("Hello from Advanced AI channel")
    except: 
        print("Something went wrong when writing to the file")
    finally:
        f.close()   
except: 
    print("Something went wrong when opening the file")
