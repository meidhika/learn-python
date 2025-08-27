#membuat gabungan area rentang dari angka

inputUser = float(input("masukkan angka yang bernilai \nkurang dari 3  \natau \nlebih besar dari 10  : "))

isKurangDari3 = inputUser < 3
print("kurang dari 3 =", isKurangDari3)



isLebihDari10 = inputUser > 10
print("lebih dari 10 =", isLebihDari10)

#+++++++3--------10+++++++++
isCorrect = isKurangDari3 or isLebihDari10
print("angka yang anda masukkan  =", isCorrect)



#kasus irisan area rentang dari angka
#---------3+++++++++10-------------
inputUser = float(input("masukkan angka yang bernilai \nlebih dari 3  \ndan \nkurang dari 10  : "))

isLebihDari3 = inputUser > 3
print("lebih dari 3 =", isLebihDari3)

isKurangDari10 = inputUser < 10
print("kurang dari 10 =", isKurangDari10)

isCorrect = isLebihDari3 and isKurangDari10
print("angka yang anda masukkan 2 =", isCorrect)