data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print("data angka",data_angka)

#count data
jumlah_data_4 = data_angka.count(4)
print("jumlah data 4 adalah", jumlah_data_4)
jumlah_data_3 = data_angka.count(3)
print("jumlah data 3 adalah", jumlah_data_3)



#ambil posisi data
data = ["mei", "dhika", "nawa", "sapta"]
print("data", data)
data_dhika = data.index("dhika")
print("posisi data dhika adalah", data_dhika)

#mengurutkan list
data_angka.sort()
data.sort()
print("data urut", data)
print("data angka urut", data_angka)


#mengurutkan list secara terbalik
data_angka.reverse()
data.reverse()
print("data urut terbalik", data)
print("data angka urut terbalik", data_angka)
