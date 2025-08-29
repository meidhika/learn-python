# Membuat Module Matematika dengan import

# lebih disarankan pakai ini, menggunakan import berdasarkan module
# from module_mtk import tambah, kali, pangkat

#menggunakan alias
from module_mtk import tambah as add
from module_mtk import kali as multiply
from module_mtk import pangkat as power

# bisa alias juga
import module_mtk as math 


#untuk mengambil semua fungsi di module mtk
# from module_mtk import *

hasil_tambah = add(1,2,3,4,5)
print(f"Hasil Tambah {hasil_tambah}")

hasil_kali = multiply(1,2,3,4,5)
print(f"Hasil kali {hasil_kali}")


pangkat_3 = power(3)
print(f"Hasil pangkat 3 {pangkat_3(5)}")