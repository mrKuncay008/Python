import os
import time

class Kucing: # class
	def kuncay(): # Object
		print("mememewo") # input 
	
	def sumbul():
		print("mawooww")

	def itam():
		try:
			print(itam)
		except NameError:
			print("Maaf Itam dah meninggal :(")
# Output
print(Kucing.kuncay())

# dengan menggunakan class init dan self

y = input("Tekan Y untuk lanjut: ")
if y == 'y':
	os.system('clear')
	os.system('cls')
	time.sleep(1)

class Sapi:
	def __init__(self, jenis, berat):
		
		self.jenis = jenis

		self.berat = berat
	
	def jenis():
		print(self.jenis)

	def berat():
		print(self.berat)

qurban = Sapi("Lokal", "20 kg")

print(f"""Tanggal 29 juni idul adha Telah berkurban Seekor sapi {qurban.jenis}.
	Dengan Berat {qurban.berat} Alhamdulillah""")