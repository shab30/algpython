# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 00:55:39 2021

@author: My Device is Awesome
"""

print("")
print("===============================")
print("KANTIN FAK. TEKNOLOGI INFORMASI")
print("===============================")
print("=MENU MAKANAN=")
print("a = Nasi Goreng Rp 15.000")
print("b = Lontong Goreng Rp 14.900")
print("c = Bakso Goreng Rp 12.900")
print("d = Rujak Goreng Rp 13.000")
print("e = Rujak Bakso Rp 15.000")
print("f = Rujak Bakso Pecel Rp 17.000")
print("")

kode = ['a','b','c','d','e','f']
namaMakanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel']
harga = [15000,14900,12900,13000,15000,17000]

pilihan = input(">Masukan kode Makanan = ")
qty = input(">Masukan Jumlah Makanan = ")

i = 0
while i<len(namaMakanan):
    if kode[i] == pilihan:
        nm_mknan = namaMakanan[i]
        hrgsat = harga[i]
        i+=1
        
tot_byr = hrgsat * int(qty)

print("> Nama Makanan  : " + nm_mknan)
print("> Harga Makanan : " + str(hrgsat))
print("> Jumlah Makanan : " + qty)
print("=================================")
print("> Total Bayar : " + str(tot_byr))

print("")
print("=MENU MINUMAN=")
print("a. Teh Dingin/Hangat/Panas = Rp 2.500")
print("b. Kopi Dngin = Rp 5.000")
print("c. Kopi Teh Panas = Rp 6.500")
print("d. Coca Cola Dingin = Rp 3.500")
print("e. Coca Cola Panas = Rp 5.000")

kode =['a','b','c','d','e']
namaMinuman =['Teh Dingin/Hangat/Panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
harga =[2500,5000,6500,3500,5000]

pilihan = input(">Masukan kode Minuman = ")
qty = input(">Masukan Jumlah Minuman = ")

i = 0
while i<len(namaMinuman):
    if kode[i] == pilihan:
        nm_mnmam = namaMinuman[i]
        hrgsat = harga[i]
        i+=1
        
tot_byr = hrgsat * int(qty)

print("> Nama Minuman  : " + nm_mnmam)
print("> Harga Minuman : " + str(hrgsat))
print("> Jumlah Minuman : " + qty)
print("=================================")
print("> Total Bayar : " + str(tot_byr))
