#operasi dan manipulasi string

#menggabungkan string (concatenate)
nama_pertama = "Meidhika"
nama_tengah = "Nawa"
nama_akhir = "Sapta"

nama_lengkap = nama_pertama +" "+  nama_tengah +" "+  nama_akhir
print(nama_lengkap) #output: MeidhikaNawaSapta


#menghitung panjang string
panjang_nama = len(nama_lengkap)
print("panjang nama dari", nama_lengkap, "adalah", str(panjang_nama), "karakter") #output: 19

#operator untuk string
#mengechek apakah ada komponen char atau string di dalam string
d = "dhika"
print("dhika" in nama_lengkap) #output: True
print("dhika" not in nama_lengkap) #output: False

#mengulang string
print("wk"*10) #output: wkwkwkwkwkwkwkwkwk

#string indexing
#Meidhika Nawa Sapta
print(nama_lengkap[0]) #output: M
print(nama_lengkap[-1]) #output: a
print(nama_lengkap[0:5]) #output: Meidh
print(nama_lengkap[0:5:2]) #output: Mih
print(nama_lengkap[0::3]) #output: Mh aS


#item paling kecil
print(min(nama_lengkap)) #output:  (spasi)
#item paling besar
print(max(nama_lengkap)) #output: w

#ascii code
ascii_code = ord(" ")
print("ascii code untuk spasi adalah", ascii_code) #output: 32
data_char = chr(32)
print("char untuk ascii code 32 adalah", data_char) #output:  (spasi)

#operator dalam bentuk method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada ", data, "adalah", jumlah) #output: 6