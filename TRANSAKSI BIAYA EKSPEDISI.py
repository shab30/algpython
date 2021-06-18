# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:50:06 2021

@author: My Device is Awesome
"""

print("---TRANSAKSI BIAYA EKSPEDISI---")

print("a = Bali")
print("b = Malang")

kode = ['a','b']
kota = ['Bali','Malang']
jarak = ['135','552']
ongkirperkm = ['3000','3500']

pilihan = input("Masukkan Kode Tujuan = ")

if pilihan=="a":
    idx = 0
elif pilihan=="b":
    idx = 1
    
else:
    idx = 0
    
print("Pilihan Tujuan = " + kota[idx])
print("Jarak = " + str(jarak[idx]) + "km")
print("Ongkir per km = Rp. " + str(ongkirperkm[idx]))

ongkir = jarak[idx] * ongkirperkm[idx]
print(">>>> Total           = Rp. " + str(ongkir))
print(" ")
print("===========================================")