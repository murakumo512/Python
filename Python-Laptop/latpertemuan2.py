import random
import numbers
import time
import sys
from math import *

#soal 2.1
def average():
    print("Soal no.1")
    array = [] #ini buat listnya nilainya
    i = int(input("Masukkan jumlah data : ")) #masukann banyaknya data


    x = 0 #berikan nilai awa 0
    while x < i: #selama x kurang dari i
    #for x in range (i): <<<salah
        nilai = input("Masukkan nilai ke {}: ".format(x+1)) #outpunya akan masukan nilai ke 1, karena x+1
        if nilai >= "a" and nilai <= "z": #jika inputan adalah a-z maka salah
            print("salah") #print salah
        else:
            x += 1 #jika inputan adalah angka, maka +1
            nilaix = int(nilai) #karena nilai inputan adalah string kita perlu merubahnya menjadi int
            array.append(nilaix) #menambah elemen list dengan append

    print("Hasiln nilai total adalah : ",format(sum(array))) #sum buat nambahin semua jumlah nilainya
    print("Hasil nilai rata-rata adalah : ", format(sum(array) / nilaix)) #nah setelah mendapatkan semua jumlah nilai baru dibagi dengan jumlahnya data
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

    hari = 35 #total hari dalam 5 minggu
    seminggu = 7
    perdaykerja = 9
    soalminggu = 5  #soalnya minta 5 minggu

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
    sisagaji = int(gajipajaks - (beliBA+belitul)) #jadi alat tulis sama aksesorisnya dibeli jadi 1, totalnya 11%
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
    sys.exit

# fungsi untuk menampilkan menu
def menu():
    print ("1. Average")
    print("2. Hitung var")
    print("3. Gaji")
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
        print("salah pilih")


        #71180293 - Mardonius Riel