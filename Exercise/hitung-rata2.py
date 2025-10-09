jumlah_angka = int(input("Masukan jumlah angka: "))
total = 0
for i in range (jumlah_angka):
    angka = float (input("Masukan angka ke-{}:".format(i + 1)))
    total += angka
    rata_rata = total / jumlah_angka
    print("Rata-rata dari angka-angka tersebut adalah ", rata_rata)
    