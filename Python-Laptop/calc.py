no1 = float(input("Masukkan angka: "))
bk = input("Masukkan operator : ")
no2 = float(input("Masukkan angka kedua : "))

if bk == "+":
    print(no1 + no2)
elif bk == "-":
    print(no1 - no2)
elif bk == "/":
    print(no1 / no2)
elif bk == "*":
    print(no1 * no2)
else:
    print("operator salah")