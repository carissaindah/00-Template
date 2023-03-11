"""
1. continue --> akan membuat loop melompat
                ke fungsi selanjutnya
2. pass --> berfungsi sebagai dummy
            jadi tidak akan dieksekusi
3. break --> membuat loop kembali ke end
             ketika sudah dapat hasilnya
"""

# Pass 

#angka = 0

#while angka < 5:
#    angka += 1
#    if angka == 3:
#       pass 
#    print(angka)
        

# continue

#angka = 0

#while angka < 5:
#    angka += 1
#    print (f"angka sekarang --> {angka}") #aksi 1
#    if angka == 2:
#        print("cie") #hondisi lain 
#        continue
#    print("hai") #aksi 2
#print("Selesai gais")

#BREAK

angka = 0

while angka <5 :
    angka += 1
    print(f"angka sekarang adalah --> {angka}")

    if angka == 2:
        print("love")
        break

    print("heiii")

print("udah bos")

data_int = int(input("hitung sampai = "))

angka = 0

while True:
    angka += 1
    print(f"count --> {angka}")

    if angka == data_int:
        print("okey")
        break
    print("hai")

print("udah")




