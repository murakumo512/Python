import random
import numbers
import time
import sys
from math import *

#soal 2.1
def average():
    print("Soal no.1")
    array = []
    total = 0

    i = int(input("Masukkan data : "))

    for x in range (i):
        nilai = float(input("Masukkan nilai ke {}: ".format(x+1)))
        array.append(nilai)

    print("Hasiln nilai total adalah : ",format(sum(array)))
    print("Hasil nilai rata-rata adalah : ", format(sum(array)))
    print()
    menu()


#soal 2.2
def hitung_susah():
    print("Soal no.2")
    a = int(input("Masukkan bilangan Bulat : "))
    x = 2*a **3 + 2*a + 15/a
    print("Jika Var A adalah : ", a)
    print("Maka hasilnya adalah : ", x)
    print()
    menu()

#soal 2.3
def gaji_susah():
    print("Soal no.3")
    print()

    hari = 35
    seminggu = 7
    perdaykerja = 9
    soalminggu = 5

    GajiPerJam = int(input("Gaji perjam : Rp. ")) #Gaji per jam
    PajakGaji = 0.14 #bayar pajak dari penghasilan selama bekerja adalah 14%
    BeliBajuAkses = 0.10 #beli baju dan aksesoris pada smt baru adalah 10%
    Atul = 0.01 #alat tulis 1%
    Sedekah = 0.25 #lalu sedekah 25%

    
    gajiseminggu = int(seminggu * perdaykerja * GajiPerJam)
    gajimu = int(gajiseminggu * soalminggu)

    gajipajak = int(gajimu * PajakGaji) #ini hasil dari gaji kali pajaknya 14%
    gajipajaks = int(gajimu - gajipajak) #ini gaji - pajak

    beliBA = int(BeliBajuAkses * gajipajaks) #harga akesesoris
    belitul = int(Atul * gajipajaks) #harga alat tulis
    sisagaji = int(gajipajaks - (beliBA+belitul))
    #beliBAS = int(gajipajaks - beliBA)
    #belitul = int(Atul * beliBAS)
    #belituls = int(beliBAS - belitul)

    dekah = int(sisagaji * Sedekah)
    yatim = int(dekah / 1000) * 1000
    yatims = int(yatim * 0.3)
    dhuafa = int(dekah - yatims)


    print("Hari : ", hari, "Hari")
    print("Minggu : ", seminggu, "Hari")
    print("sehari kerja : ", perdaykerja, "jam")
    print("kerjanya selama : ", soalminggu, "Minggu")
    print()
    print("Gaji dalam seminggu  : Rp.", gajiseminggu)
    print("Gaji sebelum bayar pajak : Rp.", gajimu)
    print("Gaji setelah bayar pajak : Rp.", gajipajaks)
    print()
    print("Baju dan Aksesoris : Rp.", beliBA)
    print("Alat tulis : Rp. ", belitul)
    print("Sisa uang Budi : Rp.", sisagaji)
    print()
    print("Sedekah : Rp.", dekah)
    print("Yatim : Rp.", yatims)
    print("Dhuafa : Rp", dhuafa)
    #print("Sisa uang Budi : Rp.", beliBAS)
    #print()
    #print("Alat tulis menghabiskan : Rp.", belitul)
    #print("Sisa uang Budi : Rp.", belituls)
    #print()
    #print("Uang yang disedekahkan Budi : Rp.", dekah)
    #print("Sisa uang Budi : Rp.", dekahs)




    print()
    menu()
# fungsi exit program
def exit():
    print("Exiting Program")
    time.sleep(2)
    sys.exit

# fungsi untuk menampilkan menu
def menu():
    print ("1. Average")
    print("2. Hitung gajelas")
    print("3. Gaji gajelas")
    print("4. Exit")


menu()
loop = 1
while loop:
    pilih = input("Masukkan pilihan : ")
    print()
    if pilih == "1":
        average()
    elif pilih == "2":
        hitung_susah()
    elif pilih == "3":
        gaji_susah()
    elif pilih == "4":
        exit()
    else :
        ("salah pilih")