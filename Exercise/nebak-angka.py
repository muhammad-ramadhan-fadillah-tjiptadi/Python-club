import random
angka_acak = random.randint(1, 100)
tebakan = 0
while True:
    tebakan = int(input("Tebak angka (1-100)"))
    if tebakan < angka_acak:
        print("Angka terlalu kecil, coba lagi")
    elif tebakan > angka_acak:
        print("Angka terlalu besar, coba lagi")
    else:
        print("Selamat, tebakan anda benar!")
        break