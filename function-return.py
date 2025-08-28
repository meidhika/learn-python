# Fungsi dengan return

#fungsi kuadrat

def kuadrat(angka):
    hasil = angka ** 2
    return hasil

angka = int(input("Masukkan angka: "))
hasil_kuadrat = kuadrat(angka)
print(f"Hasil kuadrat dari {angka} adalah {hasil_kuadrat}")


z = 10 + kuadrat(5)
print(z)


# def tambah (angka1, angka2):
#     return angka1 + angka2

# a = tambah(10, 20)
# print(a)


#fungsi dengan return banyak

def operasi_mtk (angka1, angka2):
    kali = angka1 * angka2
    bagi = angka1 / angka2
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    return kali, bagi, tambah, kurang

angka1 = int(input("Masukkan angka1: "))
angka2 = int(input("Masukkan angka2: "))
kali, bagi, tambah, kurang = operasi_mtk(angka1, angka2)

print(f"Hasil kali {kali}")
print(f"Hasil bagi {bagi}")
print(f"Hasil tambah {tambah}")
print(f"Hasil kurang {kurang}")