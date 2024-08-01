# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 22:07:50 2021

@author: nikola
"""
import login2

def reg():
    file = open("users.txt","r") 
    Counter = 1
    
    Content = file.read() 
    CoList = Content.split("\n") 
    
    for i in CoList: 
        if i: 
            Counter += 1
    
    name = input("Unesite vase ime: ")
    lastname = input("Unesite vase prezime: ")
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    
    
    file = open("users.txt","a")
    file.write("\n")
    file.write (name)
    file.write ("|")
    file.write (lastname)
    file.write ("|")
    file.write ("User")
    file.write ("|")
    file.write (str(Counter))
    file.write ("|")
    file.write (username)
    file.write ("|")
    file.write (password)
    file.close()

    print ("Your login details have been saved. ")
    login2.check()