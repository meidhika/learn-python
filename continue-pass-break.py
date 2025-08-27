#continue, pass, break


#pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi
# angka = 0
# while angka < 10:
#     angka += 1
#     if angka == 5:
#         pass #tidak akan dieksekusi
#     print(f"angka = {angka}")


#continue -> dia akan melewati kondisi tertentu
# angka = 0
# while angka < 10:
#     angka += 1
#     print(f"angka = {angka}")
#     if angka == 5:
#         print("nice")
#         continue #melewati kondisi tertentu
#     print("whatsup!")
# print("akhir dari program") #output

#break -> dia akan menghentikan perulangan
# angka = 0
# while angka < 10:
#     angka += 1
#     print(f"angka = {angka}")
#     if angka == 5:
#         print("nice")
#         break #menghentikan perulangan
#     print("whatsup!")
# print("akhir dari program") #output


data_input = int(input("Masukkan angka: "))
angka = 0
while True:
    angka += 1
    print(f"angka = {angka}")
    if angka == data_input:
        print("nice")
        break
    print("whatsup!")
print("akhir dari program") #output