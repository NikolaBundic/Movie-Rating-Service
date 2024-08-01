# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:28:36 2021

@author: nikola
"""

import umainmenu
import sys

def reg2():
    file = open("users.txt","r") 
    Counter = 1
    
    Content = file.read() 
    CoList = Content.split("\n") 
    
    for i in CoList: 
        if i: 
            Counter += 1
    
    name = input("Unesite ime: ")
    lastname = input("Unesite prezime: ")
    username = input("Unesite korisnicko ime: ")
    password = input("Unesite lozinku: ")
    
    
    file = open("users.txt","a")
    file.write("\n")
    file.write (name)
    file.write ("|")
    file.write (lastname)
    file.write ("|")
    file.write ("Admin")
    file.write ("|")
    file.write (str(Counter))
    file.write ("|")
    file.write (username)
    file.write ("|")
    file.write (password)
    file.close()

    print ("Novi admin je dodat.")
    amainmenu()

def novifilm():
    file = open("filmovi.txt","r") 
    Counter = 1
    
    Content = file.read() 
    CoList = Content.split("\n") 
    
    for i in CoList: 
        if i: 
            Counter += 1
    
    name = input("Unesite ime filma: ")
    godina = input("Unesite godinu: ")
    ocena = input("Unesite ocenu kritika: ")
    reziser = input("Unesite ime rezisera: ")
    
    
    file = open("filmovi.txt","a")
    file.write("\n")
    file.write (str(Counter))
    file.write ("|")
    file.write (name)
    file.write ("|")
    file.write (godina)
    file.write ("|")
    file.write (ocena)
    file.write ("|")
    file.write ("0")
    file.write ("|")
    file.write (reziser)
    file.close()

    print ("Film je uspesno dodat")
    amainmenu()
    
def novaserija():
    file = open("serije.txt","r") 
    Counter = 1
    
    Content = file.read() 
    CoList = Content.split("\n") 
    
    for i in CoList: 
        if i: 
            Counter += 1
    
    name = input("Unesite ime serije: ")
    godina = input("Unesite godinu: ")
    ocena = input("Unesite ocenu kritika: ")
    reziser = input("Unesite ime rezisera: ")
    
    
    file = open("serije.txt","a")
    file.write("\n")
    file.write (str(Counter))
    file.write ("|")
    file.write (name)
    file.write ("|")
    file.write (godina)
    file.write ("|")
    file.write (ocena)
    file.write ("|")
    file.write ("0")
    file.write ("|")
    file.write (reziser)
    file.close()

    print ("Serija je uspesno dodat")
    amainmenu()

def amainmenu():
    print("\n1. Unesite novi film")
    print("2. Unesite novu seriju")
    print("3. Dodajte novog admina")
    print("4. Predji u korisnicki meni")
    print("5. Ugasite program")
    
    x = 0
    while x<=0 or x>5:
        x = int(input("Unesite broj: "))
    if x == 1:
        novifilm()
    if x == 2:
        novaserija()
    if x == 3:
        reg2()
    if x == 4:
        umainmenu.umainmenu()
    if x == 5:
        sys.exit()