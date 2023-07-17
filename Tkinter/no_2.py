import tkinter as tk
from tkinter import messagebox

# Data Fakultas dan Program Studi
fakultas = {
    "FILKOM": ["Teknik Informatika", "Sistem Informasi", "Sistem Komputer", "Manajemen Informatika", "Rekayasa Perangkat Lunak"],
    "FT": ["Teknik Industri", "Teknik Mesin", "Teknik Kimia", "Teknik Nuklir", "Teknik Elektro"],
    "FKIP": ["Matematika", "Biologi", "Bahasa Inggris", "Bahasa Jerman", "Fisika"]
}

# Data Biaya Pendaftaran
biaya_pendaftaran = {
    "FILKOM": 500000,
    "FT": 500000,
    "FKIP": 350000
}

# Data Biaya Program Studi
biaya_program_studi = {
    "TI": 14000000,
    "SK": 14000000,
    "RPL": 14000000,
    "SI": 10000000,
    "MI": 10000000,
    "TInd": 13000000,
    "TM": 13000000,
    "TK": 13000000,
    "TN": 13000000,
    "TE": 13000000,
    "MTK": 6700000,
    "BIO": 6700000,
    "Bing": 6700000,
    "BJ": 6700000,
    "FS": 6700000
}

# Data Potongan Beasiswa
potongan_beasiswa = {
    "Raport": 0.05,
    "Prestasi": 0.06,
    "Bidikmisi": 0.08
}

# Inisialisasi variabel global
nisn = ""
nama = ""
alamat = ""
fakultas_pilihan = ""
program_studi_pilihan = ""
total_pembayaran = 0
bayar = 0

def submit_biodata():
    global nisn, nama, alamat
    nisn = entry_nisn.get()
    nama = entry_nama.get()
    alamat = entry_alamat.get()
    messagebox.showinfo(message="Biodata berhasil disimpan!")

def select_fakultas():
    global fakultas_pilihan
    fakultas_pilihan = entry_fakultas.get()
    if fakultas_pilihan in fakultas:
        program_studi_list = "\n".join(fakultas[fakultas_pilihan])
        label_status.config(text="Fakultas Berhasil Dipilih!")
    else:
        label_status.config(text="Fakultas tidak valid!")

def select_program_studi():
    global program_studi_pilihan
    program_studi_pilihan = entry_program_studi.get()
    if program_studi_pilihan in biaya_program_studi:
        label_status.config(text="Program Studi " + program_studi_pilihan + " dipilih!")
    else:
        label_status.config(text="Program Studi tidak valid!")

def calculate_pembayaran():
    global total_pembayaran
    total_pembayaran = biaya_pendaftaran[fakultas_pilihan] + biaya_program_studi[program_studi_pilihan]
    label_status.config(text="Total Pembayaran: Rp " + str(total_pembayaran))

def select_metode_pembayaran():
    global bayar
    bayar = 0
    metode_pembayaran = var_metode.get()
    if metode_pembayaran == 1:  # Cash
        bayar = total_pembayaran
        label_status.config(text="Anda memilih pembayaran cash.")
    elif metode_pembayaran == 2:  # Non-cash
        potongan = potongan_beasiswa[var_beasiswa.get()]
        bayar = total_pembayaran * (1 - potongan)
        label_status.config(text="Anda memilih pembayaran non-cash dengan potongan beasiswa " + var_beasiswa.get() + ".")

def submit_pembayaran():
    global bayar, total_pembayaran
    bayar = int(entry_submit_pembayaran.get())
    kembalian = bayar - total_pembayaran 
    if kembalian >= 0:
        messagebox.showinfo("Pembayaran Berhasil", "Berhasil!\n\nKembalian: Rp " + str(kembalian))
        messagebox.showinfo(f"Diskon Beasiswa: {diskon * 100}%")
    else:
        messagebox.showerror("Pembayaran Kurang", "Pembayaran kurang!\nMohon masukkan jumlah yang cukup.")

 # Menyimpan data ke file
        try:
            with open("data_pembayaran.txt", "w") as file:
                file.write(f"NISN: {nisn}\n")
                file.write(f"Nama: {nama}\n")
                file.write(f"Alamat: {alamat}\n")
                file.write(f"Fakultas: {fakultas_pilihan}\n")
                file.write(f"Program Studi: {program_studi_pilihan}\n")
                file.write(f"Total Pembayaran: Rp {total_pembayaran}\n")
                file.write(f"Jenis Pembayaran: {'Cash' if var_metode.get() == 1 else 'Non-cash'}\n")
                file.write(f"Diskon Beasiswa: {diskon * 100}%\n")
                file.write(f"Kembalian: Rp {kembalian}\n")
            messagebox.showinfo("File Tersimpan", "Data pembayaran telah disimpan dalam file data_pembayaran.txt")
        except IOError:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data ke file.")
        else:
            messagebox.showerror("Pembayaran Kurang", "Pembayaran kurang!\nMohon masukkan jumlah yang cukup.")
