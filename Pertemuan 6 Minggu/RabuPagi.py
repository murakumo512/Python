import random
import sys
from math import *
import time
import numbers
def satu():
    for i in range(5):
        for j in range(3):
            print("Dalam loop a, j: ", j)
        print("Luar loop a, i:", i)

def dua(n):
    for i in range(1, n+1):
        for j in range(i):
            print(i, end ='\t')
        print()



def tiga(n):
    for i in range(1, n+1):
        if i % 2 == 1:
            for j in range(1, n+1):
                print(j,end='')
        else:
            for i in range(n,0,-1):    #n,0,-1
                print(i, end='')
        print()

n = int(input("Masukkan N : "))
tiga(n)


def empat():
    n = 8
    for i in range(n,0,-1):
        for j in range(1,i+1):
            if j % 2 == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()

#def lima():
    #for i in range(1, n+1):

def enam(baris,kolom):
    for i in range(1, baris+1):
        for j in range(1, kolom+1):
            print(i*j, end = '\t')
        print()

baris = int(input("Masukkan Baris : "))
kolom = int(input("Masukkan Kolom : "))
enam(baris,kolom)
