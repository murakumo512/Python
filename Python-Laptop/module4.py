def right(s,amount):
    print (s)
    return s[-amount:]#

def numx():
    num1x = input("Masukkan nilai pertama : ")
    num2x = input("Masukkan nilai kedua : ")
    num3x = input("Masukkan nilai ketiga : ")

    num1 = right(num1x,2)
    num2 = right(num2x, 2)
    num3 = right(num3x, 2)
    
    if num1 == "":
        num1= int(num2)+int(num3)

    if num2 == "":
        num2= int(num1)+int(num3)

    if num3 == "":
        num3= int(num2)+int(num1)


    print("prameter 1 :",num1)
    print("prameter 2 :",num2)
    print("prameter 3 :",num3)

    if num1 == num2: #cek nilai 1 dan 2 apakah sama?
        if num1 == num3:#jika nilai 1 dan 2 sama cek lagi nilai 1 dan 3 apakah sama?
            print("True")#jika ketiganya sama printout "sama"
        else:#jika num1 dan num3 tidak sama maka,
            print("True")#print ini
    else:#jika num1 dan num2 tidak sama maka
        if num2 == num3:#cek lagi apakah num2 dan num3 sama?
            print("True")#jika num2 dan num 3sama maka print 2 sisi sama
        else:#jika num2 dan num3 tidak sama maka,
            if num1 == num3:#cek lagi apakah num1 dan num3 sama?
                print("True")#jika num1 dan num3 sama print
            else:#jika num1 != num3 maka tidak ada yang sama
                print("False") #print tidak ada yang sama

numx()

#say = "71180293"
#print(say[2:3])


#say = "71180293"
#print(say[2:4])

#if (say[2:4]=="18"):
#	print ("angkatan'18")
#7 1 1 8 0 2 9 3
#0 1 2 3 4 5 6 7


