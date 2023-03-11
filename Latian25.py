## ---LIST---

# 1. Kumpulan data numbers
data_angka = [1,2,3,4]
print (data_angka)

# 2. Kumpulan data string
data_string = ["ilid","mas angga", "ais"]
print(data_string)

# 3. Kumpulan data boolean
data_bool = [True, False, False, True]
print(data_bool)

# 4. Data campuran
data_campuran = [1,"Ilid", False]
print(data_campuran)

# 5. Cara alternatif membuat list
data_range = range(0,10) #start,stop,step
data_list = list(data_range)
print(data_list)

# 6. Membuat list dengan for loop (list comprehensif)
data_list_for = [i for i in range (0,10)]
print(data_list_for)

#bisa di kuadrat dll
data_list_for = [i**2 for i in range (0,10)]
print(data_list_for)

# 7. List pake for pake if

list_for_if = [i for i in range (0,10) if i !=5]
print(list_for_if)

list_for_if = [i for i in range (0,10) if i%2 == 0]
print(list_for_if)