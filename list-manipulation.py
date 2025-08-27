## Operasi

# index 
data = ['dhika', 'budi', 'andi', 'caca']

#mengambil data dari list
data_index_0 = data[0]
print("Data index ke 0: ", data_index_0)

data_terakhir = data[-1]
print("Data index terakhir: ", data_terakhir)


#panjang list
panjang_data = len(data)
print(f"Panjang data: {panjang_data}")

#manipulasi data list
#menambahkan item pada list sesuai posisi
data.insert(1, 'susi')
print("Data setelah insert: \n", data)

#menambahkan item di akhir list
data.append('jojo')
print("Data setelah append: \n", data)

#menambahkan list dengan list
data_baru = ['mei', 'nawa', 'sapta']
data.extend(data_baru)
print("Data setelah extend: \n", data)

#merubah data
#kita ubah data 2
data[2] = 'andi'
print("Data setelah diubah: \n", data)

#menghapus data
#kita hapus data 2
data.remove('susi') #harus sesuai case sensitive
print("Data setelah dihapus: \n", data)

#menghapus data paling akhir
data.pop()
print("Data setelah dihapus: \n", data)

#menghapus semua data
data.clear()
print("Data setelah dihapus: \n", data)