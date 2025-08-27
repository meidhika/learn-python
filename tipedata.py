#tipe data integer : angka bulat
data_integer = 1
print("data : ", data_integer, ", type : ", type(data_integer))

#tipe data float : angka dengan koma
data_float = 1.5
print("data : ", data_float, ", type : ", type(data_float))

#tipe data string : kumpulan karakter
data_string = "ucup"
print("data : ", data_string, ", type : ", type(data_string))

#tipe data boolean : true/false
data_bool = True
print("data : ", data_bool, ", type : ", type(data_bool))

#tipe data khusus
#tipe data kompleks
data_complex = complex(5,6)
print("data : ", data_complex, ", type : ", type(data_complex))

#tipe data dari bahasa C
from ctypes import c_double, c_char, c_long
data_c_double = c_double(10.5)
print("data : ", data_c_double, ", type : ", type(data_c_double))