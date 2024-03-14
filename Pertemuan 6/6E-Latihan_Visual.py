import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan ukuran maksimum baris dan kolom
rowmax = int(1079)
colmax = int(1919)

# Mendefinisikan titik pusat
center_i = rowmax // 2
center_j = colmax // 2

# Mendefinisikan radius maksimum
radius_max = min(center_i, center_j)

# Mendefinisikan batas-batas radius
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.6 * radius_max)
batas4 = int(0.8 * radius_max)

# Membuat array Gambar dengan ukuran (rowmax+1, colmax+1, 3) dan tipe data int16
Gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.int16)

# Melakukan iterasi untuk setiap baris dan kolom
for i in range(0, rowmax+1):
    for j in range(0, colmax+1):
        # Menghitung jarak dari titik pusat
        dist = (i - center_i)**2 + (j - center_j)**2

        # Mengubah warna pixel berdasarkan jarak dari pusat
        if dist >= 0 and dist < batas1**2:
            Gambar[i, j, 0] = 255  # Merah
        elif dist >= batas1**2 and dist < batas2**2:
            Gambar[i, j, 1] = 255  # Hijau
        elif dist >= batas2**2 and dist < batas3**2:
            Gambar[i, j, 2] = 255  # Biru
        elif dist >= batas3**2 and dist < batas4**2:
            Gambar[i, j, 0] = 255  # Kuning
            Gambar[i, j, 1] = 255
        elif dist >= batas4**2 and dist < radius_max**2:
            Gambar[i, j, 0] = 255  # Ungu
            Gambar[i, j, 2] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()
