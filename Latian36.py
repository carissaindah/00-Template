# ----------LOOPING DICTIONARY------------

nama_teman = {
    "a" : "Ilid",
    "b" : "Erlangga",
    "c" : "Cemong",
    "d" : "Dudung",
    "e" : "Bulbul"
}

# looping pake for (yg keluar keynya)

for nama in nama_teman:
    print(nama)

# operator untuk mengambil item/iterables
keys = nama_teman.keys()
print(keys)

for key in nama_teman.keys(): #buat ambil key aja
    print(nama_teman.get(key))

values = nama_teman.values() #buat ambil value aja
print(values)

for value in nama_teman.values():
    print(value)

items = nama_teman.items() #buat ambil key ama value
print(items)

for items in nama_teman.items():
    print(items) 

for key, value in nama_teman.items():
    print(f"Key: {key}, value: {value}")