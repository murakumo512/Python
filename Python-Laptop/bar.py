import random


saldo_awal = 200
besar_bunga = 0.1
jum_bunga_perthn = 1
#jum_per = 0
saldo_akhir = 0
#satu_periode = 5
#print("Satu periode adalah", satu_periode)

while True:
    jum_per = jum_per+1
saldo_akhir = saldo_awal * (1 + besar_bunga / jum_bunga_perthn) ** (jum_bunga_perthn*jum_per)
print(jum_per)
print(saldo_akhir)
if(saldo_akhir >400):
    break









#ga ngerti cara looping buat i+=1, kalau make if saldo_awal <= 200 do jum_per +=1