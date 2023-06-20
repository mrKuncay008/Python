# Pernyataan break digunakan untuk keluar/mengakhiri sebuah loop.

# Rancang program yang menggunakan perulangan while dan terus-menerus meminta pengguna untuk memasukkan kata kecuali
# jika pengguna memasukkan "chupacabra" sebagai kata keluar rahasia, dalam hal ini pesan "Anda telah berhasil keluar dari perulangan." harus dicetak ke layar,
# dan loop harus dihentikan.
# Jangan cetak kata apa pun yang dimasukkan oleh pengguna. Gunakan konsep eksekusi bersyarat dan pernyataan break.

while True:
	word = input("Masukan Kata : ")

	if word == "Chapibara":
		print("Anda telah berhasil keluar dari perulangan.")
		break
	else:
		print("Kata salah, Coba lagi !!")