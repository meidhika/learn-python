#Membuat Fungsi Dengan Argument

'''
def nama_fungsi(argument):
    #function body
    aksi
'''

def hello_world(nama):
    #function body
    print(f"Hello {nama}")

hello_world("ucup")
hello_world("asep")



#program tambah

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")

tambah(10, 20)
# tambah(100, 200)


def say_hi(list_peserta):
    for peserta in list_peserta:
        print(f"halo {peserta}")


anggota = ["dhika", "nawa", "sapta"]
say_hi(anggota)