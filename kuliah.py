# #mencari lua persegi panjang

# panjang = 20
# lebar = 10
# tinggi = 3

# luas = panjang * lebar * tinggi

# print("Hasil Luas persegi adalah : " , luas)

# artimatika
a = int(input('Masukan jumlah a: '))
b = int(input('Masukan jumlah b: '))

jumlah = a + b
kurang = a - b
kali = a * b
bilbulat = b // b
pangkat = a ** 3

print("Hasil = ", jumlah)

print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

x = float(input("Enter value for x: "))
y = 1./(x + 1./(x + 1./(x + 1./x)))
print("y =", y)

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
mins = mins + dura # find a total of all minutes
hour = hour + mins // 60 # find a number of hours hidden in minutes and update the hour
mins = mins % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", mins, sep='')


print(1 // 2 * 3)

x = 1
y = 2
z = x
x = y
y = z
print(x, y)

x = input()
y = input()
print(x + y)

x = int(input())
y = int(input())

x = x // y
y = y // x

print(y)

x = int(input())
y = int(input())

x = x / y
y = y / x

print(y)

x = int(input())
y = int(input())

x = x % y
x = x % y
y = y % x

print(y)

x = input()
y = int(input())

print(x * y)

z = y = x = 1
print(x, y, z, sep='*')

x = 1 / 2 + 3 // 3 + 4 ** 2
print(x)

x = int(input())
y = int(input())

print(x + y)

