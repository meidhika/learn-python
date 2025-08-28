#Default Argument

def hello_world(nama="ucup"):
    print(f"Hello {nama}")

nama = input("Siapa nama Anda? ")
hello_world(nama)



def sapa_dia (nama, pesan="Apa Kabar?" ):
    print(f"{pesan}, {nama}")

sapa_dia("ucup")


#contoh 3

def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print (hitung_pangkat(2, 3))

hasil = hitung_pangkat(angka=5, pangkat=3)
print(hasil)


# contoh 4

def fungsi(input1=1,input2=2, input3=3, input4=4, input5=5):
    hasil = input1 + input2 + input3 + input4 + input5
    return hasil


print(fungsi())