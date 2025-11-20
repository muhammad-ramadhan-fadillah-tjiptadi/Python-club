class Siswa:
    # Atribut
    nis = ""
    nama = ""

    # Constructor
    def __init__(self, nis="", nama=""):
        self.nis = nis
        self.nama = nama
    
    # Method
    def printSiswa(self):
        print(f"NIS : {self.nis}")
        print(f"Nama : {self.nama}")

# Membuat objek "sis1" dari class Siswa dengan constructor
sis1 = Siswa("12410462", "Ramadhan")

# Memanggil Method
sis1.printSiswa()