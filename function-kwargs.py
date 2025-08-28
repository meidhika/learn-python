''''Function **kwargs'''


def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''

fungsi("Meidhika", 170, 50)

def fungsi(**kwargs):
    '''fungsi biasa'''
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]   
    berat = kwargs["berat"]
    print(f"{nama} memiliki tinggi {tinggi} cm dan berat {berat} kg")


fungsi(nama="Meidhika", tinggi=170, berat=50)

#studi kasus

def math(*args, **kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output+=angka
    elif kwargs["option"] == "kurang":
        for angka in args:
            output-=angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output*=angka
    elif kwargs["option"] == "bagi":
        output = 1
        for angka in args:
            output/=angka
    else:
        print("tidak ada operasi")
    return output

hasil = math(1,2,3,4,5,6, option="tambah")   
print(f"hasil tambah {hasil}") 
hasil = math(1,2,3,4,5,6, option="kali")  
print(f"hasil kali {hasil}")  