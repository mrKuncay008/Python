from tkinter import *
from tkinter import messagebox

app = Tk()
app.title('Aplikasi Toko Buku Pren')

# variable
ap = IntVar()
s = IntVar()
k = IntVar()
db = IntVar()
t_total = IntVar()
t_uang = IntVar()
subtotal = IntVar()
ppn = IntVar()
total = 0

# funtion

def totalbeli():
	global ap, s, k, db, t_total, t_uang, total
	ha = ap.get() * 189000
	hs = s.get() * 165000
	hk = k.get() * 123000
	hd = db.get() * 119000

	subtotal = ha + hs + hk + hd
	ppn = subtotal * 0.11
	total = subtotal + ppn
	t_total.set(total)
	

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

# ===== UI Design =+====

# Ukuran dan Background Warna 

app.geometry('750x600')
app.configure(bg='#E7D9D6')
# Judul
Label(app, text='KASIR TOKO BUKU PREN', 
	 font='arial 18 bold italic').place(x=200, y=30)
# Label Menu

# 1 buku algoritma
Label(app, text = '1) Algoritma Dan Pemograman', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=100,y=100)
# 2 Buku Struktur data
Label(app, text = '2) Struktur data', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=100,y=140)
# 3 Buku Keamanan sistem
Label(app, text = '3) Keamanan Sistem', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=100,y=180)
# 4 buku Dataabse
Label(app, text = '4) Database', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=100,y=220)

# Label Harga
Label(app, text = '189.000', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=350,y=100)

Label(app, text = '165.000', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=350,y=140)

Label(app, text = '123.000', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=350,y=180)

Label(app, text = '119.000', bg='white', foreground='#3D3D3D',font='arial 12 bold').place(x=350,y=220)

# Spinbox
Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=ap,command=totalbeli).place(x=550, y=100)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=s,command=totalbeli).place(x=550, y=140)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=k,command=totalbeli).place(x=550, y=180)

Spinbox(app, from_=0,to=100,width=4,font='arial 10',textvariable=db,command=totalbeli).place(x=550, y=220)
# Jumlah Total Harga
Label(app, text='Jumlah Total: ', bg='black',fg='white',font='arial 13 bold italic').place(x=450,y=260)

Label(app, text='Rp.', font='arial 13 bold').place(x=450,y=290)

Label(app, textvariable=t_total, font='arial 13 bold').place(x=475,y=290)

# PPN

Label(app, text='PPN (11 %) ').place(x=450, y=350)
# Label(app, text='Rp', textvariable=subtotal, fg='black', font='arial 13').place(x=450,y=400)

# Laber Pembayaran
Label(app,text='Masukan Uang Anda',foreground='black',font='arial 12 bold').place(x= 210,y=260)

# Entry Jumlah Uang
Entry(app,textvariable=t_uang).place(x= 200, y = 300)

# Label Total
Label(app,text='Rp. ',foreground='black',font='arial 12 bold').place(x=165, y=300)

# Button
Button(app,text='Enter',bg='white',foreground='black',font='arial 12 bold',width=5, command=kembali).place(x=165, y=330)

# Footer text
Label(app, text='Created By Muhammad Frendi Arahman 4112210', foreground='dark red' ,font='arial 15 bold').place(x=190, y=490)
app.mainloop()