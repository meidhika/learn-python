# Error ada syntax error, logic error, runtime error, 
# exception error terjadi saat program sedang berjalan
# syntax error terjadi ketika program tidak sesuai dengan aturan bahasa pemrograman


# contoh sederhana untuk menambah exception
# from math import nan
# input_user = int(input("Masukkan angka: "))
# hasil = nan

# try:
#     hasil = 10 / input_user
# except:
#     print("Input tidak boleh 0")

# print(hasil)



# contoh di aplikasi
# while(True):
#     angka = int(input("Masukkan angka pembagi: "))
#     try:
#         hasil = 10 / angka
#         print(hasil)
#         is_done = input("Apakah sudah selesai? (y/n) ")
#         if is_done == "y":
#             print("Program selesai")
#             break
#     except:
#         print("Input tidak boleh 0, masukkan input lagi")
# print("Program selesai")


#contoh aplikasi untuk membuat file data.txt
# while(True):
#     try:
#         with open("data.txt", "r") as file:
#             print(file.read())
#             break
#     except:
#         print("File tidak ditemukan membuat file baru")
#         with open("data.txt", "w", encoding="utf-8") as file:
#             file.write("ini file baru kedua")
#             break
# print("Program selesai")