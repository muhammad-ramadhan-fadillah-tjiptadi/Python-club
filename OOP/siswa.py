class Siswa:
    # Atribut
    nis = ""
    nama = ""
    
    # Method
    def printSiswa(self):
        print(f"NIS : {self.nis}")
        print(f"Nama : {self.nama}")

# Membuat objek 'sis1' dari class siswa
sis1 = Siswa()
# Memberi nilai kedua atribut dari objek
sis1.nis = "12410462"
sis1.nama = "Ramadhan"
# memanggil method
sis1.printSiswa()