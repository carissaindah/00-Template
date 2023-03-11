# ------MULTI KEYS AND NESTING DICTIONARY-----

import datetime
mahasiswa1 = {
    'nama' : 'Erlangga',
    'nim' : '4301190011',
    'sks_lulus' : 138,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000,12,12)
}

mahasiswa2 = {
    'nama' : 'Kuntul',
    'nim' : '4301190012',
    'sks_lulus' : 120,
    'beasiswa' : False,
    'lahir' : datetime.datetime(2002,11,14)
}

mahasiswa3 = {
    'nama' : 'Bulbul',
    'nim' : '4301190013',
    'sks_lulus' : 140,
    'beasiswa' : True,
    'lahir' : datetime.datetime(2000,2,29)
}

data_mahasiswa = {
    'MAH001' : mahasiswa1,
    'MAH002' : mahasiswa2,
    'MAH003' : mahasiswa3  
}

print(f"{'KEY':<6} {'Nama':<10} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*40)

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa

    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim'] 
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    print(f"{KEY:<6} {NAMA:<10} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")
