print("----------------- Program Warung Kopi UTS -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print("Nama Pembeli :", pembeli)

def fungsimakanan():
    global totalmnm
    global mnm
    print("\n----------------- Daftar Menu Warung Kopi -----------------")
    print("1. Pandan Latte - Rp 28,000")
    print("2. Matcha - Rp 29,000")
    print("3. Espresso - Rp 25,000")
    print("4. Capocinno - Rp 28,000")
    print("5. Kopi Kenngan Mantan - Rp 31,000")
    print("6. Kopi Kangen - Rp 26,000")
    print("7. Kopi Enak - Rp 18,000")
    print()

    pesanan = []
    totalmnm = 0
    pilihan = "y"

    while pilihan.lower() == "y":
        print("Daftar Pesanan: \n")
        nomor = int(input("Masukkan Pilihan: "))

        if nomor == 1:
            mnm = "Pandan Latte"
            harga = 28000
        elif nomor == 2:
            mnm = "Matcha"
            harga = 29000
        elif nomor == 3:
            mnm = "Espresso"
            harga = 25000
        elif nomor == 4:
            mnm = "Capocinno"
            harga = 28000
        elif nomor == 5:
            mnm = "Kopi Kenngan Mantan"
            harga = 31000
        elif nomor == 6:
            mnm = "Kopi Kangen"
            harga = 26000
        elif nomor == 7:
            mnm = "Kopi Enak"
            harga = 18000
        else:
            print("Pilihan tidak valid!")
            continue

        pesanan.append((mnm, harga))
        totalmnm += harga

        pilihan = input("Lanjut pesan? (y/t): ")

    print("\nDaftar Pesanan:")
    for item in pesanan:
        print(item[0], "- Rp", item[1])

    print("\nTotal Pembayaran: Rp","{:,.0f}".format(totalmnm))

    print("========================================================")

    pembayaran = int(input("Masukkan Uang Pembayaran: Rp. "))
    kembalian = pembayaran - totalmnm
    print("-----------------------------------------------------")
    print("Kembalian: Rp.", "{:,.0f}".format(kembalian))
    print()
    print("------------- Muhammad Frendi Arahman-411221049-Uts---------")
    
fungsimakanan()