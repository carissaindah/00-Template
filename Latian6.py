#latihan konversi satuan temperature

#Program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius : "))
print("Suhu adalah",celcius, "Celcius")

#Reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah : ",reamur, "Reamur")

#Farenheit
farenheit = ((9/5) * celcius) +32
print("Suhu dalam farenheit adalah : ",farenheit, "Farenheit")

#Kelvin
kelvin = celcius + 273.15
print("Suhu dalam kelvin adalah : ",kelvin, "Kelvin")
