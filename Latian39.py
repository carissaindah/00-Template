# template  dict mahasiswa

import datetime
import os
import string
import random

mahasiswa_template = {
    'nama' : 'nama',
    'nim' : '0000000000',
    'sks_lulus': 0,
    'lahir' :datetime.datetime(111,11,11)

}

data_mahasiswa = {}

while True: 
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print('-'*30)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = input("SKS Lulus: ")
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (DD): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range (6)))
    data_mahasiswa.update({KEY: mahasiswa})
    
    print(f"{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS':<10}  {'Lahir':<10}")
    print("-"*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim'] 
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:<10} {LAHIR:<10}")

    print("\n")
    is_done = input("Adalah lagi (y/n)?")
    if is_done == "n":
        break

print(f"Akhir dari program, terima kasih")