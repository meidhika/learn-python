import datetime
import os
import string
import random
#template dict mahasiswa

mahasiswa_template ={
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,11,11)
}

data_mahasiswa ={}

while True:
    os.system('cls') #untuk windows
    print(f"{'Selamat Datang':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print(f"{'-'*20}")

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa: ")
    mahasiswa['nim'] = input("NIM Mahasiswa: ")
    mahasiswa['sks_lulus'] = int(input("SKS Lulus Mahasiswa: "))
    TAHUN_LAHIR = int(input("Tahun Lahir Mahasiswa (YYYY): "))
    BULAN_LAHIR = int(input("Bulan Lahir Mahasiswa (MM): "))
    TANGGAL_LAHIR = int(input("Tanggal Lahir Mahasiswa (DD): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    print(f"{'KEY':<6} {'Nama':<10} {'SKS':<6}{'Lahir':<10}")
    print(f"{'-'*50}")
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        Nama = data_mahasiswa[KEY]["nama"]
        SKS = data_mahasiswa[KEY]["sks_lulus"]
        Lahir = data_mahasiswa[KEY]["lahir"].strftime("%x")

        print(f"{KEY:<6} {Nama:<10} {SKS:<6}  {Lahir}")

    lanjut = input("\nIngin menambahkan data mahasiswa lagi? (y/n) : ")
    if lanjut == "n":
        break



