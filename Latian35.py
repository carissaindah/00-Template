# operator dictionary

data_dict = {
    'a' : 'Ilid',
    'b' : 'Erlangga',
    'c' : 12
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# MENGECEK KEY EXIST ATAU GA

KEY = "a"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data_dict: {CHECKKEY}")

# mengakses value (read) dengan get --> kalo get cuma di dict aja
print(data_dict["a"])
print(data_dict.get("a"))
print(data_dict.get("z","key tidak ditemukan"))

# mengupdate data
data_dict ["a"] = "Ilid manies"
print(data_dict)
data_dict ["d"] = "Uuhuy"
print(data_dict)

#cara enak nya pake update
data_dict.update({"a":"Icha manis"})
print(data_dict)
data_dict.update({"e":"Bulbul manis"})
print(data_dict)

#mendelete data
del data_dict["d"]
print(data_dict)

