import random
import numbers
from math import *

#Berkaitan dengan compound interest pada Contoh 1.2 dan 1.3, jika Erika memiliki
#uang 200 juta rupiah dan ingin disimpan di deposito Pasti Cuan sampai uangnya menjadi
#minimal 400 juta, berapa lama waktu yang dibutuhkan?
#catatan: bunga 10% per-tahun.

uang_erika = 200
target_erika = 400
bungapersen = 0.1

print("Uang Erika sekarang : Rp", uang_erika, ("Juta"))
print("Target uang Erika : Rp", target_erika, ("Juta"))

### space created
print()
### space created

pening_erika = target_erika - uang_erika
print("Peningkatan Erika harus : ", pening_erika, ("%"))
lamanya = int((pening_erika / 100) / bungapersen)
print("Lamanya waktu yang dibutuhkan untuk mencapai target adalah", lamanya, ("Tahun"))