# Membuat jendela aplikasi
window = tk.Tk()
window.title("Pendaftaran Universitas BYG")

# Panel dan UI
window.geometry('1500x1000')
window.configure(bg='white')

# Tampilan Head
label_head = tk.Label(window, text="///////// Selamat datang di Universitas BYG //////// ",bg='black',fg='white', font='arial 18 bold italic')
label_head.place(x=200, y=25)
label_head = tk.Label(window, text="Berikut ini adalah Fakultas yang Tersedia: ", bg='white',fg='black',font='arial 13 bold')
label_head.place(x=160, y= 80)

label_head = tk.Label(window, text="Fakultas Ilmu Komputer Program Sarjana( FILKOM ): ", bg='white',fg='black',font='arial 12 bold')
label_head.place(x=160, y= 120)
label_head = tk.Label(window, text="- Teknik Informatika (TI)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 140)
label_head = tk.Label(window, text="- Sistem Formasi (SI)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 160)
label_head = tk.Label(window, text="- Rekayasa Perangkat Lunak (RPL)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 180)
label_head = tk.Label(window, text="- Managemen Informatika (MI)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 200)
label_head = tk.Label(window, text="- Sistem Komputer (SK)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 220)

label_head = tk.Label(window, text="Fakultas Teknik Program Sarjana( FT ): ", bg='white',fg='black',font='arial 12 bold')
label_head.place(x=160, y= 250)
label_head = tk.Label(window, text="- Teknik Industri (TInd)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 269)
label_head = tk.Label(window, text="- Teknik Kimia (TK)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 285)
label_head = tk.Label(window, text="- Teknin Mesin (TM)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 305)
label_head = tk.Label(window, text="- Teknik Nuklir (TN)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 325)
label_head = tk.Label(window, text="- Teknik Elektro (TE)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 345)

label_head = tk.Label(window, text="Fakultas Ilmu Pendidikan( FKIP ): ", bg='white',fg='black',font='arial 12 bold')
label_head.place(x=160, y= 370)
label_head = tk.Label(window, text="- Bahasa Inggris (Bing)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 390)
label_head = tk.Label(window, text="- Matematika (MTK)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 410)
label_head = tk.Label(window, text="- Biologi (BIO)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 430)
label_head = tk.Label(window, text="- Bahasa Jerman (BJ)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 450)
label_head = tk.Label(window, text="- Fisika (FS)", bg='white',fg='black',font='arial 10 bold')
label_head.place(x=180, y= 470)

# Input Biodata
label_nisn = tk.Label(window, text="Masukan Data Diri: ",bg='white',fg='black',font='arial 11 bold')
label_nisn.place(x=650, y= 120)
label_nisn = tk.Label(window, text="NISN:", bg='#2e2e2e',fg='white', font='arial 10 bold')
label_nisn.place(x=650,y= 145)
entry_nisn = tk.Entry(window, bg='#ededed',fg='black')
entry_nisn.place(x=650,y= 165)

label_nama = tk.Label(window, text="NAMA:", bg='#2e2e2e',fg='white', font='arial 10 bold')
label_nama.place(x=650,y= 185)
entry_nama = tk.Entry(window, bg='#ededed',fg='black')
entry_nama.place(x=650,y= 205)

label_alamat = tk.Label(window, text="Alamat:",bg='#2e2e2e',fg='white',font='arial 11 bold')
label_alamat.place(x=650,y= 230)
entry_alamat = tk.Entry(window,bg='#ededed',fg='black')
entry_alamat.place(x=650,y= 250)

btn_submit_biodata = tk.Button(window, text="ENTER", bg='#005e00',fg='white',font='arial 7 bold', command=submit_biodata)
btn_submit_biodata.place(x=650,y=275)


# Menu Pilihan


label_fakultas = tk.Label(window, text="Masukan Kode Fakultas:",bg='white', fg='black',font='arial 10 bold')
label_fakultas.place(x=920, y= 120)
entry_fakultas = tk.Entry(window, bg='#ededed',fg='black')
entry_fakultas.place(x=920, y= 140)
btn_select_fakultas = tk.Button(window, text="Pilih Fakultas", bg='#ededed',fg='black',font='arial 7 bold', command=select_fakultas)
btn_select_fakultas.place(x=920, y= 160)

label_program_studi = tk.Label(window, text="Masukan kode program Studi:",bg='white', fg='black',font='arial 10 bold')
label_program_studi.place(x=920, y= 200)
entry_program_studi = tk.Entry(window, bg='#ededed',fg='black')
entry_program_studi.place(x=920, y= 220)
btn_select_program_studi = tk.Button(window, text="Pilih Program Studi", bg='#ededed',fg='black',font='arial 7 bold',command=select_program_studi)
btn_select_program_studi.place(x=920, y= 240)


# Hitung Pembayaran
btn_calculate_pembayaran = tk.Button(window, text="TOTAL", bg='green',fg='white',font='arial 7 bold',command=calculate_pembayaran)
btn_calculate_pembayaran.place(x=920, y= 265)

# Menu Pembayaran
var_metode = tk.IntVar()
var_metode.set(1)  # Pilihan default: Cash

label_metode = tk.Label(window, text="Pilih Metode Pembayaran:", bg='white', fg='black',font='arial 12 bold')
label_metode.place(x=1124, y= 120)

radio_cash = tk.Radiobutton(window, text="Cash", bg='#ededed',fg='black',font='arial 10 bold',variable=var_metode, value=1)
radio_cash.place(x=1124, y= 140)

radio_noncash = tk.Radiobutton(window, text="Non-cash", bg='#ededed',fg='black',font='arial 10 bold',variable=var_metode, value=2)
radio_noncash.place(x=1124, y= 160)

btn_select_pembayaran = tk.Button(window, text="Pilih Pembayaran", bg='#ededed',fg='black',font='arial 6 bold', command=select_metode_pembayaran)
btn_select_pembayaran.place(x=1124,y=195)

var_beasiswa = tk.StringVar()
var_beasiswa.set("Raport")  # Pilihan default: Beasiswa Raport

label_beasiswa = tk.Label(window, text="Pilih Jenis Beasiswa:", bg='white', fg='black',font='arial 12 bold')
label_beasiswa.place(x=650,y=320)

radio_raport = tk.Radiobutton(window, text="Beasiswa Raport", bg='#ededed',fg='black',font='arial 10 bold',variable=var_beasiswa, value="Raport")
radio_raport.place(x=650,y=340)

radio_prestasi = tk.Radiobutton(window, text="Beasiswa Prestasi", bg='#ededed',fg='black',font='arial 10 bold',variable=var_beasiswa, value="Prestasi")
radio_prestasi.place(x=650,y=360)

radio_bidikmisi = tk.Radiobutton(window, text="Beasiswa Bidikmisi", bg='#ededed',fg='black',font='arial 10 bold',variable=var_beasiswa, value="Bidikmisi")
radio_bidikmisi.place(x=650,y=380)


## Submit Pembayaran
entry_submit_pembayaran = tk.Entry(window, bg='#ededed',fg='black')
entry_submit_pembayaran.place(x=920, y= 340)
btn_submit_pembayaran = tk.Button(window, text="Submit Pembayaran", bg='#ededed',fg='black',font='arial 8 bold',command=submit_pembayaran)
btn_submit_pembayaran.place(x=920,y=365)

# Status
label_status = tk.Label(window, text="" ,bg='#d7b01f', fg='black', font='arial 18 bold italic')
label_status.place(x=450,y=580)

# Menjalankan aplikasi
window.mainloop()