#operasi logika atau boolean

#not, or, and, xor

#jika a bernilai true maka c akan bernilai false
print("====NOT====")
a = True
c = not a
print("data a =", a)
print("data c =", c)


#jika salah satu bernilai true maka hasilnya true
print("\n====OR====")
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
print("data c =", c)


#jika keduanya bernilai true maka hasilnya true
#jika salah satu bernilai false maka hasilnya false
print("\n====AND====")
a = True
b = False
c = a and b
print("data c =", c)


#jika salah satu bernilai true maka hasilnya true
#jika keduanya bernilai true atau false maka hasilnya false
print("\n====XOR====")
a = True
b = False
c = a ^ b
print("data c =", c)

