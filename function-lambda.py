# Lambda function

def f_kuadrat (angka):
    return angka ** 2
print (f"hasil fungsi kuadrat ={f_kuadrat(5)}")


#kita coba dengan lambda
#output = lambda argument: expression

kuadrat = lambda angka: angka ** 2
print (f"hasil lambda kuadrat = {kuadrat(10)}")


pangkat = lambda num,pow: num ** pow
print (f"hasil lambda pangkat = {pangkat(2,3)}")


## kegunaan lambda
#sorting untuk list

angka = [1, 4, 5, 2, 1, 9, 7, 4, 6, 10]
angka.sort()
print (f"sorted angka = {angka}")


data_list = ["dhika", "agung", "sapta", "mei"]
data_list.sort()
print (f"sorted data = {data_list}")


#sorting pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print (f"sorted data list pakai len = {data_list}")


# sort pakai lambda
data_list = ["dhika", "agung", "sapta", "mei"]
data_list.sort(key=lambda nama: len(nama))
print (f"sorted data list pakai lambda = {data_list}")


# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12,13]
#cari angka genap
data_genap = list(filter(lambda x: x % 2 == 0, data_angka))
print (f"data genap = {data_genap}")

#cari angka ganjil
data_ganjil = list(filter(lambda x: x % 2 == 1, data_angka))
print (f"data ganjil = {data_ganjil}")


def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima, data_angka))
print (f"data kurang dari lima = {data_angka_baru}")


data_angka_baru_lagi = list(filter(lambda x: x < 5, data_angka))
print (f"data kurang dari lima pakai lambda = {data_angka_baru_lagi}")

data_kelipatan_3 = list(filter(lambda x: x % 3 == 0, data_angka))
print (f"data kelipatan 3 = {data_kelipatan_3}")
