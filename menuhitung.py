import random
import numbers
import sys
import time
from math import *


def trapesium () : #ini adalah sebuah fungsi untuk mengerjakan luas trapesium
    #t = int(input("Masukkan tinggi : "))
    #j = int(input("Masukkan jumlah sisi sejajar : "))
    #l = int(t * j / 2) #ini rumus
    #print ("Jadi luas trapesium adalah : ", l, ("\n")) #ini resultny
    array = []
    total = 0

    i = int(input("Masukkan data : "))

    for x in range (i):
        nilai = float(input("Masukkan nilai ke {}: ".format(x+1)))
        array.append(nilai)

    print("Hasiln nilai total adalah : ",format(sum(array)))
    print("Hasil nilai rata-rata adalah : ", format(sum(array)))
    menu() #ini balik ke menu lagi

def jajargenjang () : #ini adalah sebuah fungsi untuk mengerjakan luas jajargenjang
    t = int(input("Masukkan tinggi segitiga : "))
    a = int(input("Masukkan alas segitiga : "))
    l = a * t #ini rumus
    print ("Jadi luas jajargenjang adalah : ", l, ("\n"))
    menu() #ini balik ke menu lagi

def bola () : #ini adalah sebuah fungsi untuk mengerjakan luas bola
    r = int(input("Masukkan jari - jari : "))
    l = 4 * 3.14 * r * r #ini rumus
    print ("Jadi luas bola adalah : ", l, ("\n")) #ini resultnya
    menu()#ini balik ke menu lagi

def quit () : #ini adalah sebuah fungsi untuk keluar dari program
    print("Exiting Program...")
    time.sleep(2) #tunggu 2 detik dan dia akan keluar

def menu(): #ini adalah fungsi menu
    print ("Menu Pilihan")
    print()
    print ("1. Trapesium")
    print ("2. Jajargenjang")
    print ("3. Bola")
    print ("4. exit")

menu() #ini buat namipilin fungsi menu()
loop = 1 #ini buat looping
while loop == 1: #jika loopingnya dikasih 1 maka setelah selesai menyelesaikan fungsi-fungsi diatas diakan balik ke menu lagi
    pilih = input("Masukkan pilihan : ")
    if pilih == "1":
        trapesium()
    elif pilih == "2":
        jajargenjang()
    elif pilih == "3":
        bola()
    elif pilih == "4":
        quit()
        loop = 0 #disini agak berbeda, loop dikasih 0 agar tidak terjadi looping lagi sehingga program bisa keluar
    else :
        print("Salah Pilih!") #ini bila dirimu salah memasukan angka
        menu()