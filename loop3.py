blocks = int(input("Enter number of blocks: "))
height = 0
blocks_i = blocks

for layer in range(1, blocks + 1):
    if blocks_i >= layer:  # Cek apakah masih cukup blok untuk menyelesaikan lapisan berikutnya
        blocks_i -= layer  # Mengurangi jumlah blok yang digunakan untuk lapisan saat ini
        height += 1  # Menambahkan ketinggian pyramid
    else:
        break  # Jika tidak cukup blok, hentikan perulangan

print("The height of the pyramid:", height)
print()
print("\t====== Rumus MTK Collatz ======")
print()

n = int(input("Masukan Bilangan: "))
steps = 0

while n != 1:
    print(n, end = '\n')
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1

print(1)
print("Total Steps: ", steps)