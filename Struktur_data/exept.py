try:
    x = 10 / 0
except ZeroDivisionError:
    print("Maaf Tidak Bisa Noll")
except ValueError:
    print("Value Invalid")

while True:
	try:
		z = int(input("Input angka: "))
		a = int(input("Input angka: "))
		i = a / z
		break
	except ZeroDivisionError:
		print('Sorry!,Tidak Bisa hanya 0, Masukan Angka Selain 0!!')
	except ValueError:
		print("Sorry !, Masukan Angka!!")

print(i)
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