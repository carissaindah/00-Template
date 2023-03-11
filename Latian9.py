# lATIHAN LOGIKA DAN KOMPARASI

# membuat gabungan area rentang dari angka

""" CASE 1 GABUNGAN
    ++++3--------10+++++++
    PAKAI OR
"""
inputUser = float(input("Masukan angka yang bernilai\nkurang dari 3\n atau\nlebih besar dari 10\n:"))

#++++++++3------------
#Memeriksa angka <3
isKurangDari = (inputUser < 3)

#-----------10+++++
#Memeriksa angka>10
isLebihDari = (inputUser > 10)

isCorrect = isKurangDari or isLebihDari
print("Angka yang anda masukkan =", isCorrect)


""" CASE 2 IRISAN
    -------3++++++10-----------
    PAKAI AND
"""
inputUser = float(input("Masukan angka yang bernilai\nlebih dari 3\n dan\nkurang dari 10\n:"))

#--------3++++++
#Memeriksa angka >3
isLebihDari = (inputUser > 3)

#++++++10---------
#Memeriksa angka<10
isKurangDari = (inputUser < 10)

isCorrect = isKurangDari and isLebihDari
print("Angka yang anda masukkan =", isCorrect)

"""" CASE 3
    ----0++++5----8++++11----
"""

inputUser = float(input("Masukan angka yang bernilai\n>0 dan <5\natau\n>8 dan <11\n:"))
isLebihDari = (inputUser > 0)
isKurangDari = (inputUser < 5)
isCorrectA = isKurangDari and isLebihDari

isLebihDari = (inputUser > 8)
isKurangDari = (inputUser < 11)
isCorrectB = isKurangDari and isLebihDari

isCorrect = isCorrectA or isCorrectB
print("Angka yang anda masukkan =", isCorrect)

"""" CASE 4
    ++++0----5++++8----11++++
"""

inputUser = float(input("Masukan angka yang bernilai\n<0 atau <11\natau\n>5 dan <8\n:"))
isLebihDari = (inputUser > 5)
isKurangDari = (inputUser < 8)
isCorrectA = isKurangDari and isLebihDari

isLebihDari = (inputUser > 11)
isKurangDari = (inputUser < 0)
isCorrectB = isKurangDari or isLebihDari

isCorrect = isCorrectA or isCorrectB
print("Angka yang anda masukkan =", isCorrect)