dic = {
	"cat" : "chat",
	"dog" : "Chien",
	"horse" : "Cheval"
}

phone = {'boss' : 1283890, 'Suyz' : 2221837289}

kosong = {}

print(dic['cat'])
print(phone['boss'])
print(kosong)

smt = {
	"AP2" : "Algoritma dan pemograman 2",
	"KSI" : "Kewirausahan",
	"STD" : "Struktur data"
}

for kuliah in smt :
	print(smt)

keys = smt.keys()
print(keys)

for key in smt.keys():
	print(smt.get(key))
values = smt.values()
print(values)

item = smt.item()
print(item)

for items in smt.item():
	print(items)

for key, value in smt.item():
	print(f"Kuncinya = {key}, value = {value}")

smt = {
	"AP2" : "Algoritma dan pemograman 2",
	"KSI" : "Kewirausahan",
	"STD" : "Struktur data"
}

mk = smt.copy()
print(f"Matakuliah: {smt}\n")
print(f"Matakuliah: {mk}\n")

smt["AP2"] = "Algoritma dan pemograman 2"
print(f"Matakuliah = {smt}\n")
print(f"Matakuliah = {mk}\n")