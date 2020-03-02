import random
import numbers
from math import *



#Gerard membeli emas 25 gram dengan harga Rp. 650.000/gram. Jika sekarang harga emas menjadi Rp. 685.000/gram,
#• Berapa keuntungan yang didapat oleh Gerard (dalam Rp dan dalam %)?
#• Jika Gerard kemudian membeli lagi 15 gram emas dengan harga Rp. 685.000, maka
#Gerard sekarang memiliki total 40 gram emas. Jika kemudian harga emas naik lagi
#menjadi Rp. 715.000, berapa keuntungan yang didapat oleh Gerard (dalam Rp dan dalam%)?


beli1 = 25
harga1 = 650000 #for each gram
harga2 = 685000 #harganya naik

#jawaban pertanyaan 1, untung dalam rupiah dan %
print("emas pertama : ",  beli1) #total gram
sel1 = beli1 * harga1 #total harga emas pertama
print("total harga emas pertama : Rp ", sel1)
sel2 = beli1 * harga2 #total harga emas kedua
print("total harga emas kedua : Rp ", sel2)

##space created
print()

#ini untung Rupiah pertamanya
untung1 = sel2 - sel1 #untung rupiah pertama
print("untung Gerard pertama : Rp ", untung1)

#ini untung dalam persen pertamanya
untungpercen1 = float(untung1) / float(harga2) * 100/100 #untung percent pertama
print("untung Gerard pertama dalam percent : ", untungpercen1)

##space created
print()

####
beli2 = 15
sel3 = beli2 * harga2
print("pembelian emas yang kedua Gerard : ", sel3)

#total emas gerard
total1 = beli1 + beli2 #total emasnya ada 40
print("Total emas Gerard : ", total1)
harga3 = 715000 #harga emas terbaru pergramnya

#hitung untung ruginya

sel4 = total1 * harga3
print("Total harga emas ketiga : Rp ", sel4) #total harga emas ketiga

untungtebaru = sel4 - untung1
print("untung Gerard ketiga : Rp ", untungtebaru)

#untung percentnya
untungpercent2 = (untungtebaru) / harga3 * 100/100
print("untung Gerard ketiga dalam bentuk percent : ", untungpercent2)
percentage2 = untungpercent2 * 100


#Kepala saya pusing pakk





