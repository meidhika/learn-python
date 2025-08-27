import datetime as dt
hari_ini = dt.date.today()
print("Hari ini tanggal:", hari_ini)

print(f"hari ini adalah: {hari_ini:%A}" )


tanggal = dt.date(2024, 12, 25)
print("Tanggal:", tanggal)



print("silahkan masukkan tanggal, bulan, dan tahun lahir Anda")
tgl = int(input("Tanggal (dd): "))
bln = int(input("Bulan (mm): "))
thn = int(input("Tahun (yyyy): "))

tanggal_lahir = dt.date(thn, bln, tgl)
print(f"Tanggal lahir Anda adalah: {tanggal_lahir:%A}" )

hari_ini = dt.date.today()
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365
print(f"Hari Lahir Anda adalah: {tanggal_lahir:%A} hari")
print(f"Umur Anda adalah: {umur_tahun} tahun")