def bin(coll: list) -> list:
	n = len(coll)
	for i in range(i, n):
		val = coll[i]
		low = 0
		high = i - 1

		while low <= high:
			mid = (low + high) // 2
			if val < coll[mid]:
				high = mid - 1
			else:
				low = mid + 1
		for j in range(i, low, -1):
			coll[j] = coll[j - 1]
		coll[low] = val
	return coll

if __name__ == "__main__":
	user = input("Masukkan angka yang dipisahkan dengan koma: \n").strip()
	unsort = [int(item) for item in user.split(",")]

	print(bin(unsort))