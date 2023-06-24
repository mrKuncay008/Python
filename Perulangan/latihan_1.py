# membuat urutan angka ganjil

for a in range(0, 100):
	if a % 2 != 0:
		print(a)
# output:
# 1
# 3
# 5
# ...
# 99

# membuat urutan angka genap

for a in range(0, 100):
	if a % 2 != 1:
		print(a)
# output:
# 0
# 2
# 4
# ...
# 98

# looping untuk memanggil nama dari simbol
for ch in "411221049@mahasiswa.undira.ac.id":
    if ch == "@":
        break
    print(ch, end=" ")

# output:
# 411221049

# looping untuk memisahkan char dan di ganti 
for digit in "0165031806510":
    if digit == "0":
        print(" x ", end="")
        continue
    print(digit, end="")

    # outpu : 
    # x 165 x 318 x 651 x 

 # bonus
n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

# list array
numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.
 
numbers[1] = 111
print("New list contents: ", numbers)  # Current list contents.
 
# output
#  Original list contents: [10, 5, 7, 2, 1]
# New list contents:  [10, 111, 7, 2, 1]

# array 0 atau kosong
my_list = []  # Creating an empty list.
for i in range(10):
    if my_list.append(i + 1)

print(my_list)

# array terbalik
my_list = []  # Creating an empty list.
 
for i in range(10):
    my_list.insert(0, i + 1)
 
print(my_list)

