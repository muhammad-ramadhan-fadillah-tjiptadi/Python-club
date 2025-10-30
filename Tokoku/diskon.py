def total(harga, jumlah):
    # Fungsi untuk menghitung total bayar
    return harga*jumlah

def diskon(harga):
    # Fungsi menghitung diskon
    if (harga <= 500000):
        potongan=harga*0.1
    else:
        potongan=harga*0.05
    return potongan

def bayar(harga, potongan):
    # Fungsi menghitung total bayar
    return harga-potongan