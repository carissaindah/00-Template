# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
hasil = a > 3
print(a,'>',3,'=',hasil)

hasil = b > 3
print(b,'>',3,'=',hasil)

# Lebih kecil dari
hasil = a < 3
print(a,'<',3,'=',hasil)

hasil = b < 3
print(b,'<',3,'=',hasil)

# Lebih besar sama dengan
hasil = a >= 3
print(a,'>=',3,'=',hasil)

hasil = b >= 3
print(b,'>=',3,'=',hasil)

# Lebih kecil sama dengan
hasil = a <= 3
print(a,'<=',3,'=',hasil)

hasil = b <= 3
print(b,'<=',3,'=',hasil)

#Sama dengan
hasil = a == 3
print(a,'==',3,'=',hasil)

hasil = b == 3
print(b,'==',3,'=',hasil)

#Tidak sama dengan
hasil = a != 4
print(a,'!=',4,'=',hasil)

hasil = b != 4
print(b,'!=',4,'=',hasil)

# is itu membandingkan variabel dgn variabel lain
#is sebagai komparasi object identity

x = 5 #ini adalah assingnment membuat object
y = 5

print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))

hasil = x is y
print('x is y =',hasil)

x = 5 #ini adalah assingnment membuat object
y = 6

print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))

hasil = x is y
print('x is y =',hasil)

#is not
x = 5 #ini adalah assingnment membuat object
y = 5

print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))

hasil = x is not y
print('x is not y =',hasil)

x = 5 #ini adalah assingnment membuat object
y = 6

print("nilai x =",x,"id = ",hex(id(x)))
print("nilai y =",y,"id = ",hex(id(y)))

hasil = x is not y
print('x is not y =',hasil)