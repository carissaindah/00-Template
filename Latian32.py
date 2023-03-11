# PROGRAM LIST BUKU


list_buku = []
while True:
    print("\nMasukkan data buku")
    judul = input ("Masukkan judul buku\t: ")
    penulis = input("Masukkan penulis\t: ")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    
    print("\n","="*10, "Data Buku","="*10)
    for index, buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n","="*20)
    isLanjut = input("Apakah akan dilanjutkan?(y/n)")

    if isLanjut == "n":
        break
print("program selesai")
    