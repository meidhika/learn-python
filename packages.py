import time

t_start = time.time()
import sains.matematika
#bisa seperti ini
from sains import fisika
#bisa seperti ini juga
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1,2,3,4,5)
print(f"Hasil Tambah {hasil_tambah}")

t_end = time.time()
print(f"Waktu eksekusi: {t_end - t_start}")


gaya = fisika.gaya(90,20)
print(f"Gaya adalah: {gaya}")

gaya = force(80,20)
print(f"Gaya adalah: {gaya}")