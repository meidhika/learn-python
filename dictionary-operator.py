#operator dictionary

data_dict = {
    "dh":"Dhika",
    "mei":"Meidhika",
    "sa":"Sapta",
    "na":"Nawa",
}

#menghitung panjang dictionary
lendict = len(data_dict)
print("panjang dictionary", lendict)

#mengecek apakah ada key tertentu pada dictionary
key = "mei"
chek_key = key in data_dict
print(f"apakah ada key, {key}, di dalam dictionary?, {chek_key}")

#mengakses value (read) dengan get
print(data_dict["mei"]) 
print(data_dict.get("dh"))
#check key dengan message error.
print(data_dict.get("nawa", "key tidak dapat ditemukan"))


#mengupdate data dictionary
data_dict["mei"] = "meimei"
print(data_dict)

#menambahkan key baru
data_dict["ucup"] = "Ucup"
print(data_dict)

data_dict.update({"test":"tester"}) #dapat membuat data baru kalau datanya tidak ada
data_dict.update({"sa":"saya"}) #dapat mengupdate data
print(data_dict)


#menghapus data
del data_dict["ucup"]
print(data_dict)