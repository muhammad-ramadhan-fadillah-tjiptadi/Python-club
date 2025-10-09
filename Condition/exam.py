# Cek Ganjil Atau Genap
str_input = input("Masukan Nilai:")
nilai = int(str_input)

if nilai % 2 == 0:
    print("Nilai Anda Genap")
else:
    print("Nilai Anda Ganjil")

# Penentuan Tahun Kabisat
tahun = int(input("Masukan Tahun Kabisat:"))

if tahun % 4 == 0:
    print("Tahun Kabisat")
elif tahun % 4 != 0 and tahun % 100 == 0:
    print("Bukan Tahun Kabisat")
elif tahun % 400 != 0 and tahun % 100 == 0 and tahun % 4 == 0:
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")