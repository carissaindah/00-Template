#Tipe data 1: Angka satuan (integer)
data_integer = 1
print("data : ", data_integer) 
print("- bertipe : ", type(data_integer))

#Tipe data 2 : Angka dengan koma (float)
data_float = 12.15
print("data : ", data_float)
print("- bertipe : ", type(data_float))

#Tipe data 3 : kumpulan karakter (string)
data_string = "mas angga nakal"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

#Tipe data 4 : biner true/false (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

#Tipe data khusus

#bilangan kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))
