# operasi yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assignment

a = 5 # adalah assignment
print("nilai = ",a)
 
a += 1 # artinya a = a + 1
print("nilai a += 1",", akan menjadi",a)

a -= 1 # artinya a = a - 1
print("nilai a -= 1",", akan menjadi",a)

a *= 2 # artinya a = a * 2
print("nilai a *= 2",", akan menjadi",a)

a /= 2 # artinya a = a / 2
print("nilai a /= 2",", akan menjadi",a)

a //= 1 # artinya a = a // 1
print("nilai a //= 1",", akan menjadi",a)

a %= 2 # artinya a = a % 2
print("nilai a %= 2",", akan menjadi",a)

a = 5
a **= 2 # artinya a = a ** 2
print("nilai a **= 2",", akan menjadi",a)

#Operasi bitwise
#or
c = True
c |= False
print("nilai c|= False",", akan menjadi",c)
c = False
c |= False
print("nilai c|= False",", akan menjadi",c)

#and
c = True
c &= False
print("nilai c&= False",", akan menjadi",c)
c = True
c &= True
print("nilai c&= True",", akan menjadi",c)

#XOR
c = True
c ^= False
print("nilai c^= False",", akan menjadi",c)
c = False
c ^= True
print("nilai c^= True",", akan menjadi",c)

#Shifting
d = 0b0100
d >>= 1
print("nilai d>>= 1",", akan menjadi",format(d,'04b'))

d = 0b0100
d <<= 1
print("nilai d<<= 1",", akan menjadi",format(d,'04b'))