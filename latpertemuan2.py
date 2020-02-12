import random
import numbers
import time
from math import *

#2.1
def average():
    array = []
    total = 0

    i = int(input("Masukkan data : "))

    for x in range (i):
        nilai = float(input("Masukkan nilai ke {}: ".format(x+1)))
        array.append(nilai)

    print("Hasiln nilai total adalah : ",format(sum(array)))
    print("Hasil nilai rata-rata adalah : ", format(sum(array)))
    menu()


#2.2
def hitung_susah():
    a = int(input("Masukkan bilangan Bulat : "))
    x = 2*a **3 + 2*a + 15/a
    print("Jika Var A adalah : ", a)
    print("Maka hasilnya adalah : ", x)
    menu()

#2.3
def gaji_susah():
    lama_minggu = 5
    to_pa_gaji = 14
    item_a = 10
    item_b = 1


    print()

def exit():
    time.sleep(2)
    exit

# fungsi untuk menampilkan menu
def menu():
    print ("Test Tist")
    print ("Average")
    print("Hitung gajelas")
    print("Gaji gajelas")

print ("test")
print ()
menu()
pilih = input("Masukkan pilihan : ")

if pilih == 1:
    average()
elif pilih == 2:
    hitung_susah()
elif pilih == 3:
    gaji_susah()
elif pilih == 4:
    exit()
else :
    ("salah pilih")