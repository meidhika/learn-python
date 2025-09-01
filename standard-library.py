# Menggunakan package/library yang sudah ada di python

import datetime

data_waktu = datetime.datetime.now()
print(f"datetime now: {data_waktu}")
print(f"Tahun : {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")


from collections import Counter

data = [1,1,1,2,2,3,3,3,3,4,4,4,4]
counter = Counter(data)
print(counter)

data_alphabet = ["a", "b", "c","d","e", "a", "g","c"]
count_alphabet = Counter(data_alphabet)
print(f"data count alphabet: {count_alphabet}")
print(f"data count alphabet: {count_alphabet['a']}")


import io 
file = io.open("file_text.txt", "r")
print(file.read())


