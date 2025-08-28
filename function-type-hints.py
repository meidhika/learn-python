''''Type hints untuk fungsi'''

#bentuk standar fungsi yang udah kita pelajari

## Studi Kasus
# def fungsi(parameter):
#     hasil = parameter**2
#     print(hasil)

# fungsi(1)
# fungsi("dhika")
# fungsi(True)

import string

# Penggunaan Type Hints

def fungsi_hints(parameter:int) -> int:
    hasil = parameter**2
    return hasil

hasil = fungsi_hints(5)
print(hasil)


def display(argument:string):
    print(argument)

display("Halo")
