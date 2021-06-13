# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 00:57:24 2021

@author: My Device is Awesome
"""

print("Cek Nilai")
print ("=========================")

n = input("Masukkan Nilai = ")

if int(n)>0 and int(n)<=100:
    if int(n)>80: 
        sts="Baik Sekali"
    elif int(n)>=65: 
        sts="Baik"
    elif int(n)>=55: 
        sts="Cukup"
    elif int(u)>=40:
        sts="Kurang"
        
    else:
        sts="Kurang Sekali"
    print (sts)
else:
    pesan="Masukkan angka 0-100 saja"
    print(pesan)