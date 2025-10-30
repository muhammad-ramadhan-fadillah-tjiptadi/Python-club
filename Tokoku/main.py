from diskon import total,diskon,bayar
print("--- Toko Jiem Maju Jaya ---")

# Input data
Harga = int(input("Masukan harga barang: "))
Jumlah = int(input("Masukan jumlah baju yang dibeli: "))
Total = total(Harga, Jumlah)
Potongan = diskon(Total)
Tagihan = bayar(Total, Potongan)
print("Total harga = ", "Rp.", Total)
print("Diskon = ", "Rp.", Potongan)
Bayar = int(input("Jumlah Nominal Uang: "))
Kembalian = (Bayar-Tagihan)
print("Uang Kembalian = ", "Rp.", Kembalian)