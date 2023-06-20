import datetime

mhs_1 = {
	'nama' : 'Muhammad Kuncay',
	'Nim'  : '92000',
	'Nilai': '9,0',
	'Behasiswa' : False,
	'Tanggl Lahir': datetime.datetime(2000,4,30)
}

mhs_2 = {
	'nama' : 'Muhammad masnur',
	'Nim'  : '92021',
	'Nilai': '8,2',
	'Behasiswa' : True,
	'Tanggl Lahir': datetime.datetime(1970,5,30)
}

mhs_3 = {
	'nama' : 'Muhammad Joni',
	'Nim'  : '91928',
	'Nilai': '7,1',
	'Behasiswa' : False,
	'Tanggl Lahir': datetime.datetime(2010,2,10)
}

mh = {
	'MH-01' : mhs_1,
	'MH-02' : mhs_2,
	'MH-03' : mhs_3
}
print()
print(f"{'No':<6} {'Nama':<24} {'Nilai':<8} {'Behasiswa':<10} {' Lahir':<10}")
print("=" * 60)
print()

for No, mhs in mh.items():
	Nama = mhs['nama']
	Nim = mhs['Nim']
	Nilai = mhs['Nilai']
	Beasiswa = mhs['Behasiswa']
	Tanggal_Lhr = mhs['Tanggl Lahir'].strftime("%x")

	print(f"{No:<6} {Nama:<24} {Nilai:<8} {Beasiswa:<10} {Tanggal_Lhr:<10}")
