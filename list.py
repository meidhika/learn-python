#-------------List /Array Methods in Python----------------#

#kumpulan data numbers
numbers = [1, 2, 3, 4, 5]
print("Data numbers awal: ", numbers)

#kumpulan data string
fruits = ['apple', 'banana', 'cherry']
print("Data fruits awal: ", fruits)

#kumpulan data boolean
booleans = [True, False, True]
print("Data booleans awal: ", booleans)

#kumpulan data campuran
mixed = [1, 'apple', True, 3.14]
print("Data mixed awal: ", mixed)

#cara alternatif membuat list
data_range = range(0,10, 2) #start, stop, step
print(data_range)
data_list = list(data_range)
print("Data list dari range: ", data_list)

#membuat list dengan for loop, list comprehension
data_list_for = [i for i in range(0,10)]
print("Data list dari for loop: ", data_list_for)


#membuat list pake for pake if
data_list_for_if = [i for i in range(0,10) if i % 2 == 0]
print("Data list dari for loop dengan if: ", data_list_for_if)