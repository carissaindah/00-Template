# -------- MANIPULASI LIST--------

## OPERASI

#Index    0(-4)    1(-3)    2(-2)   3(-1)
data = ["Ilid","Mas Angga","Ais","Kuntul"]

data_0 = data[0]
print(f"Data pertama --> {data_0}")

# Mengambil info jumlah data 

panjang_data = len(data)
print(f"panjang data adalah {panjang_data}")

## Manipulasi data list

# Menambahkan data
data.insert(2,"Cici") #data.insert(posisi,datanya)
print(data)
#Nambah data di akhir
data.append("Piglet")
print(data)

# menambah list dengan list
data_baru = ["Babi", "Munyuk"]
data.extend(data_baru)
print(data)

#Merubah data --> merubah data index 2 jadi "BUlbul"
data[2] = "Bulbul"
print(data)

# Meremove data
data.remove("Babi")
print(data)

# Meremove data paling belakang
data.pop()
print(data)

