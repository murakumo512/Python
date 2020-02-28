import random
import numbers
import math

def hitungharibulan():
    inpbulan = input("Masukkan bulan (1-12): ")
    if inpbulan == "1":
        print("Jumlah hari: 31")
    elif inpbulan == "2":
        print("Jumlah hari: 29")
    elif inpbulan == "3":
        print("Jumlah hari: 31")
    elif inpbulan == "4":
        print("Jumlah hari: 30")
    elif inpbulan == "5":
        print("Jumlah hari: 31")
    elif inpbulan == "6":
        print("Jumlah hari: 30")
    elif inpbulan == "7":
        print("Jumlah hari: 31")
    elif inpbulan == "8":
        print("Jumlah hari: 31")
    elif inpbulan == "9":
        print("Jumlah hari: 30")
    elif inpbulan == "10":
        print("Jumlah hari: 31")
    elif inpbulan == "11":
        print("Jumlah hari: 30")
    elif inpbulan == "12":
        print("Jumlah hari: 31")
    else:
        print("inputan salah")


def soal1():
    num1 = int(input("Masukkan nilai pertama : "))
    num2 = int(input("Masukkan nilai kedua : "))
    num3 = int(input("Masukkan nilai ketiga : "))

    if num1 == num2: #cek nilai 1 dan 2 apakah sama?
        if num1 == num3:#jika nilai 1 dan 2 sama cek lagi nilai 1 dan 3 apakah sama?
            print("sama")#jika ketiganya sama printout "sama"
        else:#jika num1 dan num3 tidak sama maka,
            print("2 sisi sama")#print ini
    else:#jika num1 dan num2 tidak sama maka
        if num2 == num3:#cek lagi apakah num2 dan num3 sama?
            print("2 sisi sama")#jika num2 dan num 3sama maka print 2 sisi sama
        else:#jika num2 dan num3 tidak sama maka,
            if num1 == num3:#cek lagi apakah num1 dan num3 sama?
                print("2 sisi sama")#jika num1 dan num3 sama print
            else:#jika num1 != num3 maka tidak ada yang sama
                print("tiadk ada yang sama") #print tidak ada yang sama
    #soal1()

soal1()