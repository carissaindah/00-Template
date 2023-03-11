# OPERASI LOGIKA ATAU BOOLEAN

"""
    1. not
    2. or
    3. and
    4. xor
"""

#NOT
print("===NOT===") #ini bakal print kebalikannya
a = False
c = not a
print("data a = ",a)
print("data c = ",c)

#OR 
print("===OR===") #kalau salah satu true bakal jadi true
a = True
b = True
c = a or b
print(a,'or',b,'=',c)
a = True
b = False
c = a or b
print(a,'or',b,'=',c)
a = False
b = True
c = a or b
print(a,'or',b,'=',c)
a = False
b = False
c = a or b
print(a,'or',b,'=',c)

#AND
print("===AND===") #kalau salah satu false bakal jadi false
a = True
b = True
c = a and b
print(a,'and',b,'=',c)
a = True
b = False
c = a and b
print(a,'and',b,'=',c)
a = False
b = True
c = a and b
print(a,'and',b,'=',c)
a = False
b = False
c = a and b
print(a,'and',b,'=',c)

#XOR
print("===XOR===") #jika salah satu true bakal true, lainnya false
a = True
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'xor',b,'=',c)
a = False
b = False
c = a ^ b
print(a,'xor',b,'=',c)