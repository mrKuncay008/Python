print("----------------- Program Warung Kopi UTS -----------------")
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Daftar Menu Warung Kopi -----------------")
   print("1. Pandan Latte - Rp 28000")
   print("2. Matcha- Rp 29000")
   print("3.  Espresso - Rp 25000")
   print("4.  Capocinno - Rp 28000")
   print("5.  Kopi Kenngan Mantan - Rp 31000")
   print("6.  Kopi Kangen - Rp 26000")
   print("7.  Kopi Enak - Rp 18000")


   nomor=int(input("Masukan Pilihan: "))
   
   if nomor==1:
       totalmkn=porsi*15000
       print (porsi," porsi Nasi Goreng Telur = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es kopi - Rp 4000")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   else:
      print("Pilihan tidak ada, silahkan masukan lagi!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\nTotal harus Dibayar: Rp",totalsemua)
uang=int(input("Uang Tunai Pembeli: Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("========== S T R U K   B E L I =========")
print("==================================")
print ("Nama\t\t:",pembeli)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("==================================")