import datetime as dt
mahasiswa1 ={
    "nama":"Meidhika",
    "nim":"12345678",
    "sks_lulus":130,
    "beasiswa":False,
    "lahir":dt.datetime(2025,8,27)
}


mahasiswa2 ={
    "nama":"Nawa",
    "nim":"1234567899",
    "sks_lulus":150,
    "beasiswa":True,
    "lahir":dt.datetime(2024,8,1)
}

mahasiswa3 ={
    "nama":"Sapta",
    "nim":"1234500",
    "sks_lulus":100,
    "beasiswa":True,
    "lahir":dt.datetime(2023,8,20)
}


data_mahasiswa = {
    "M1":mahasiswa1,
    "M2":mahasiswa2,
    "M3":mahasiswa3
}

print(f"{'KEY':<6} {'Nama':<10} {'SKS':<6} {'Beasiswa':<10} {'Lahir':<10}")
print(f"{'-'*50}")

for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    Nama = data_mahasiswa[KEY]["nama"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    Beasiswa = data_mahasiswa[KEY]["beasiswa"]
    Lahir = data_mahasiswa[KEY]["lahir"].strftime("%x")

    print(f"{KEY:<6} {Nama:<10} {SKS:<6} {Beasiswa:^10} {Lahir}")