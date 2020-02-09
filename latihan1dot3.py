import random

def hitung_periode(saldo_awal, besar_bunga, jum_bunga_perthn, jum_per, saldo_akhir):
    saldo_awal
    besar_bunga 
    jum_bunga_perthn 
    jum_per
    saldo_akhir
    satu_periode = 5
    print("Satu periode adalah", satu_periode)
    while (saldo_akhir <= 400):
        jum_per = jum_per+1
        saldo_akhir = int(saldo_awal * (1 + besar_bunga / jum_bunga_perthn) ** (jum_bunga_perthn*jum_per))
        print("periode ke-", jum_per)
        print("saldo", saldo_akhir, ("Juta \n"))
        if(saldo_akhir >= 400):
            break 
    tahun = satu_periode * jum_per
    print("Butuh", tahun, ("Tahun ") + "untuk mencapai saldo Rp", saldo_akhir,"Juta")


hitung_periode(200, 0.1, 1, 0, 0)

#untung kelar :)












#ga ngerti cara looping buat i+=1, kalau make if saldo_awal <= 200 do jum_per +=1