# segitiga sama kaki kanan

tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(tinggi):
    for j in range(i+0):
        print("*", end="")
    print("")

# segitiga sama kaki terbalik kanan
for i in range(tinggi, 0, -1):
    for j in range(tinggi):
        if j <= tinggi - i -1:
            print(" ", end="")
        else:
            print("*", end="")
    print("")


# sama kaki kiri

for i in range(tinggi):
    for j in range(tinggi):
        if j < tinggi - i -1:
            print(" ", end="")
        else:
            print("*", end="")
    print("")
       

    # segitiga sama kaki terbalik kiri

for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

   
print(" ")

print(" Dan ini segitiga sejajar ")

    # sama kaki kiri
for i in range(1, tinggi+1):
    for j in range(1, tinggi -i+1):
        print(end=" ")
    for j in range(1, i+1):
        print("*", end="")
    for j in range(1, i):
        print("*", end="")   
    print("")
       
for i in range(tinggi):
    for j in range(i):
        print(end=" ")
    for j in range(0,2 * (tinggi - i)-1):
        print("*", end="")

    print("")
