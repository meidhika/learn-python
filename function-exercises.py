#Function Exercises


import os

# Program menghitung luas dan keliling persegi panjang

# Membuat Header Program
# os.system('cls')
# print(f"{'Program Menghitung Luas':^40}")
# print(f"{'dan Keliling Persegi Panjang':^40}")
# print(f"{'-'*40:^40}")

# #Mengambil input user
# LEBAR = int(input("Masukkan lebar: "))
# PANJANG =int(input("Masukkan panjang: "))


# #Program Menghitung Luas
# LUAS = LEBAR * PANJANG
# KELILING = 2 * (LEBAR + PANJANG)


# # tampilkan hasil
# print(f"Hasil Luas Persegi Panjang: {LUAS}")
# print(f"Hasil keliling Persegi Panjang: {KELILING}")



def header():
    # os.system('cls')
    print(f"{'Program Menghitung Luas':^40}")
    print(f"{'dan Keliling Persegi Panjang':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    LEBAR = int(input("Masukkan lebar: "))
    PANJANG =int(input("Masukkan panjang: "))
    return LEBAR, PANJANG

def hitung_luas(LEBAR, PANJANG):
    return LEBAR * PANJANG

def hitung_keliling(LEBAR, PANJANG):
    return 2 * (LEBAR + PANJANG)

def display(message, value):
    print(f"Hasil perhitungan {message}: {value}")

while True:
    header()
    opsi = input("pilih opsi perhitungan (luas/keliling): ")

    if opsi == "luas":
        LEBAR, PANJANG = input_user()
        LUAS = hitung_luas(LEBAR, PANJANG)
        display(f"luas", LUAS)
    elif opsi == "keliling":
        LEBAR, PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR, PANJANG)
        display(f"keliling",KELILING)
    else:
        print("Pilihan tidak tersedia")
    isContinue = input("Apakah Lanjut (y/n)?")
    if isContinue == "n":
        break

print("Program Selesai")
