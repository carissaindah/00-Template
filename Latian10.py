#Bitwise, operasi biner

a = 9
b = 5

# bitwise or (|)
c = a | b
print("===========or===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print("--------------------------------------(|)")
print ('nilai :',c,',binary:',format(c,'08b'))

#bitwise and (&)
c = a & b
print("===========and===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print("--------------------------------------(&)")
print ('nilai :',c,',binary:',format(c,'08b'))

#bitwise XOR (^)
c = a ^ b
print("===========xor===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print ('nilai :',b,',binary :',format(b,'08b'))
print("--------------------------------------(^)")
print ('nilai :',c,',binary:',format(c,'08b'))

#bitwise NOT (~)
c = ~a
print("===========xor===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print("--------------------------------------(~)")
print ('nilai :',c,',binary:',format(c,'08b'))

#shifting

#shift right (>>)
c = a >> 1
print("===========>>===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print("--------------------------------------(>>)")
print ('nilai :',c,',binary:',format(c,'08b'))

#shift right (<<)
c = a << 1
print("===========<<===========")
print ('nilai :',a,',binary :',format(a,'08b'))
print("--------------------------------------(<<)")
print ('nilai :',c,',binary:',format(c,'08b'))