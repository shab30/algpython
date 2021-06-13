# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:55:54 2021

@author: My Device is Awesome
"""

jwb = "y"
while jwb=="y" or jwb=="Y":
    
    print ("=========================")
    print(" CEK KELULUSAN ")
    print ("=========================")
    
    n = input(">> Masukkan Nilai = ")
    
    if int(n)>60:
        sts = "LULUS"
    else:
        sts="ULANG"
    print(sts)
jwb = input("Mulai lagi?")
    if jwb== "t":
        break