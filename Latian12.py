"""
Cara membuat string
1. Dengan menggunakan single quote '...'
2. Dengan menggunakan double quote "..."
"""

data = 'Bebi sayang'
print (data)

data = "Mas angga jahat ninggalin aku"
print (data)

print('"Apaan si beb"')
print("'mas angga'")
print("kebanyakan 'antot")

"""
3. Menggunakan tanda \
   a. bisa membuat tanda ' menjadi string
   b. untuk membuat tanda \ keliatan
   c. ngebuat jarak jauhan \t (tab)
   d. ngebuat jarak deketan \b (backspace)
   e. ngebuat enter (newline)
"""

#a.
print('apaan si \'antot')

#b backlash
print("C:\\user\\MasAngga")

#c tab
print("Mas angga\t Icha")

#d backspace
print("Mas angga \bIcha")

#e newline
print("Mas Angga \nIcha") #LF -> line feed -> unix, mac os, linux
print("Mas Angga \rIcha") #CR -> Carriage return -> commodore, acorn, lisp
print("Mas Angga\r\nIcha") #CRLF -> line feed carriage return -> windows

"""
    4. String literal atau raw
"""

#hati hati
print('C:\new folder') #akan salah pathnya

#menggunakan raw string
print(r'C:\new folder')

#multiline literal string
print("""
Ilid
Mas angga""")