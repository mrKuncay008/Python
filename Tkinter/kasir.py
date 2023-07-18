from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Toko Buku Pren')

# variable dan Jenis buku
ap = IntVar()
s = IntVar()
k = IntVar()
db = IntVar()
pp, dj, cm, sf, tc, dw = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
# =========================
t_total = StringVar()
t_uang = IntVar()
subtotal = IntVar()
t_sub = StringVar()
ppn = IntVar()
total = 0

# funtion

def totalbeli():
	global ap, s, k, db, pp, dj, cm, sf, tc, dw, t_total, t_uang, total, subtotal, t_sub
	ha = ap.get() * 189000
	hs = s.get() * 165000
	hk = k.get() * 123000
	hd = db.get() * 119000
	hp = pp.get() * 115000
	hdj = dj.get() * 100000 
	hcm = cm.get() * 150000
	hsf = sf.get() * 120000
	htc = tc.get() * 110000
	hdw = dw.get() * 196000

	subtotal = ha + hs + hk + hd + hp + hdj + hcm + hsf + htc + hdw
	ppn = subtotal * 0.11
	total = subtotal + ppn
	t_total.set(total)
	t_sub.set(subtotal)

def kembali():
	global total
	uang = t_uang.get()

	if uang >= total:
		kembali = uang - total
		messagebox.showinfo(message='KEMBALIAN Rp.{}'.format(kembali))

def clear():
	ap.set('0')
	s.set('0')
	k.set('0')
	db.set('0')
	t_total.set('0')
	t_uang.set('0')
	pp.set('0')
	dj.set('0')
	cm.set('0')
	sf.set('0')
	tc.set('0')
	dw.set('0')

# ===== UI Design =+====

# Ukuran dan Background Warna 

app.geometry('750x600')
app.configure(bg='#E7D9D6')
# Judul
Label(app, text='KASIR TOKO BUKU PREN', 
	 font='arial 18 bold italic').place(x=200, y=30)
# Label Menu

# 1 buku algoritma
Label(app, text = '1) Algoritma Dan Pemograman', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=100)
# 2 Buku Struktur data
Label(app, text = '2) Struktur data', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=120)
# 3 Buku Keamanan sistem
Label(app, text = '3) Keamanan Sistem', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=140)
# 4 buku Dataabse
Label(app, text = '4) Database', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=160)

Label(app, text = '5) Pemograman Python', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=180)

Label(app, text = '6) Dasar-Dasar Jaringan', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=200)

Label(app, text = '7) Indahnya Masuk Surga', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=220)

Label(app, text = '8) Sistem Formasi', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=240)

Label(app, text = '9) Tata cara Sholat Lengkap', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=260)

Label(app, text = '10) 10 cara Design Web', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=100,y=280)

# Label Harga
Label(app, text = '189.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=100)

Label(app, text = '165.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=120)

Label(app, text = '123.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=140)

Label(app, text = '119.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=160)

Label(app, text = '115.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=180)

Label(app, text = '100.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=200)

Label(app, text = '150.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=220)

Label(app, text = '120.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=240)

Label(app, text = '110.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=260)

Label(app, text = '196.000', bg='white', foreground='#3D3D3D',font='arial 8 bold').place(x=350,y=280)

# Spinbox
Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=ap,command=totalbeli).place(x=550, y=100)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=s,command=totalbeli).place(x=550, y=120)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=k,command=totalbeli).place(x=550, y=140)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=db,command=totalbeli).place(x=550, y=160)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=pp,command=totalbeli).place(x=550, y=180)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=dj,command=totalbeli).place(x=550, y=200)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=cm,command=totalbeli).place(x=550, y=220)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=sf,command=totalbeli).place(x=550, y=240)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=tc,command=totalbeli).place(x=550, y=260)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=dw,command=totalbeli).place(x=550, y=280)
# Jumlah Total Harga
Label(app, text='Jumlah Total: ', bg='black',fg='white',font='arial 10 bold italic').place(x=570,y=320)

Label(app, text='Rp.',bg='blue',fg='white',font='arial 9 bold').place(x=555,y=342)

# Input uang dan clear
Label(app, textvariable=t_total, bg='blue', fg='white',font='arial 9 bold').place(x=580,y=342)
Button(app,text='ENTER',bg='white',foreground='black',font='arial 7 bold',width=5, command=kembali).place(x=100, y=365)
Button(app,text='CLEAR',bg='red',foreground='white',font='arial 7 bold',width=5, command=clear).place(x=145, y=365)

# PPN

Label(app, text='PPN (11 %) ',bg='#E7D9D6',font='arial 10 bold').place(x=450, y=320)
Label(app, text='Subtotal:', font='arial 9 bold',bg='#E7D9D6').place(x=450,y=340)
Label(app, text='Rp', textvariable=t_sub, fg='black', font='arial 9 bold',bg='#E7D9D6').place(x=450,y=360)
Label(app, text='Rp', fg='black', font='arial 9 bold',bg='#E7D9D6').place(x=430,y=360)

# Laber Pembayaran
Label(app,text='Masukan Uang Anda',bg='#E7D9D6',foreground='black',font='arial 12 bold').place(x= 100,y=320)

# Entry Jumlah Uang
Entry(app,textvariable=t_uang).place(x= 100, y = 340)
# Footer text
Label(app, text='Created By Muhammad Frendi Arahman 4112210', foreground='dark red' ,font='arial 15 bold').place(x=190, y=490)
app.mainloop()