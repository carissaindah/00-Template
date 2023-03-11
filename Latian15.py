#Format string

# Contoh generic
#String
nama = "Erlangga"
str = "Hellaw " + nama

print (str)

#Menjadi
nama = "Ilid"
format_str = f"hellow {nama}"
print(format_str)

#Angka
angka = 2012.5
format_str = f"angka = {angka}"
print(format_str)

#Bilangan bulat
angka = 201
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

#Bilangan ribuan
angka = 100000
format_str = f"ribuan = {angka:,}"
print(format_str)

#Bilangan decimal
angka = 3232321.212
format_str = f"desimal = {angka:.1f}"
print(format_str)

#Leading Zero
angka = 32321.212
format_str = f"desimal = {angka:09.1f}"
print(format_str)

#Menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10.123
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(angka_minus)
print(angka_plus)

#Memformat persen
prosentase = 0.456
format_persen = f"prosentase = {prosentase:.2%}"
print(format_persen)

#Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# melakukan operasi aritmetika

# Luas Persegi Panjang
panjang = float(input("Masukkan panjang = "))
lebar = float(input("Masukkan lebar = "))

format_luas = f"luas persegi panjang = {panjang*lebar}"
print(format_luas)

# Luas Segitiga

alas = float(input("Masukkan alas = "))
tinggi = float(input("Masukkan tinggi = "))

format_luas = f"luas segitiga = {alas*tinggi/2}"
print(format_luas)