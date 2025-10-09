def sapa(nama):
    print(f"Halo {nama}, selamat belajar Python!")
sapa("Aisyah")
sapa("Budi")

# Dengan return
def tambah(a, b):
    return a + b
hasil = tambah(5, 7)
print(hasil) # Output: 12

# Study Case
def cari_nilai_tertinggi(data):
    tertinggi = data[0]
    for nilai in data:
        if nilai > tertinggi:
            tertinggi = nilai
    return tertinggi

angka = [18,15,16,13,12,17,11,14]
print(cari_nilai_tertinggi(angka))

# Pembuatan funsi dilakukan dengan keyword def diikuti dengan nama fungsi, lalu dibawahnya ditulis body/isi fungsi
# Sebagai contoh pada kode berikut fungsi say_hello() dideklarasikan dengan isi sebuah statement yang menampilkan text hello

def say_hello():
    print("hello")

say_hello()

# Suatu funsgi hanya bisa diakses dan dipanggil setelah funsgi tersebut dideklarasikan (statement pemanggilan fungsi harus dibawah statement deklarasi fungsi). jika fungsi dipaksa digunakan sebelum dideklarasikan hasilnya akan error.

# Fungsi dengan banyak statement 
def print_something():
    print("Hello")

    today = "Friday"
    print(f"Happy {today}")

    for i in range (5):
        print(f"i: {i}")
print_something()