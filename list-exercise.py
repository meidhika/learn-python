#program list buku

list_buku = []
while True:
    judul = input("\nMasukkan judul buku\t\t : ")
    penulis = input("Masukkan nama penulis buku\t : ")

    buku_baru = [judul, penulis]
    list_buku.append(buku_baru)
    

    for index,buku in enumerate(list_buku):
        print(f"{index+1}. {buku[0]} oleh {buku[1]}")

    lanjut = input("\nIngin menambahkan buku lagi? (y/n) : ")
    if lanjut == "n":
        break
print("\nProgram selesai")
