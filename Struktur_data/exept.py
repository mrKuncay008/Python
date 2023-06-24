while True:
	try:
		a = int(input("Input angka: "))	
		z = int(input("Input angka: "))
		break
	except ValueError:
		print("Sorry !, Masukan Angka!!")
	except ZeroDivisionError:
		print("Sorry!,Tidak Bisa hanya 0, Masukan Angka Selain 0!!")

x = a * z
print("Hasil nya: ", x)

# from datetime import datetime as dt

# tgl = False

# while not tgl:
#     date_input = input("Input Tanggal Lahir (dd mm yyyy): \n")
#     try:
#         tgl_lahir = dt.strptime(date_input, '%d %m %Y')
#         tgl = True
#     except ValueError:
#         print("Format tanggal salah. Coba lagi!")

# current_time = dt.now().strftime("%H:%M:%S")       

# print("Tanggal Lahir:", tgl_lahir.strftime("%d %B %Y"))
# print("Waktu Saat ini: ", current_time)