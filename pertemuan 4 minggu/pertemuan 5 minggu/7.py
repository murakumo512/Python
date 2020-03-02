hargaKaos = 50000
jumlahDibeli = 5
member = 1
total = 2000

total = total * 4 /10
total -= 10000
if jumlahDibeli >=3:
    total = float(hargaKaos * jumlahDibeli)
    if member ==1 and total > 10000:
        print(total)