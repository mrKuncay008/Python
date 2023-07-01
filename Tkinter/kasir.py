from tkinter import *
from tkinter import messagebox
import locale

app = Tk()
app.title('Aplikasi Toko Buku Pren')

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
	global total
	total = ha + hs + hk + hd
	t_total.set(locale.format_string("%d", total, grouping=True))

def kembali():
	global total
	uang = int(t_uang.get())

	if uang >= total:
		kembali = uang - total
		messagebox.showinfo(message='kembalian anda sebesar{}'.format(kembali))

def clear():
	ap.set('0')
	s.set('0')
	k.set('0')
	db.set('0')
	t_total.set('0')
	t_uang.set('0')

# ===== UI Design =+====

locale.setlocale(locale.LC_ALL, '')
# Ukuran dan Background Warna 

app.geometry('750x600')
app.configure(bg='Blue')
# Judul
Label(app, text='KASIR TOKO BUKU PREN', 
	bg='#E9E4E3', foreground='#323232', font='arial 18 bold').place(x=200, y=30)
# Label Menu

# 1 buku algoritma
Label(app, text = '1 Algoritma Dan Pemograman', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=100,y=100)
# 2 Buku Struktur data
Label(app, text = '2 Struktur data', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=100,y=140)
# 3 Buku Keamanan sistem
Label(app, text = '3 Keamanan Sistem', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=100,y=180)
# 4 buku Dataabse
Label(app, text = '4 Database', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=100,y=220)

# Label Harga
Label(app, text = '189.000', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=350,y=100)

Label(app, text = '165.000', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=350,y=140)

Label(app, text = '123.000', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=350,y=180)

Label(app, text = '119.000', bg='#31c6d4', foreground='#fef5ac',font='arial 12 bold').place(x=350,y=220)

# Spinbox
Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=ap,command=totalbeli).place(x=550, y=100)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=s,command=totalbeli).place(x=550, y=140)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=k,command=totalbeli).place(x=550, y=180)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=db,command=totalbeli).place(x=550, y=220)

# Laber Pembayaran
Label(app,text='Masukan Uang Anda', bg='#31c6d4',foreground='#fef5ac',font='arial 12').place(x= 200,y=280)

# Entry Jumlah Uang
Entry(app,textvariable=t_uang).place(x= 200, y = 300)

# Label Total
Label(app,text='Rp. ',bg='#31c6d4',foreground='#fef5ac',font='arial 12 bold').place(x=165, y=300)

# Button
Button(app,text='Total',bg='white',foreground='black',font='arial 12 bold',width=10, command=kembali).place(x=165, y=320)
app.mainloop()