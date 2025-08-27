#Teknik Menduplikat List

a = ["mei", "dhika", "nawa", "sapta"]
print("data a",a)

b =a
print("data b",b)

#kita akan merubah member dari a
#ini akan merubah kedua list
a[1] = "budi"
b.sort()
print("data a",a)
print("data b",b)

#menduplikat list dengan copy()
print("membuat list c dengan copy dari a")
c = a.copy()
c[1] = "ucup"
print("data c",c)