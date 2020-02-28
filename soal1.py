import random
import numbers
import math


def soal1():
   #num1 = int(input("Masukkan nilai pertama : "))
    #num2 = int(input("Masukkan nilai kedua : "))
    #num3 = int(input("Masukkan nilai ketiga : "))

    #if num1 == num2 and num2 == num3 and num3 == num1:
        #print("semua angka sama")
    #else:
        #numbers.sort(num1,num2,num3)
        #print(numbers.sort)

    deret = [] #ini buat listnya nilainya
    i = int(input("Masukkan jumlah data : ")) #masukann banyaknya data


    x = 0 #berikan nilai awa 0
    while x < i: #selama x kurang dari i
        nilai = input("Masukkan nilai ke {}: ".format(x+1)) #outpunya akan masukan nilai ke 1, karena x+1
        x += 1 #jika inputan adalah angka, maka +1
        deret.append(int(nilai))

    n = len(deret) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if deret[j] > deret[j+1] : 
                deret[j], deret[j+1] = deret[j+1], deret[j] 

    print ("Sorted array is:") 
    for i in range(len(deret)): 
        print ("%d" %deret[i])


def soal2():
    print("Soal no.2")
    array = [] #ini buat listnya nilainya
#    i = int(input("Masukkan jumlah data : ")) #masukann banyaknya data
    i = 1

    x = 0 #berikan nilai awa 0
    while x < i: #selama x kurang dari i
    #for x in range (i): <<<salah
        nilai = input("jumlah potong kue yang diberikan: ".format(x+1)) #outpunya akan masukan nilai ke 1, karena x+1
        if (nilai >= "a" and nilai <= "z") or (int(nilai) < 0): #jika inputan adalah a-z maka salah
            print("salah") #print salah
        else:
            x += 1 #jika inputan adalah angka, maka +1
            nilaix = int(nilai) #karena nilai inputan adalah string kita perlu merubahnya menjadi int
            array.append(nilaix) #menambah elemen list dengan append

            if (nilai % 2 == 1):
                print("Nami marah besar")
            else:
                if (nilai == 0 ):
                    print("Mereka tidak mendapatkan kue")
                else:
                    print("jumlah potong kue yang diterima masing-masing ", nilai / 2)

def soal22():
    nilaix = input("Jumlah potong kue yang diberikan :")
    if (nilaix >= "a" and nilaix <= "z") or (int(nilaix) < 0):
        print("salah") #print salah
    else:
        nilai = int(nilaix)
        if (nilai % 2 == 1):
                print("Nami marah besar")
        else:
            if (nilai == 0 ):
                print("Mereka tidak mendapatkan kue")
            else:
                print("jumlah potong kue yang diterima masing-masing ", nilai / 2)


def soal3():
    prumah = int(input("Panjang Rumah = "))
    lrumah = int(input("Lebar Rumah = "))
    spersegi = int(input("Panjang sisi persegi = "))
    lhome = prumah * lrumah             
    lpersegi = spersegi * spersegi
    sper = 2
    shom = 10
    keramik = lhome / lpersegi
    print(keramik)
    if lpersegi < sper:
        print("inputan anda tidak sesusai ketentuan")
    elif lhome < shom:
        print("inputan anda tidak sesuai ketentuan")
    elif ((keramik - int(keramik)) > 0):
        keramix = int(keramik)+1
        print(keramix)
    else:
        keramix = keramik
        print(keramix)

    

def soal4():
    a= 3.6
    print(int(a))

soal1()
