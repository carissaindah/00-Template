# Date and time

import datetime as dt

hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari =  {hari_ini:%A}")

print("Silahkan masukkan tanggal, \nbulan, dan tahun lahir anda")

tanggal = int(input("Tanggal \t: "))
bulan   = int(input("Bulan \t\t: "))
tahun   = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir Anda adalah = {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal {hari_ini}")

umur_hari = hari_ini - tanggal_lahir
print(f"Umur Anda adalah = {umur_hari}")

umur_tahun = umur_hari.days // 365
print(f"Umur Anda saat ini adalah {umur_tahun} tahun")