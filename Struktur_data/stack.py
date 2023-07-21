kucing = []

# Stack Structur data python

kucing.append("mansur")
kucing.append("Kuncay")
kucing.append("Itam")
x = input("Apa Ada kucing yang sudah tiada ?")
if x in kucing:
    kucing.remove(x)
print(kucing)

baju = ["itam","Merah","Hijau"]
print("")

print("Lemari Baju Ku !!!\n")
print(baju)

nambah = ["Biru","Orange","Kuning"]
baju.append(nambah)
print(baju)
baju.pop()
print(baju)