#looping dari list


#for loop
# kumpulan_angka = [5,4,3,2,1,0]

# for angka in kumpulan_angka:
#     print(f"angka = {angka}")

# peserta = ["mei", "dhika", "nawa", "sapta"]
# for name in peserta :
#     print(f"peserta = {name}")


#for loop dan range
# kumpulan_angka = [10,9,8,7,6,5,4,3,2,1]
# panjang = len(kumpulan_angka)

# for i in range(panjang):
#     print(f"for loop angka = {kumpulan_angka[i]}") 


#while loop
kumpulan_angka = [10,9,8,7,6,5,4,3,2,1]
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
    print(f"while loop angka = {kumpulan_angka[i]}")
    i +=1



#list comprehension
data = ["meidhika", 1,2,3, "nawa", "sapta"]
[print(f"data={i}") for i in data]

angka = [10,9,8,7,6,5,4,3,2,1]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)



#enumerate
print("\nEnumerate")
data_list = ["meidhika", 1,2,3, "nawa", "sapta"]
for index,data in enumerate(data_list):
    print(f"index={index}, data={data}")