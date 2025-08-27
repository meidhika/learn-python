#If dan Else Statement

#1. if
#2. kondisi
#3. aksi

# nama = input("Siapa nama Anda? ")

#1. program if inline
# if nama == "ucup": print("Hallo, apa kabar?")
# print("Senang bertemu denganmu ")

#2. program if identation
# if nama == "asep":
#     print(f"Hallo, apa kabar {nama}?")
#     print("Senang bertemu denganmu ")
# print("ini adalah akhir dari program")


#3. Else Statement
# if nama == "ucup":
#     print(f"Hallo, apa kabar {nama}?")
#     print(f"Senang bertemu denganmu {nama} ")
# else:
#     print("Ah, siapa kamu?")
# print("ini adalah akhir dari program")

#4. Elif Statement
# if nama == "ucup": #kondisi 1
#     print(f"Hallo, apa kabar {nama}?")
# elif nama == "asep": #kondisi 2
#     print(f"ohhh kamu {nama}, apa kabar {nama}?")
# else: #kondisi else
#     print("Ah, siapa kamu?")
# print("ini adalah akhir dari program")


#5. If bersarang (nested if)
# if nama == "ucup": #kondisi 1
#     print(f"Hallo, apa kabar {nama}?")
#     if nama == "ucup":
#         print(f"Senang bertemu denganmu {nama} ")
# else: #kondisi else
#     print("Ah, siapa kamu?")
# print("ini adalah akhir dari program")


#Latihan Kalkulator Sederhana
print("Kalkulator Sederhana")
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Masukkan operator (+, -, *, /): ")

if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasil: {angka1} + {angka2} = {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasil: {angka1} - {angka2} = {hasil}")
elif operator == "*":
    hasil = angka1 * angka2
    print(f"Hasil: {angka1} * {angka2} = {hasil}")
elif operator == "/":
    if angka2 != 0:
        hasil = angka1 / angka2
        print(f"Hasil: {angka1} / {angka2} = {hasil}")
    else:
        print("Error: Pembagian dengan nol tidak diperbolehkan.")
else:
    print("Error: Operator tidak dikenali.")