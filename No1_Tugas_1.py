# Buatlah Implementasi Tipe Data, Variabel, Operator, dan Operasi I/O pada Python
# MUHAMMAD FRENDI ARAHMAN_411221049


# - Definisi Implementasi Tipe data
# Tipe data String / str
var_a = "Saya Sedang Belajar Python"
var_b = 'Python Yang Sedang Saya Pelajari'

print(str(var_a))
print(str(var_b))
#output : 
# Saya Sedang Belajar Python
# Python Yang Sedang Saya Pelajari

# Tipe data Intreger / int
var_a = 20
var_b = 12

print(int(var_a))
print(int(var_b))
#output : 
# 20
# 12


# Tipe data Float / float
var_a = 20
var_b = 12

print(float(var_a))
print(float(var_b))
#output : 
# 20.0
# 12.0


# Tipe data Boolean / bool
var_a = (20 == 12)
var_b = (20 > 12)

print(bool(var_a))
print(bool(var_b))
#output : 
# False
# True


# - definisi implementasi Variable
var1 = "Saya Suka Belajar"
var2 = "Python"
print(var1, var2)
# Output :
# Saya Suka Belajar Python

#-------------------------------#


# - Definisi Implementasi Operasi dan I/O (input outpu)
a = int(input('Masukan jumlah a: '))
b = int(input('Masukan jumlah b: '))

jumlah = a + b #penjumlhan
kurang = a - b #pengkurangan
kali = a * b #pengkalian
bilbulat = b // b #pembagian
pangkat = a ** 3 #pangkat

print("Hasil penjumlahan = ", jumlah)
print("Hasil pengurangan = ", kurang)
print("Hasil pengkalian= ", kali)
print("Hasil pembagian = ", bilbulat)
print("Hasil pangkat = ", pangkat)

#output 
# Masukan jumlah a: 23
# Masukan jumlah b: 25
# Hasil penjumlahan =  48
# Hasil pengurangan =  -2
# Hasil pengkalian=  575
# Hasil pembagian =  1
# Hasil pangkat =  12167
