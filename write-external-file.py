# 1. mode write, dia akan membuat file baru jika tidak ada lalu akan menimpa / overwrite isinya

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Meidhika Nawa Sapta")

with open("data_1.txt", "w", encoding="utf-8") as file:
    file.write("Hello World")


# 2. mode append

with open("data_3.txt", "a", encoding="utf-8") as file:
    file.write("Hello World\n" )
with open("data_3.txt", "a", encoding="utf-8") as file:
    file.write("Meidhika\n")
with open("data_3.txt", "a", encoding="utf-8") as file:
    file.write("Nawa Sapta\n")


# 3 mode r+
with open("data_4.txt", "w", encoding="utf-8") as file:
    file.write("data ke 4\n" )
    

with open("data_4.txt", "r+", encoding="utf-8") as file:
    file.write("menambah dengan r+ baris 1\n" )
    file.write("menambah dengan r+ baris 2\n" )

with open("data_4.txt", "r+", encoding="utf-8") as file:
    data = file.read()
    print(data)
    