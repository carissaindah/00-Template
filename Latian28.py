#Teknik menduplikasi list

a = a = ["Ilid","Bulbul","Nyanyak","Mpig"]
print(f"data a = {a}")

b = a
print(f"data b = {b}")

#coba ubah member a -->ternyata merubah keduanya (adressnya sama)

a[1] = "Pigsy"

print(f"data a = {a}")
print(f"data b = {b}")

#duplikat list dengan copy --> kalo di ubah gakan ngubah data utama

c = a.copy()
print(f"data c = {c}")
c[0] = "Mas Angga"
print(f"data a = {a}")
print(f"data b = {b}")
print(f"data c = {c}")
