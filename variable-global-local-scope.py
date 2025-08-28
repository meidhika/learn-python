## Global dan Local Scope


nama_global = "dhika"  #global scope

#akses varibale global dalam fungsi

def fungsi():
    print(f"fungsi menampilkan {nama_global}")

fungsi()


#akses varibale global dalam loop
for i in range(0,5):
    print(f"loop {i} menampilkan {nama_global}")

if True:
    print(f"if menampilkan {nama_global}")



## variabel local scope
def fungsi2():
    nama_local = "nawa" #variabel local scope
    print(f"fungsi menampilkan {nama_local}")

fungsi2()
#print(nama_local) #tidak bisa diakses


## Contoh 1 : Penggunaan akses variabel
def say_hello():
    print(f"hello {nama}")

nama = "dhika"
say_hello()

## Contoh 2: merubah variabel global
angka = 0
nama = "sapta"
def ubah(nilai_baru, nama_baru):
    global angka  #fungsi ini mendapat akses merubah angka
    global nama #fungsi ini mendapat akses merubah nama 
    angka = nilai_baru
    nama = nama_baru


print(f"angka sebelum diubah = {angka, nama}")
ubah(10, "nawa")
print(f"angka setelah diubah = {angka, nama}")


## Contoh 3: variable local dapat diakses ketika pakai if dan for
angka = 0
for i in range (0,5):
    angka += 1
    angka_dummy = 2

print(f"angka = {angka}")
print(f"angka_dummy = {angka_dummy}")

if True:
    angka = 10
    angka_dummy = 3


print(f"angka = {angka}")
print(f"angka_dummy = {angka_dummy}")