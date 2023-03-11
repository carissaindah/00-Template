#OPERASI MATEMATIKA

a = 5
b = 2

#operasi tambah
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi pengurangan
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi perkalian
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi pembagian
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi pangkat (exponen) pakai **
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus (sisa dari pembagian) pake %
#kalo di % dengan bilangan yg lebih kecil hasilnya bilangan yg kecil itu
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division kebalikan modulus //
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi
'''
    1. ()
    2. eksponen **
    3. perkalian dll * / % //
    4. tambah dll + -
'''
x=3
y=2
z=4

hasil = x ** y / z * y - x + z // y % x 

print(x,'**',y,'/',z,'*',y,'-',x,'+',z,'//',y,'%',x,'=', hasil)

hasil = y % 3
print(y,'%',x,'=',hasil)