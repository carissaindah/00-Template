# -------NESTED LIST---------
# LIST DI DALAM LIST

data_0 = [0,1]
data_1 = [2,3]

data = [1,2,3,4]

list2D = [data_0,data_1,4,5]
print(list2D)

#contoh penggunaan

peserta_0 = ["Ucup",25,"Laki-laki"]
peserta_1 = ["Ilid",22,"Perempuan"]
peserta_2 = ["Mas Angga",23,"Laki-laki"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print(list)

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")

