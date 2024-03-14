import time

a = int(input("Masukan Nilai A: "))
b = int(input("Masukan Nilai B: "))
ppn_a = 0.0
ppn_b = 0.0

print("\nData sedang diproses", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)

print(f"\n\nNilai A adalah: {a}, \nNilai B adalah: {b}")

if a > b:
    print("Kesimpulan: Nilai A lebih besar dari B.")
elif a < b:
    print("Kesimpulan: Nilai B lebih besar dari A.")
elif a == b:
    print("Kesimpulan: Nilai A sama dengan nilai B")

print("\nData sedang diproses", end="")
for i in range(3):
    print(".", end="")
    time.sleep(1)

if a >= 10000:
    ppn_a = (12/100) * a
    a_total = a + ppn_a
    print(f"\n\nNilai A terkena PPN 12% sebesar = {ppn_a}")
else:
    print(f"\n\nNilai A = {a} dan belum mencukupi untuk dikenakan PPN 12%")
if b >= 50000:
    ppn_b = (12/100) * b
    b_total = b + ppn_b
    print(f"Nilai B terkena PPN 12% sebesar = {ppn_b}")
else:
    print(f"Nilai B = {b} dan belum mencukupi untuk dikenakan PPN 12%")

if ppn_a != 0.0 and ppn_b != 0.0:
    print(True)
else:
    print(False)

del a, b

if 'a' in globals() and 'b' in globals():
    print("\n'a' dan 'b' masih ada")
else:
    print("\nKedua variabel telah dihapus")