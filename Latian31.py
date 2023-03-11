# Looping dari list

#for loop

kumpulan_angka = [1,2,3,4,5,7,8,9,6,4,5]
for angka in kumpulan_angka:
    print(f"angka= {angka}")

nama_peserta = ["Ilid","Mpig","Cicom"]
for nama in nama_peserta:
    print(f"nama= {nama}")
print("end\n")

#for loop dan range

kumpulan_angka = [1,2,3,4,5,7,8,9,6,4,5]
panjang = len(kumpulan_angka)

for i in range(panjang):
    print (f"angka = {kumpulan_angka[i]}")
print ("end\n")

# pake while
kumpulan_angka = [1,2,3,4,5,7,8,9,6,4,5]
panjang = len(kumpulan_angka)
i=0

while i < panjang:
    print(f"angka = {kumpulan_angka[i]}")
    i +=1
print("end\n")

#List comprehension
kumpulan_angka = [1,2,3,4,5,7,8,9,6,4,5]
angka_kuadrat = [i **2 for i  in kumpulan_angka ]
[print(f"data = {i}") for i in angka_kuadrat]

data = ["Ilid","Mas Angga",1,2,3,"Setan","Babi"]

[print(f"data = {i}") for i in data]
[print (i) for i in data]
print("end\n")

#Enumerate

data_list = ["Ilid","Mas Angga",1,2,3,"Setan","Babi"]

for index, data in enumerate(data_list):
    print(f"index = {index}, data = {data}")