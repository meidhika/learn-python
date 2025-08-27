#operasi komparasi

#setiap operasi komparasi akan menghasilkan nilai boolean, True atau False

# > lebih dari
# < kurang dari
# >= lebih dari sama dengan
# <= kurang dari sama dengan
# == sama dengan
# != tidak sama dengan
# is, is not
# in, not in

a = 4
b = 2

#lebih besar dari
print("--Lebih besar dari--")
hasil = a > b
print("Hasil dari", a, ">", b, "adalah", hasil)

#kurang dari
print("--Kurang dari--")
hasil = a < b
print("Hasil dari", a, "<", b, "adalah", hasil)

#lebih besar sama dengan
print("--Lebih besar sama dengan--")
hasil = a >= b
print("Hasil dari", a, ">=", b, "adalah", hasil)

#kurang dari sama dengan
print("--Kurang dari sama dengan--")
hasil = a <= b
print("Hasil dari", a, "<=", b, "adalah", hasil)

#sama dengan
print("--Sama dengan--")
hasil = a == b
print("Hasil dari", a, "==", b, "adalah", hasil)

#tidak sama dengan
print("--Tidak sama dengan--")
hasil = a != b
print("Hasil dari", a, "!=", b, "adalah", hasil)

#is, is not
print("--is, is not--")
x = 5
y = 5
z = x

print(x is y) #true
print(x is z) #true

print(x is not y) #false
print(x is not z) #false