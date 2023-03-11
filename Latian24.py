# Latihan perulangan

# sisi = 10

# # 1.menggunakan for
# count = 10
# for i in range(sisi):
#     print("*"*count)
#     count -= 1

"""# 2.menggunakan while
sisi = 10
count = sisi
while True:
    print("*"*count)
    count -= 1

    if count == 0:
        break
print("selesai")

# 3. hanya ganjil saja
sisi = 10
count = 1
while True:

    if (count%2):
        print("*"*count)
        count += 1
    else:
        count += 1
        continue
           
    if count > sisi:
        break
print("akhir")"""

# sisi = 10
# count = 1
# while True:

#     if (count%2):
#         print("*"*count)
#         count += 1
#     else:
#         count += 1
#         continue
           
#     if count > sisi:
#         break
# print("akhir")

sisi = 20
spasi = int(sisi/2)
count = 1
while True:
    if (count%2):
        print(" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue       
    if count > sisi:
        break
count = sisi - 1
spasi2 = 1
while True:
    if (count%2):
        print(" "*spasi2,"+"*count)
        spasi2 += 1
        count -= 1
    else:
        count -= 1
        continue       
    if count == 0:
        break