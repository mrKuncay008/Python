# step 1:
Beatles = []
print("Langkah pertama: kosong !")

# step 2:

Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Langkah ke-2:", Beatles)

# step 3:
for members in range(1):
    Beatles.append(input("New band member: "))
print("Langkah ke-3:", Beatles)

# step 4:
del Beatles[-1]
del Beatles[-1]
print("Langkah ke-4:", Beatles)

# step 5:
Beatles.insert(0, members)
print("Langkah ke-5:", Beatles)
print("Mantap Band:",len(Beatles))

# kode ini adalah gambaran Algoritma bubleshort