# operasi dan manipulasi string

# 1. menyambung string (concatenate)

nama_depan = "Erlangga"
nama_tengah = "Dewa"
nama_akhir = "Sakti"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. menghitung panjang string
panjang = len(nama_lengkap)
print("Panjang dari" + nama_lengkap + "=" + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string

D = "D"
status = D in nama_lengkap
print("String " + D + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print("String " + d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*12)
print(12*"wk")

# indexing (mengambil data dari string/motong2)
print("Index ke-0 :" + nama_lengkap[0])
print("Index ke-1 :" + nama_lengkap[1])
print("Index ke-(-1) :" + nama_lengkap[-1]) #kalau minus ambilnya dari blkg
print("Index ke-(0,2) :" + nama_lengkap[0:3]) #pyton bakal ngeprint index ke 0 ama 1 aja kalo nulis 0:2
print("Index ke-(0,2,4,6,8,10) :" + nama_lengkap[0:11:2]) #pyton bakal ngeprint index ke 0 ama 1 aja kalo nulis 0:2

# item paling kecil
print("paling kecil: " + min(nama_lengkap))

# item paling max
print("paling besar: " + max(nama_lengkap))

ascii_code = ord(" ")
print("Ascii code untuk spasi adalah " + str(ascii_code))

ascii_code = ord("w")
print("Ascii code untuk w adalah " + str(ascii_code))

data = 117
print("Char untuk ascii code 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "erlangga dewa sakti kek silit"
jumlah = data.count("s")
print("Jumlah s pada " + data + " adalah " + str(jumlah))

