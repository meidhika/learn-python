# *args


# Memasukkan data/argument

def fungsi(nama, tinggi, berat):
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Meidhika", 167.5, 50)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi(["Dhika", 167.5, 50])


# kenalan dengan *args (argumen):

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")

fungsi("Nawa", 167.5, 50)


# studi kasus

def tambah (*data):
    #data tipenya adalah tuple dan ia dapat diiterasi
    output = 0
    for angka in data:
        output += angka
    return output


hasil = tambah(1, 2, 3, 4, 5,6,7,8,9,10)
print(f"Hasil: {hasil}")