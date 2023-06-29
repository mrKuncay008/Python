teks = input("Masukan Pesan: ")

jarak = 0

while jarak == 0:
	try:
		jarak = int(input("Masukan jarak [1..5]"))
		if jarak not in range(1, 6):
			raise ValueError
	except ValueError:
		jarak = 0
		if jarak == 0:
			print("Value salah !!")

code = ''
for char in teks:
	if char.isalpha():
		cod = ord(char) + jarak

		if char.isupper():
			pertama = ord('A')
		else:
			pertama = ord('a')

		cod -= pertama
		cod %= 6

		code += chr(pertama + cod)
	else:
		code += char

print(code)