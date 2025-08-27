import datetime
import os
#template dict mahasiswa

mahasiswa_template ={
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,11,11)
}

data_mahasiswa ={}


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
print(mahasiswa)



