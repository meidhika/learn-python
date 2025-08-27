#list -> array, mengakses data dengan menggunakan index
data_list = [1,2,3,4,5]
print(data_list[1])

#Dictionary (dict) -> associative array, mengakses data dengan menggunakan key/identifier
data_dict = {
    "name" : "Ucup",
    "age" : 10,
    "gender" : "Laki-laki",
    "list": data_list,
    "dict":{
        "dict1": "value1",
        "dict2": "value2"
    }
}
print(data_dict["dict"])

