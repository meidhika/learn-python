data_0 = [1,2]
data_1 = [3,4]


list_biasa = [1,2,3,4]
print("List biasa :",list_biasa)

list_2D = [data_0, data_1]
print("List 2D :",list_2D)

list_2d_campuran = [data_0,data_1,5,6,7]
print("List 2D campuran :",list_2d_campuran)


#contoh penggunaan
peserta_0 = ["dhika", 25, "laki-laki"]
peserta_1 = ["ucup", 20, "laki-laki"]
peserta_2 = ["asep", 30, "laki-laki"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print("list peserta:",list_peserta)

for peserta in list_peserta:
    print("nama :",peserta[0])
    print("umur :",peserta[1])
    print("gender:",peserta[2])
    print("-------------")
