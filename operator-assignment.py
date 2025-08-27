#operasi yang dapat dilakukan dengan penyingkatan
#operasi ditambah dengan assignment

a =5 #adalah assignment
print("nilai a =", a)

#a =a+1 #adalah operasi ditambah dengan assignment
a += 1 #adalah operasi ditambah dengan assignment dengan penyingkatan
print("nilai a =", a)

a -= 2 #adalah operasi dikurang dengan assignment dengan penyingkatan
print("nilai a =", a)

a *= 5 #adalah operasi dikali dengan assignment dengan penyingkatan
print("nilai a =", a)

a /= 2 #adalah operasi dibagi dengan assignment dengan penyingkatan
print("nilai a =", a)

b =10
print("nilai b =", b)
b %= 3 #adalah operasi modulus dengan assignment dengan penyingkatan
print("nilai b =", b)

b //= 3 #adalah operasi floor division dengan assignment dengan penyingkatan
print("nilai b =", b)

b **= 3 #adalah operasi pangkat dengan assignment dengan penyingkatan
print("nilai b =", b)


#operasi bitwise dengan assignment
c = True
print("nilai c =", c)
c |= False #adalah operasi bitwise OR dengan assignment dengan penyingkatan
print("nilai c =", c)
c &= False #adalah operasi bitwise AND dengan assignment dengan penyingkatan
print("nilai c =", c)
c ^= True #adalah operasi bitwise XOR dengan assignment dengan penyingkatan
print("nilai c =", c)


c = False
print("nilai c =", c)
c <<= True #adalah operasi bitwise left shift dengan assignment dengan penyingkatan
print("nilai c =", c)
c >>= False #adalah operasi bitwise right shift dengan assignment dengan penyingkatan
print("nilai c =", c)