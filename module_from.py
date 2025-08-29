# Membuat Module Matematika dengan import

from module_mtk import tambah, kali, pangkat
#untuk mengambil semua fungsi di module mtk
from module_mtk import *

hasil_tambah = tambah(1,2,3,4,5)
print(f"Hasil Tambah {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"Hasil kali {hasil_kali}")


pangkat_3 = pangkat(3)
print(f"Hasil pangkat 3 {pangkat_3(5)}")