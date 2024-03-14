print("\033c")
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan ukuran maksimum baris dan kolom
rowmax = int(1079)
colmax = int(1919)

# Mendefinisikan radius maksimum
radius_max = int(1000)

# Mendefinisikan batas-batas radius
batas1 = int(0.2 * radius_max)
batas2 = int(0.4 * radius_max)
batas3 = int(0.6 * radius_max)
batas4 = int(0.8 * radius_max)

Gambar = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.int16)

for i in range(0, rowmax+1):
    for j in range(0, colmax+1):
        if (i**2 + j**2) >= 0 and (i**2 + j**2) < batas1**2:
            Gambar[i, j, 0] = 255  # Merah
        elif (i**2 + j**2) >= batas1**2 and (i**2 + j**2) < batas2**2:
            Gambar[i, j, 1] = 255  # Hijau
        elif (i**2 + j**2) >= batas2**2 and (i**2 + j**2) < batas3**2:
            Gambar[i, j, 2] = 255  # Biru
        elif (i**2 + j**2) >= batas3**2 and (i**2 + j**2) < batas4**2:
            Gambar[i, j, 0] = 255  # Kuning
            Gambar[i, j, 1] = 255
        elif (i**2 + j**2) >= batas4**2 and (i**2 + j**2) < radius_max**2:
            Gambar[i, j, 0] = 255  # Ungu
            Gambar[i, j, 2] = 255

plt.figure()
plt.imshow(Gambar)
plt.show()