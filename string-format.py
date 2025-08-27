#format string

nama = "Ucup"
format_str = f"Hallo {nama}, apa kabar?"
print(format_str) #output: Hallo Ucup, apa kabar?


#angka
angka = 2025.5
format_str = f"angka = {angka}"
print(format_str) 

#boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

#bilangan bulat
bilangan_bulat = 25
format_str = f"bilangan bulat = {bilangan_bulat:d}"
print(format_str)

#bilangan dengan pemisah ribuan
bilangan_ribuan = 1000000
format_str = f"bilangan ribuan = {bilangan_ribuan:,}"
print(format_str) #output: bilangan ribuan = 1,000,000

#bilangan dengan desimal
bilangan_desimal = 2025.5
format_str = f"bilangan desimal = {bilangan_desimal:.2f}"
print(format_str)

#bilangan leading zero
bilangan_leading_zero = 2005.54321
format_str = f"bilangan leading zero = {bilangan_leading_zero:09.3f}"
print(format_str) #output: bilangan leading zero = 02005.543

#menampilkan tanda + atau - pada bilangan
positif = 25
negatif = -25
format_str = f"positif = {positif:+d}, negatif = {negatif:+d}"
print(format_str)

#memformat persen
persen = 0.25
format_str = f"persen = {persen:.1%}"
print(format_str)

#melakukan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5
total = harga * jumlah
format_str = f"total harga = Rp.{harga*jumlah:,d}"
print(format_str) #output: total harga = 50,000

#format angka lainnya (binary, octal, hexadecimal)
angka = 255
binary= f"binary = {angka:b}"
format_binary = f"binary = {bin(angka)}"
print(binary) #output: binary = 11111111
octal = f"octal = {angka:o}"
format_octal = f"octal = {oct(angka)}"
print(octal) #output: octal = 377
hexadecimal = f"hexadecimal = {angka:x}"
format_hexadecimal = f"hexadecimal = {hex(angka)}"
print(hexadecimal) #output: hexadecimal = ff
print(format_binary) #output: binary = 0b11111111
print(format_octal) #output: octal = 0o377
print(format_hexadecimal) #output: hexadecimal = 0xff