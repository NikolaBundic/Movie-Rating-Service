# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 17:58:12 2021

@author: nikola
"""
import register
import login2

x = 0
while x<=0 or x>2:
    x = int(input("1. Uloguj se\n2. Registruj se\n\nUnesi broj: "))
if x == 1:
    login2.check()
if x == 2:
    register.reg()