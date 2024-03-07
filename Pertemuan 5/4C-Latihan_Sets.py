# Mendefinisikan set mata kuliah yang dibutuhkan untuk lulus semester 4
mata_kuliah_dibutuhkan = {
    "Statistika dan Probabilitas", "Sistem Operasi", "Pengantar Kecerdasan Buatan", "Pengantar Keamanan Siber", "Analisis Numerik", "Pengantar Sistem Digital", "Basis Data"
}

# Misalkan seorang mahasiswa telah mengambil mata kuliah berikut
mata_kuliah_diambil = {"Statistika dan Probabilitas", "Pengantar Kecerdasan Buatan", "Analisis Numerik", "Pengantar Sistem Digital", "Basis Data"}

# Memisahkan mata kuliah yang belum diambil
mata_kuliah_yang_kurang = mata_kuliah_dibutuhkan - mata_kuliah_diambil

# Mengecek apakah mahasiswa telah mengambil semua mata kuliah yang dibutuhkan
if mata_kuliah_diambil.issuperset(mata_kuliah_dibutuhkan):
    print("Mahasiswa telah mengambil semua mata kuliah yang dibutuhkan.")
else:
    print("Mahasiswa belum mengambil mata kuliah", ', '.join(map(str, mata_kuliah_yang_kurang)))