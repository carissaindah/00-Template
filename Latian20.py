# Latihan membuat Kalkulator

print(20*"=")
print("KALKULATOR")
print(20*"="+ "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+,-,*,/) : ")
angka_2 = float(input("Masukkan angka 2 = "))

if operator== "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator== "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator== "/":
    if angka_2== 0:
        print("tidak terdefinisi")
    elif angka_1== 0:
        print("Hasilnya adalah = 0")
    else:
        hasil = angka_1 / angka_2
        print(f"Hasilnya adalah = {hasil}")
elif operator== "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator== "**":
    hasil = angka_1 * angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator== "%":
    hasil = angka_1 % angka_2
    print(f"Hasilnya adalah = {hasil}")
elif operator== "//":
    hasil = angka_1 // angka_2
    print(f"Hasilnya adalah = {hasil}")

    