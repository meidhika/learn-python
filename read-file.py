## Tutorial membaca file eksternal
print(3*"==", "Membaca File Txt", 3*"==")

file = open("read-file.txt", mode="r")


print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

# print(file.read())

# # baca per baris
# print(file.readline(), end="") # Baca baris pertama
# print(file.readline(), end="") # Baca baris kedua
# print(file.readline(), ) # Baca baris ketiga dan akhirnya hilangkan enter


## baca semua baris sebagai 
print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")


## salah satu teknik membuka file di python
print(3*"==", "Membaca File Txt dengan with", 3*"==")
with open("read-file.txt", mode="r") as file:
    content = file.readline()
    print(content, end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")

