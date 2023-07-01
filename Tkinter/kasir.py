from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Tokok Aisma')

# variable
ap = StringVar()
s = StringVar()
k = StringVar()
db = StringVar()
t_total = StringVar()
t_uang = StringVar()
total = 0

# funtion

def totalbeli():
	global ap, s, k, db, t_total, t_uang
	ha = int(ap.get()) * 189000
	hs = int(s.get()) * 165000
	hk = int(k.get()) * 123000
	hd = int(db.get()) * 119000

	total = ha + hs + hk + hd
	t_total.set(str(total))

def kembali():
	global total
	uang = int(t_uang.get())

	if uang >= total:
		kembali = uang - total
		messagebox.showinfo(message='kembalian anda sebesar{}'.format(str(kembali)))

def clear():
	ap.set('0')
	s.set('0')
	k.set('0')
	db.set('0')
	t_total.set('0')
	t_uang.set('0')

app.geometry('750x600')
app.configure(bg='Black')

Label(app, text='KASIR TOKO AISMA', 
	bg='#E9E4E3', foreground='#323232', font='arial 18 bold').place(x=200, y=30)

app.mainloop()