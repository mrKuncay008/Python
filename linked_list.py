# Program Linked list
import os

kucing = ["Pony","Mansur","Kuncay","Popy"]
os.system("clear")

print("Ini adalah Kumpulan Kucing-Kucing --\n")
print(kucing)
print("Kucing aisma adalah ", kucing[0])

pilih = input(str("Silakan Pilih kucing hiya: "))
print ("Kucing anda pilih adalah: ", kucing.index(pilih)) 

x = input(("Pilih Kucing Lagi(1/0): "))
if x == '1' :
    kucing.remove(pilih)
    print(kucing)
print("Terimakasih Bye")