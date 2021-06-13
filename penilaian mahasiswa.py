# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 01:01:34 2021

@author: My Device is Awesome
"""

print("Penilaian Mahasiswa")
print ("=========================")

n = input("Masukkan Nilai = ")

if int(n)>0 and int(n)<=100:
    if int(n)>=91 and int(n)<100: 
        sts="A"
    elif int(n)>=81 and int(n)<91: 
        sts="B"
    elif int(n)>=71 and int(n)<81: 
        sts="C"
    elif int(n)<71:
        sts="D"
        
else:
    pesan="Masukkan angka 0-100 saja"
    print(pesan)