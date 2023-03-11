# Perulangan (Looping)

"""
Menggunakan operasi for untuk looping
for:
    kondisi
    aksi
"""

# List
angka = [0,1,2,3,4]
print(angka)

for i in angka:
    print(f"i sekarang --> {i}")

print("Akhir dari program 1")

# Range
angka_range = range(1,5) # dimulai dari 1, jumlahnya 5 n

for i in angka_range:
    print(f"i sekarang --> {i}")

# Menggunakan string

data_string = "Hai sayang"

for huruf in data_string:
    print(f"spelling --> {huruf}")

