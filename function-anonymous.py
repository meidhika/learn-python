# annonymous function
#currying <- Haskell Curry

def pangkat (angka, n):
    hasil = angka ** n
    return hasil

data_hasil = pangkat(2, 3)
print(f"fungsi biasa {data_hasil}")


#dengan currying menjadi

def pangkat(n):
    return lambda angka: angka ** n

pangkat2 = pangkat(2)
print(f"fungsi currying {pangkat2(3)}")

pangkat3 = pangkat(3)
print(f"fungsi currying {pangkat3(3)}")

print(f"fungsi currying {pangkat(3)(5)}")