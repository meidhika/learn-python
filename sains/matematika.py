'''Module Matematika'''


def tambah(*args):
    '''Fungsi untuk menghitung penjumlahan'''
    hasil = 0
    for angka in args:
        hasil += angka
    return hasil

def kali(*args):
    '''Fungsi untuk menghitung perkalian'''
    hasil = 1
    for angka in args:
        hasil *= angka
    return hasil

def pangkat(n):
    '''Fungsi untuk menghitung pangkat'''
    return lambda angka: angka ** n