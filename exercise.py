# Latihan perulangan membuat segitiga


# 1. menggunakan for

sisi = 10
# count = 1
# print("Menggunakan for")
# for i in range(sisi):
#     print('*' * count)
#     count += 1

# menggunakan while
# print("\nMenggunakan while")
# count = 1
# while True:
#     print("*" * count)
#     count += 1
#     if count > sisi:
#         break
# print("Akhir dari perulangan")

# hanya ganjil saja
print("\nMenggunakan while")
count = 1
while True:
    #akan kembali keatas jika count ganjil
    if ~(count % 2):
        count += 1
        continue

    #akan print jika count genap
    print("*" * count)
    count += 1
    if count > sisi:
        break
print("Akhir dari perulangan")
