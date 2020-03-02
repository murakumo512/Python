satu = "LalA"
dua = "lALa"
tiga = "LaLa"
empat = ""
for kalimat in range (1,3):
    if kalimat % 2 == 0:
        empat = empat + satu +dua +tiga
    else:
        empat = satu +empat +tiga +dua
    print(empat)