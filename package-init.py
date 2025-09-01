import sains
from sains.matematika import scientific

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil Tambah {hasil_tambah}")

hasil_fisika = sains.fisika.gaya(90,20)
print(f"Gaya adalah: {hasil_fisika}")


hasil_kali = sains.matematika.kali(1,2,3,4,5)
print(f"Hasil kali {hasil_kali}")

hasil_pangkat = scientific.pangkat(3) 
print(f"Hasil pangkat 3 {hasil_pangkat(5)}")



# from sains import *

# hasil_tambah = matematika.basic.tambah(1,2,3,4,5)
# print(f"Hasil Tambah {hasil_tambah}")

# hasil_fisika = fisika.gaya(90,20)
# print(f"Gaya adalah: {hasil_fisika}")


# hasil_kali = matematika.basic.kali(1,2,3,4,5)
# print(f"Hasil kali {hasil_kali}")