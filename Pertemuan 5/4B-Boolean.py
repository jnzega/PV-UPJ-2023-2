print("Case 1")
# Boolean data type declaration (Standard way)
f = bool(True)
g = bool(False)
print(f)
print(g)
print("=================================")

print("Case 2")
print(3<2)
print(3+2==5)
print(3<2)
print("=================================")

print("Case 3")
Penghasilan = 20000000
PenghasilanTanpaPajak = 4000000
if Penghasilan <= PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0
if Penghasilan > PenghasilanTanpaPajak:
    PajakYangHarusDibayar = 0.1 * Penghasilan
    print("TPajak yang harus Anda bayar: Rp ", PajakYangHarusDibayar)

#Case 4
print("Case 4")
#Semua data yang tidak nol (kosong) memiliki nilai Boolean True
a = 3   #integer
b = "Ini data string."   #string
c = ("laptop", "buku", "ballpen")   #tuple
d = ["laptop", "buku", "ballpen"]   #list
e = {"laptop": "asus", "buku": "buku_teks", "ballpen": "arrow"}   #dictionary
f = {1, 2, 3, 4, 5}    #set

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

print("=================================")

#PART 3
#Case 5
print("Case 5")
#Variabel yang kosong memiliki nilai Boolean False
a = 0                                          #integer null
b = ""                                         #string kosong
c = ()                                         #tuple kosong
d = []                                         #list kosong
e = {}                                         #dictionary/set kosong
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print("=================================")

#Case 6
print("Case 6")
#Variabel yang panjangnya nol memiliki nilai Boolean False
class myclass():
    def __len__(self):
        return 0

print(bool(myclass()))
print("=================================")


