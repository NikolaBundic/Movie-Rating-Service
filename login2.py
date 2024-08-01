# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 21:54:31 2021

@author: nikola
"""
import register
import amainmenu
import umainmenu

def check():
    
    global userg
    global role
    users = open("users.txt").read().split("\n")
    for i in range(len(users)): users[i] = users[i].split("|")

    while True:
        username = str(input("Username: "))
        password = str(input("Password: "))

        for user in users:
            uname = user[4]
            pword = user[5]
            role = user[2]
            userg = user[3]

            if uname == username and pword == password and role == "Admin":
                print("Hello " + user[0] + ".")
                amainmenu.amainmenu()
                
            if uname == username and pword == password and role == "User":
                print("Hello " + user[0] + ".")
                umainmenu.umainmenu()    
            
        print("Pogresan username/password.")
        x = int(input("1. Pokusaj opet da se ulogujes\n2. Registruj se\n\nUnesi broj: "))
        if x == 1:
            check()
        if x == 2:
            register.reg()

