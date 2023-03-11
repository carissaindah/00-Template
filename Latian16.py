# Width and Multiline

# Data

data_nama = "Ilid"
data_umur = 21
data_tinggi = 158
data_berat = 42

# String standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, berat = {data_berat}"
print(data_string)

# String multiline \n pake enter
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nberat = {data_berat}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#String multiline pakai kutip triplets
data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
berat = {data_berat}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

#mengatur lebar
data_string = f"""nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
berat  = {data_berat:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)