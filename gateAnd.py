print("Algebra AND")
print("=====================")
def a(input_1: int, input_2: int) -> int:
	"""
	Menjumlah kan AND nilai Input

	>>> And-Gate(0, 0)
	0
	>>> And-Gate(0, 1)
	0
	>>> And-Gate(1, 0)
	0
	>>> And-Gate(1, 1)
	0
	"""
	return int((input_1, input_2).count(0) == 0)

def test_and() -> None:
	"""
	Test And-Gate fungsi
	"""
	assert a(0,0) == 0
	assert a(0,1) == 0
	assert a(1,0) == 0
	assert a(1,1) == 1

if __name__ == "__main__":
	test_and()
	print(a(1, 0))
	print(a(0, 0))
	print(a(0, 1))
	print(a(1, 1))

print("Algebra OR")
print("=====================")

def a (input_1: int, input_2: int) -> int:
	return int((input_1, input_2).count(1) != 0)

def test_or() -> None:
	assert a(0,0) == 0
	assert a(0,1) == 1
	assert a(1,0) == 1
	assert a(1,1) == 1

if __name__ == "__main__":
	test_or()
	print(a(1, 0))
	print(a(0, 0))
	print(a(0, 1))
	print(a(1, 1))