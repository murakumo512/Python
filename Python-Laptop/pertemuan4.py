import random
import numbers
from math import*


def nilai_tengah(a,b,c,d): #nilai terbesar kedua
    nilai = [a,b,c,d]
    nilai.sort()#urutkan
    return nilai[1]#ambil elemen ke dua


c = nilai_tengah(7,8,9,10)
print(c)

def nilai_mid(a,b,c):
    max_pertama = a
    max_kedua = 0

    if b > max_pertama:
        max_kedua = max_pertama
        max_pertama = b
    elif b > max_kedua:
        max_kedua = b
        
    if c > max_pertama:
        max_kedua = max_pertama
        max_pertama = c
    elif c > max_kedua:
        max_kedua = c

    return max_kedua

print(nilai_mid(6,7,8))
print(nilai_mid(12,7,9))
print(nilai_mid(30,28,25))
print(nilai_mid(20,7,8))
print(nilai_mid(6,7,8))
print(nilai_mid(6,7,8))




angka = [3, 45, 22, 10]
#cari nilai maksimal dari dalam list variabel angka
print(max(angka))
45

def ratarata():
    array = []
    total = 0
    n = int(input("Masukkan banyaknya elemen array: "))
    for x in range(n):
        nilai = float(input("Masukkan nilai ke-{} : ".format(x+1)))
        array.append(nilai)
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    print("Hasil rata-rata adalah : {}".format(sum(array)/n))


        Baris 1 : mendeklarasikan variable array yang berupa array kosong.
    Baris 3 : mendeklarasikan variable n dan menginputkan banyaknya data kedalam variable n oleh user.
    Baris 5-7 : melakukan perulangan sebanyak n dan menginputkan nilai dari setiap data lalu dimasukkan kedalam variable array.
    Baris 10-11 : menampilkan hasil total nilai dengan menggunakan fungsi sum dari variable array dan nilai rata-rata dari hasil operasi total dibagi jumlah variable n.



#mean
import statistics
from fractions import Fraction as F
from decimal import Decimal as D
 
statistics.mean([11, 2, 13, 14, 44])
# returns 16.8
 
statistics.mean([F(8, 10), F(11, 20), F(2, 5), F(28, 5)])
# returns Fraction(147, 80)
 
statistics.mean([D("1.5"), D("5.75"), D("10.625"), D("2.375")])
# returns Decimal('5.0625')


#random
import random
import statistics
 
data_points = [ random.randint(1, 100) for x in range(1,1001) ]
statistics.mean(data_points)
# returns 50.618
 
data_points = [ random.triangular(1, 100, 80) for x in range(1,1001) ]
statistics.mean(data_points)
# returns 59.93292281437689


#modus
import random
import statistics
 
data_points = [ random.randint(1, 100) for x in range(1,1001) ]
statistics.mode(data_points)
# returns 94
 
data_points = [ random.randint(1, 100) for x in range(1,1001) ]
statistics.mode(data_points)
# returns 49
 
data_points = [ random.randint(1, 100) for x in range(1,1001) ]
statistics.mode(data_points)
# returns 32
 
mode(["cat", "dog", "dog", "cat", "monkey", "monkey", "dog"])
# returns 'dog'



#median
import random
import statistics
 
data_points = [ random.randint(1, 100) for x in range(1,50) ]
statistics.median(data_points)
# returns 53
 
data_points = [ random.randint(1, 100) for x in range(1,51) ]
statistics.median(data_points)
# returns 51.0
 
data_points = [ random.randint(1, 100) for x in range(1,51) ]
statistics.median(data_points)
# returns 49.0
 
data_points = [ random.randint(1, 100) for x in range(1,51) ]
statistics.median_low(data_points)
# returns 50
 
statistics.median_high(data_points)
# returns 52
 
statistics.median(data_points)
# returns 51.0



#ukur sebaran data
import statistics
from fractions import Fraction as F
 
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
statistics.pvariance(data)     # returns 6.666666666666667
statistics.pstdev(data)        # returns 2.581988897471611
statistics.variance(data)      # returns 7.5
statistics.stdev(data)         # returns 2.7386127875258306
 
more_data = [3, 4, 5, 5, 5, 5, 5, 6, 6]
 
statistics.pvariance(more_data)   # returns 0.7654320987654322
statistics.pstdev(more_data)      # returns 0.8748897637790901
 
some_fractions = [F(5, 6), F(2, 3), F(11, 12)]
statistics.variance(some_fractions)
# returns Fraction(7, 432)