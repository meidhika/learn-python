data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0, data_1,10]
data_2D_copy = data_2D.copy()
# print("data 2D",data_2D)


#cara mengambil data dari nested list
# data = data_2D[0][0]
# print("data",data)

# print("data 2D copy",data_2D_copy)


#address semuanya
# print("address data 2D",hex(id(data_2D)))
# print("address data 2D copy",hex(id(data_2D_copy)))

# print("address dari member ke-1")
# print("address asli 2D",hex(id(data_2D[0])))
# print("address 2D copy",hex(id(data_2D_copy[0])))

#kita gunakan deepcopy

from copy import deepcopy
#copy secara recursive
data_2D = [data_0, data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"address asli = {hex(id(data_2D))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy))}")

print("address member ke 1")
print(f"address asli = {hex(id(data_2D[0]))}")
print(f"address deepcopy = {hex(id(data_2D_deepcopy[0]))}")


data_2D[1][0]=30
print(f"data = {data_2D}")
print(f"data copy = {data_2D_copy}")
print(f"data deepcopy = {data_2D_deepcopy}")


