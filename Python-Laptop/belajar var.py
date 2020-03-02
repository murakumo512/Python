varAngka = float(input("Masukkan nilai anda goblok tuolol : "))

if varAngka<100:
    print("Nilai : True")
    print (varAngka)
    if varAngka >= 80:
        print("Nilai A")
    elif varAngka >= 60:
        print("Nilai B")
    elif varAngka >= 50:
        print("Nilai C")
    elif varAngka >= 40:
        print("Nilai D")
    else:
        print("Nilai E")
else:
    print("nilai false")
    print (varAngka)