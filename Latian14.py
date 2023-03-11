# operator dalam bentuk method

## merubah case dari string

#Uppercase
ayang = "Erlangga Dewa"
print("Ayang = " + ayang)
ayang = ayang.upper()
print("Ayang = " + ayang)

#Lowercase
ayang = "ERLANGGA DEWA"
print("Ayang = " + ayang)
ayang = ayang.lower()
print("Ayang = " + ayang)

##pengecekan dengan isX method
ayang = "erlangga"
apakah_lower = ayang.islower() #hasilnya boolean
print(ayang + " is lower = " + str(apakah_lower))

ayang = "ERLANGGA"
apakah_upper = ayang.isupper() #hasilnya boolean
print(ayang + " is upper = " + str(apakah_upper))

"""
    3. isalpha() --> ngecek semuanya huruf
    4. isalnum() --> huruf dan angka
    5. isdecimal() --> angka aja
    6. isspace() --> spassi, tab, newline
    7. istitle() --> semua kata dimulai dengan huruf besar
"""

#mengecek komponen startswith() endswith() 
cek_start = "Mas Angga sayang".startswith("Mas")
print("start =" + str(cek_start))

cek_end = "Mas Angga sayang".startswith("sayang")
print("end =" + str(cek_end))

## penggabungan komponen join() split()

pisah = ['Mas Angga','sayang','Icha']
gabung = ' '.join(pisah)
print(gabung)

gabungan = "MasAnggaehmsayangehmIchaehmgamauehmpisah"
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()

kanan = "Erlangga".rjust(10)
print("'" + kanan + "'")

kiri = "Erlangga".ljust(10)
print("'" + kiri + "'")

tengah = "Erlangga".center(20,"-")
print("'" + tengah + "'")

#kebalikannya --> strip()
tengah = tengah.strip("-")
print("'" + tengah + "'")