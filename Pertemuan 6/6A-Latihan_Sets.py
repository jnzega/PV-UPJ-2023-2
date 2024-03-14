# Mendefinisikan set mata kuliah yang dibutuhkan untuk lulus semester 4
mata_kuliah_dibutuhkan = {
    "Statistika dan Probabilitas", "Sistem Operasi", "Pengantar Kecerdasan Buatan", "Pengantar Keamanan Siber", "Analisis Numerik", "Pengantar Sistem Digital", "Basis Data"
}

print("Mata kuliah yang dibutuhkan untuk lulus semester 4:")
for mk in mata_kuliah_dibutuhkan:
    print("-", mk)

# Misalkan seorang mahasiswa telah mengambil mata kuliah berikut
mata_kuliah_diambil = {"Statistika dan Probabilitas", "Pengantar Kecerdasan Buatan", "Analisis Numerik", "Pengantar Sistem Digital", "Basis Data"}

print("\nMata kuliah yang telah diambil oleh mahasiswa:")
for mk in mata_kuliah_diambil:
    print("-", mk)

# Memisahkan mata kuliah yang belum diambil
mata_kuliah_yang_kurang = mata_kuliah_dibutuhkan - mata_kuliah_diambil

# Mengecek apakah mahasiswa telah mengambil semua mata kuliah yang dibutuhkan
if mata_kuliah_diambil.issuperset(mata_kuliah_dibutuhkan):
    print("\nSelamat! Mahasiswa telah mengambil semua mata kuliah yang dibutuhkan.")
else:
    print("\nMahasiswa belum mengambil mata kuliah berikut:")
    for mk in mata_kuliah_yang_kurang:
        print("-", mk)

# Menambahkan mata kuliah yang baru ditawarkan
mata_kuliah_baru = "Pemrograman Jaringan"
mata_kuliah_dibutuhkan.add(mata_kuliah_baru)
print("\n(Mata kuliah [", mata_kuliah_baru, "] baru saja ditawarkan dan ditambahkan ke dalam daftar mata kuliah yang dapat diambil.)")

# Mengupdate mata kuliah yang diambil dengan mata kuliah pilihan
mata_kuliah_pilihan = {"Pemrograman Jaringan", "Pemrograman Mobile"}
mata_kuliah_diambil.update(mata_kuliah_pilihan)
print("\nMahasiswa memilih untuk mengambil mata kuliah pilihan berikut:")
for mk in mata_kuliah_pilihan:
    print("-", mk)

# Menghapus mata kuliah yang tidak lagi ditawarkan
mata_kuliah_tidak_ditawarkan = "Pengantar Keamanan Siber"
mata_kuliah_dibutuhkan.discard(mata_kuliah_tidak_ditawarkan)
print("\n(Mata kuliah [", mata_kuliah_tidak_ditawarkan, "] tidak lagi ada di dalam kurikulum dan telah dihapus dari daftar mata kuliah yang dibutuhkan.)")

# Menghitung jumlah mata kuliah yang dibutuhkan
jumlah_mata_kuliah_dibutuhkan = len(mata_kuliah_dibutuhkan)
print("\nJumlah mata kuliah yang dibutuhkan untuk lulus semester 4 adalah:", jumlah_mata_kuliah_dibutuhkan, "mata kuliah.")

# Menggabungkan semua mata kuliah yang ada
semua_mata_kuliah = mata_kuliah_dibutuhkan.union(mata_kuliah_diambil)
print("\nSemua mata kuliah yang ada adalah:")
for mk in semua_mata_kuliah:
    print("-", mk)