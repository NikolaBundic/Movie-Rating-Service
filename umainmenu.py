# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 18:59:24 2021

@author: nikola
"""
import login2
import amainmenu
import sys
import matplotlib.pyplot as plt

def listToString(s):  
    str1 = ""  
     
    for ele in s:  
        str1 += ele
        str1 += "|"
    str1 = str1[:-1]
    return str1

def izlistaj():
    filmovi = open("filmovi.txt").read().split("\n")
    for i in range(len(filmovi)): filmovi[i] = filmovi[i].split("|")

    for film in filmovi:
        print(film[0] + ". " + film[1] + ".")
        
def izlistajs():
    serije = open("serije.txt").read().split("\n")
    for i in range(len(serije)): serije[i] = serije[i].split("|")

    for serija in serije:
        print(serija[0] + ". " + serija[1] + ".")
        
def oceni():
    filmovi = open("filmovi.txt").read().split("\n")
    for i in range(len(filmovi)): filmovi[i] = filmovi[i].split("|")
    while True:
        imefilma = str(input("Unesi ime filma: "))
        
        for film in filmovi:
            ime = film[1]
            rbr = film[0]
            
            if ime == imefilma:
                filmovi2 = open("proveraocene.txt").read()
                proveraocena = login2.userg + "|" + rbr + "|"
                if proveraocena in filmovi2:
                    print("\nVec ste ocenili ovaj film")
                    umainmenu()
                
                x = 0
                while x<=0 or x>10:
                    x = float(input("Unesite ocenu za film " + film[1] + ": "))
                x = str(x)
                
                file = open("proveraocene.txt","a")
                file.write("\n")
                file.write (proveraocena + x)
                file.close()
                
                prv = "|" + rbr + "|"
                brojac = 0
                y = 0
                
                filmovi3 = open("proveraocene.txt").read().split("\n")
                for i in range(len(filmovi3)):
                    if prv in filmovi3[i]:
                        filmovi4 = filmovi3[i].split("|")
                        y += float(filmovi4[2])
                        brojac += 1
                
                konacno = y / brojac
                stari = (film[0] + "|" + film[1] + "|" + film[2] + "|" + film[3] + "|" + film[4] + "|" + film[5])
                film[4] = str(format(konacno,".2f"))
                xy = listToString(film)
                with open("filmovi.txt", "r+") as main:
                    lines = main.read()
                    lines.split("\n")
                    xyz = lines.replace(stari, xy)
                    main.seek(0)
                    main.write(xyz)
                    main.close()
                    umainmenu()
                    
                    
def ocenis():
    serije = open("serije.txt").read().split("\n")
    for i in range(len(serije)): serije[i] = serije[i].split("|")
    while True:
        imeserije = str(input("Unesi ime serije: "))
        
        for serija in serije:
            ime = serija[1]
            rbr = serija[0]
            
            if ime == imeserije:
                serija2 = open("proveraocenes.txt").read()
                proveraocena = login2.userg + "|" + rbr + "|"
                if proveraocena in serija2:
                    print("\nVec ste ocenili ovu seriju")
                    umainmenu()
                        
                x = 0
                while x<=0 or x>10:
                    x = float(input("Unesite ocenu za seriju " + serija[1] + ": "))
                x = str(x)
                
                file = open("proveraocenes.txt","a")
                file.write("\n")
                file.write (proveraocena + x)
                file.close()
                
                prv = "|" + rbr + "|"
                brojac = 0
                y = 0
                
                serija3 = open("proveraocenes.txt").read().split("\n")
                for i in range(len(serija3)):
                    if prv in serija3[i]:
                        serija4 = serija3[i].split("|")
                        y += float(serija4[2])
                        brojac += 1
                        
                konacno = y / brojac
                stari = (serija[0] + "|" + serija[1] + "|" + serija[2] + "|" + serija[3] + "|" + serija[4] + "|" + serija[5])
                serija[4] = str(format(konacno, ".2f"))
                xy = listToString(serija)
                with open("serije.txt", "r+") as main:
                    lines = main.read()
                    lines.split("\n")
                    xyz = lines.replace(stari, xy)
                    main.seek(0)
                    main.write(xyz)
                    main.close()
                    umainmenu()
                    
def filmgraf():
    max_value = None
    max_value2 = None
    max_value3 = None
    filmovi = open("filmovi.txt").read().split("\n")
    for i in range(len(filmovi)): filmovi[i] = filmovi[i].split("|")
    
    for film in filmovi:
        ocena = float(film[3])
        if (max_value is None or ocena > max_value):
            max_value = ocena
    for film in filmovi:
        ocena = float(film[3])
        if (max_value2 is None or ocena > max_value2 and ocena != max_value):
            max_value2 = ocena
    for film in filmovi:
        ocena = float(film[3])
        if (max_value3 is None or ocena > max_value3 and ocena != max_value and ocena != max_value2):
            max_value3 = ocena
            
    for film in filmovi:
        ocena = float(film[3])
        if ocena == max_value:
            film1 = film[1]
        if ocena == max_value2:
            film2 = film[1]
        if ocena == max_value3:
            film3 = film[1]
    
    filmovi2 = [film1, film2, film3]
    ocene = [max_value, max_value2, max_value3]
    
    New_Colors = ['green','blue','purple']
    plt.bar(filmovi2, ocene, color=New_Colors)
    plt.title('Top 3 filma', fontsize=14)
    plt.xlabel('Film', fontsize=14)
    plt.ylabel('Ocena', fontsize=14)
    plt.grid(True)
    plt.show()

    umainmenu()
    
def serijegraf():
    max_value = None
    max_value2 = None
    max_value3 = None
    serije = open("serije.txt").read().split("\n")
    for i in range(len(serije)): serije[i] = serije[i].split("|")
    
    for film in serije:
        ocena = float(film[3])
        if (max_value is None or ocena > max_value):
            max_value = ocena
    for film in serije:
        ocena = float(film[3])
        if (max_value2 is None or ocena > max_value2 and ocena != max_value):
            max_value2 = ocena
    for film in serije:
        ocena = float(film[3])
        if (max_value3 is None or ocena > max_value3 and ocena != max_value and ocena != max_value2):
            max_value3 = ocena
            
    for film in serije:
        ocena = float(film[3])
        if ocena == max_value:
            film1 = film[1]
        if ocena == max_value2:
            film2 = film[1]
        if ocena == max_value3:
            film3 = film[1]
    
    filmovi2 = [film1, film2, film3]
    ocene = [max_value, max_value2, max_value3]
    
    New_Colors = ['green','blue','purple']
    plt.bar(filmovi2, ocene, color=New_Colors)
    plt.title('Top 3 serije', fontsize=14)
    plt.xlabel('Serije', fontsize=14)
    plt.ylabel('Ocena', fontsize=14)
    plt.grid(True)
    plt.show()

    umainmenu()
    
def detaljnifilmovi():
    print ("{:<35} {:<10} {:<20} {:<15} {:<15}".format('Ime Filma','|Godina','|Reziser','|Ocena Kritika','|Ocena Korisnika'))
    print ("------------------------------------+----------+--------------------+---------------+--------------")
    filmovi = open("filmovi.txt").read().split("\n")
    for i in range(len(filmovi)): filmovi[i] = filmovi[i].split("|")
    for film in filmovi:
        print ("{:<35} {:<10} {:<20} {:<15} {:<15}".format(film[1],"|" + film[2],"|" + film[5],"|" + film[3],"|" + film[4]))
        
def detaljneserije():
    print ("{:<35} {:<10} {:<20} {:<15} {:<15}".format('Ime Serije','|Godina','|Reziser','|Ocena Kritika','|Ocena Korisnika'))
    print ("------------------------------------+----------+--------------------+---------------+--------------")
    serije = open("serije.txt").read().split("\n")
    for i in range(len(serije)): serije[i] = serije[i].split("|")
    for serija in serije:
        print ("{:<35} {:<10} {:<20} {:<15} {:<15}".format(serija[1],"|" + serija[2],"|" + serija[5],"|" + serija[3],"|" + serija[4]))
                                
def umainmenu():
    print("\n")
    print("1. Izlistaj filmove")
    print("2. Detaljniji pregled filmova")
    print("3. Ocenite film")
    print("4. Top 3 filma po ocenama kritika")
    print("5. Izlistaj serije")
    print("6. Detaljniji pregled serija")
    print("7. Ocenite seriju")
    print("8. Top 3 serije po ocenama kritika")
    print("9. Ugasite program")
    if login2.role == "Admin":
        print("10. Vrati se u administratorski meni")
    
    x = 0
    while x<=0 or x>10:
        x = int(input("Unesite broj: "))
    if x == 1:
        izlistaj()
        umainmenu()
    if x == 2:
        detaljnifilmovi()
        umainmenu()
    if x == 3:
        oceni()
    if x == 4:
        filmgraf()
        umainmenu()
    if x == 5:
        izlistajs()
        umainmenu()
    if x == 6:
        detaljneserije()
        umainmenu()
    if x == 7:
        ocenis()
    if x == 8:
        serijegraf()
        umainmenu()
    if x == 9:
        sys.exit()
    if x == 10 and login2.role == "Admin":
        amainmenu.amainmenu()
        