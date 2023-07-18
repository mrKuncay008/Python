kucing = []

# Stack Structur data python

kucing.append("mansur")
kucing.append("Kuncay")
kucing.append("Itam")
x = input("Apa Ada kucing yang sudah tiada ?")
if x in kucing:
    kucing.remove(x)
print(kucing)
