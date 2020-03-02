import random
import math
import numbers

def tambah(a,b):
    hasil = a + b
    return hasil

hasil1 = tambah(3,7)
print("ini soal 1:", hasil1)


def tambahh(a,b):
    hasil = a + b
    return hasil

print("ini soal 2:", tambahh(10,20))

tambahh = lambda a,b : a + b
print("ini soal 3:", tambahh(10,20))

def cek_angka():
    num1 = input("num1 = ")
    num2 = input("num2 = ")
    num3 = input("num3 = ")



def cek_digit_belakang():
    inputanmu = input("%d %d %d", num1, num2, num3)


def kelipatan_sembilan(angka):
    if angka % 9 == 0:
        return angka
    else:
        return false

kelipatan_sembilan = lambda angka: angka % 9 == 0
print(kelipatan_sembilan(69))
print(kelipatan_sembilan(2000))






def nilaitengah(a,b,c):
    if (a != b and b != c):
        print("angka harus berbeda")
        if ()