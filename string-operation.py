#operator dalam bentuk method
##merubah case dari string

#merubah semua ke upper case
salam = "Saya Sedang Belajar Python"
print("normal =", salam) #output: saya belajar python
salam = salam.upper()
print("upper =", salam) #output: SAYA BELAJAR PYTHON
salam = salam.lower()
print("lower =", salam) #output: saya belajar python

##pengechekan dengan isX method
#contoh pengechekan lower case
data = "saya sedang belajar python"
apakah_lower = data.islower() #method islower() untuk mengechek apakah semua karakter di string adalah lower case
print(data + "islower = " + str(apakah_lower)) #output: True
apakah_upper = data.isupper() #method isupper() untuk mengechek apakah semua karakter di string adalah upper case
print(data + "isupper = " + str(apakah_upper)) #output: False

#isalpha() untuk mengechek apakah semua karakter di string adalah alphabet
data = "saya"
apakah_alpha = data.isalpha()
print(data + " isalpha = " + str(apakah_alpha)) #output: True

#isalnum() untuk mengechek apakah semua karakter di string adalah alphabet dan angka
data = "saya123"
apakah_alnum = data.isalnum()
print(data + " isalnum = " + str(apakah_alnum)) #output: True

#isdecimal() untuk mengechek apakah semua karakter di string adalah angka
data = "123"
apakah_decimal = data.isdecimal()
print(data + " isdecimal = " + str(apakah_decimal)) #output: True

#isspace() untuk mengechek apakah semua karakter di string adalah spasi
data = " "
apakah_space = data.isspace()
print(data + " isspace = " + str(apakah_space)) #output: True

#istitle() untuk mengechek apakah semua kata diawali dengan huruf besar
data = "Saya Sedang Belajar Python"
apakah_title = data.istitle()
print(data + " istitle = " + str(apakah_title)) #output: True

#ngechek komponen startswith() dan endswith()
data = "saya sedang belajar python"
apakah_start = data.startswith("saya") #method startswith() untuk mengechek apakah string dimulai dengan komponen tertentu
print(data + " startswith saya = " + str(apakah_start)) #output: True
apakah_end = data.endswith("python") #method endswith() untuk mengechek apakah string diakhiri dengan komponen tertentu
print(data + " endswith python = " + str(apakah_end)) #output: True


#penggabungan komponen join() dan split()
#join() untuk menggabungkan komponen string
data = ["saya", "sedang", "belajar", "python"]
gabungan = " ".join(data) #menggabungkan list of string menjadi satu string dengan spasi sebagai pemisah
print(gabungan) #output: saya sedang belajar python
gabungan = "-".join(data) #menggabungkan list of string menjadi satu string dengan - sebagai pemisah
print(gabungan) #output: saya-sedang-belajar-python
#split() untuk memecah string menjadi list of string
data = "saya-sedang-belajar-python"
pecah = data.split("-") #memecah string menjadi list of string dengan - sebagai pemisah
print(pecah) #output: ['saya', 'sedang', 'belajar', 'python']   

#alokasi karakter dengan rjust(), ljust(), center()
data = "saya"
kanan = data.rjust(10) #method rjust() untuk menggeser string ke kanan
print("'" + kanan + "'") #output: '      saya'
kiri = data.ljust(10) #method ljust() untuk menggeser string ke kiri
print("'" + kiri + "'") #output: 'saya      '
tengah = data.center(10, "-") #method center() untuk menggeser string ke tengah
print("'" + tengah + "'") #output: '    saya    '
#penghapusan komponen dengan strip(), rstrip(), lstrip()
data = "     saya     "
print("'" + data + "'") #output: '     saya     '
print("'" + data.strip() + "'") #output: 'saya' #method strip() untuk menghapus spasi di kiri dan kanan
print("'" + data.lstrip() + "'") #output: 'saya     ' #method lstrip() untuk menghapus spasi di kiri
print("'" + data.rstrip() + "'") #output: '     saya' #method rstrip() untuk menghapus spasi di kanan