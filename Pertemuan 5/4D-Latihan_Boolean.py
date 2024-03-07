# Mendefinisikan jam operasional toko (dalam format 24 jam)
jam_buka = 9  # Jam buka toko
jam_tutup = 17  # Jam tutup toko

# Misalkan sekarang jam 15.00
jam_sekarang = 15

# Mengecek apakah toko buka atau tidak
if jam_buka <= jam_sekarang < jam_tutup:
    toko_buka = True
else:
    toko_buka = False

print("Apakah toko buka? ")

if toko_buka:
    print("Ya, toko masih buka")
else:
    print("Tidak, toko sudah tutup")
