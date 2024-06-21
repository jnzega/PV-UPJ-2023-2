# Aplikasi Kalkulator Cinta

Aplikasi Kalkulator Cinta adalah aplikasi berbasis Tkinter yang memungkinkan pengguna untuk menghitung persentase kecocokan cinta berdasarkan nama yang dimasukkan. Aplikasi ini memiliki layar sambutan yang menarik dan efek animasi cinta berhamburan saat tombol ditekan.

## Fitur

1. **Layar Sambutan:**
   - Desain layar sambutan yang menarik dengan tombol untuk memulai aplikasi.
   - Efek animasi cinta berhamburan saat tombol `Start` ditekan.

2. **Layar Utama:**
   - Input untuk dua nama.
   - Tombol untuk menghitung persentase cinta.
   - Label yang menampilkan persentase cinta.
   - Progress bar yang menunjukkan persentase cinta.
   - Efek animasi cinta berhamburan saat tombol `Calculate` ditekan.

## Cara Kerja Program

### Layar Sambutan

1. **Desain Layar Sambutan:**
   - Layar sambutan dibuat menggunakan `Canvas` dari Tkinter.
   - Gambar latar belakang dan elemen lain seperti logo dan tombol ditempatkan pada canvas.

2. **Tombol Start:**
   - Tombol `Start` dibuat menggunakan widget `Button`.
   - Ketika tombol ditekan, fungsi `start_main_screen_with_hearts` dipanggil untuk memulai layar utama dan menambahkan efek animasi hati berhamburan.

### Layar Utama

1. **Desain Layar Utama:**
   - Layar utama juga dibuat menggunakan `Canvas`.
   - Elemen-elemen seperti input untuk nama, tombol `Calculate`, label untuk menampilkan persentase cinta, dan progress bar ditempatkan pada canvas.

2. **Input Nama:**
   - Dua input untuk nama dibuat menggunakan widget `Entry`.
   - Nama yang dimasukkan oleh pengguna akan digunakan untuk menghitung persentase cinta.

3. **Tombol Calculate:**
   - Tombol `Calculate` dibuat menggunakan widget `Button`.
   - Ketika tombol ditekan, fungsi `calculate_love_percentage` dipanggil untuk menghitung persentase cinta dan memulai animasi.

### Fungsi Utama

1. **Fungsi `animate_progress_bar`:**
   - Fungsi ini digunakan untuk menganimasikan progress bar dari nilai saat ini ke nilai target.
   - Progress bar diperbarui secara bertahap dengan jeda waktu untuk menciptakan efek animasi.

2. **Fungsi `animate_label`:**
   - Fungsi ini digunakan untuk menganimasikan label persentase cinta dari nilai saat ini ke nilai target.
   - Label diperbarui secara bertahap dengan jeda waktu untuk menciptakan efek animasi.

3. **Fungsi `calculate_similarity`:**
   - Fungsi ini menghitung persentase kesamaan antara dua nama berdasarkan karakter yang sama dan kesamaan panjang nama.
   - Persentase akhir adalah kombinasi dari persentase kesamaan karakter, kesamaan panjang nama, dan nilai acak untuk variasi.

4. **Fungsi `calculate_love_percentage`:**
   - Fungsi ini dipanggil ketika tombol `Calculate` ditekan.
   - Mengambil nama dari input, menghitung persentase cinta menggunakan `calculate_similarity`, dan memulai animasi label dan progress bar.
   - Juga menambahkan efek animasi hati berhamburan.

5. **Fungsi `create_heart`:**
   - Fungsi ini membuat simbol hati pada posisi tertentu di canvas.

6. **Fungsi `animate_hearts`:**
   - Fungsi ini membuat dan menggerakkan simbol hati di canvas untuk menciptakan efek animasi hati berhamburan.
   - Simbol hati bergerak secara acak baik secara horizontal maupun vertikal.

7. **Fungsi `move_heart`:**
   - Fungsi ini digunakan dalam `animate_hearts` untuk menggerakkan setiap simbol hati.

8. **Fungsi `start_main_screen_with_hearts`:**
   - Fungsi ini memulai layar utama dan menambahkan efek animasi hati berhamburan saat layar utama ditampilkan.

## Struktur Kode

```python
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter.ttk import Progressbar
import time
import random

# Mengatur jalur output dan aset
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\J. N. Zega\Documents\Code Projects\SPINO\PV-UPJ-2023-2\UAS\App\build\assets\frame0")

# Fungsi untuk mengonversi jalur relatif ke aset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk menampilkan layar utama
def show_main_screen():
    # Menghapus semua widget dari layar sambutan
    for widget in window.winfo_children():
        widget.destroy()

    # Deklarasi variabel global
    global canvas, love_percentage_label, progress_bar
    global entry_1, entry_2
    global backgroundPink, subTitle, textBoxSubtitle1, textBoxSubtitle2
    global smallLogoText, smallLogoSymbol, calculateButton
    global entryName1, entryName2, barProgress, loveSymbol

    # Membuat layar utama
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=480,
        width=360,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    
    canvas.place(x=0, y=0)
    backgroundPink = PhotoImage(
        file=relative_to_assets("bgPink.png"))
    bgPink = canvas.create_image(
        180.0,
        240.0,
        image=backgroundPink
    )

    subTitle = PhotoImage(
        file=relative_to_assets("subtitle.png"))
    subtitle = canvas.create_image(
        180.0,
        458.0,
        image=subTitle
    )

    # Bagian Main Screen Mulai
    textBoxSubtitle1 = PhotoImage(
        file=relative_to_assets("textBoxSub1.png"))
    textBoxSub1 = canvas.create_image(
        78.0,
        127.0,
        image=textBoxSubtitle1
    )

    textBoxSubtitle2 = PhotoImage(
        file=relative_to_assets("textBoxSub2.png"))
    textBoxSub2 = canvas.create_image(
        254.0,
        127.0,
        image=textBoxSubtitle2
    )

    # Label untuk persentase cinta
    love_percentage_label = Label(
        window,
        text="You are 100% in love",
        bg="#FFFFFF",
        fg="#000000",  # Warna teks diubah menjadi hitam untuk kontras
        font=("MontserratRoman Light", 13)
    )
    love_percentage_label.place(
        x=106,
        y=196
    )

    # Logo kecil
    smallLogoText = PhotoImage(
        file=relative_to_assets("smallLogo.png"))
    smallLogo = canvas.create_image(
        60.0,
        35.0,
        image=smallLogoText
    )

    smallLogoSymbol = PhotoImage(
        file=relative_to_assets("smallSymbol.png"))
    smallSymbol = canvas.create_image(
        74.99999953419263,
        22.0,
        image=smallLogoSymbol
    )

    # Tombol untuk menghitung persentase cinta
    calculateButton = PhotoImage(
        file=relative_to_assets("calculateBtn.png"))
    calculateBtn = Button(
        image=calculateButton,
        borderwidth=0,
        highlightthickness=0,
        command=calculate_love_percentage,
        relief="flat"
    )
    calculateBtn.place(
        x=101.0,
        y=307.0,
        width=157.0,
        height=47.0
    )

    # Input untuk nama pertama
    entryName1 = PhotoImage(
        file=relative_to_assets("entry_bg_1.png"))
    entry_bg_1 = canvas.create_image(
        267.5,
        155.0,
        image=entryName1
    )
    entry_1 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=208.0,
        y=141.0,
        width=119.0,
        height=26.0
    )

    # Input untuk nama kedua
    entryName2 = PhotoImage(
        file=relative_to_assets("entry_bg_2.png"))
    entry_bg_2 = canvas.create_image(
        91.5,
        155.0,
        image=entryName2
    )
    entry_2 = Entry(
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
    )
    entry_2.place(
        x=32.0,
        y=141.0,
        width=119.0,
        height=26.0
    )

    # Progress bar untuk persentase cinta
    progress_bar = Progressbar(
        window,
        orient="horizontal",
        length=200,
        mode='determinate'
    )
    progress_bar.place(
        x=80,
        y=246
    )

    # Simbol cinta di layar utama
    loveSymbol = PhotoImage(
        file=relative_to_assets("loveSymbolImg.png"))
    loveSymbolImg = canvas.create_image(
        179.0,
        155.0,
        image=loveSymbol
    )
    # Bagian Main Screen Selesai

# Fungsi untuk animasi progress bar
def animate_progress_bar(target_value):
    current_value = int(progress_bar['value'])  # Mendapatkan nilai saat ini dari progress bar
    target_value = int(target_value)  # Mengubah target value menjadi integer
    step = 1 jika target_value > current_value else -1  # Menentukan arah langkah
    for value in range(current_value, target_value + step, step):
        progress_bar['value'] = value  # Mengupdate nilai progress bar
        window.update()  # Mengupdate tampilan jendela
        time.sleep(0.01)  # Delay untuk menciptakan efek animasi

# Fungsi untuk animasi label persentase cinta
def animate_label(target_value):
    current_value = int(love_percentage_label.cget("text").split('%')[0].split()[-1])  # Mendapatkan nilai saat ini dari label
    step = 1 jika target_value > current_value else -1  # Menentukan arah langkah
    def update_label(value):
        love_percentage_label.config(text=f"You are {value}% in love")  # Mengupdate teks label
        jika (step == 1 dan value < target_value) atau (step == -1 dan value > target_value):
            window.after(10, update_label, value + step)  # Delay untuk membuat tempo lebih cepat
        else:
            love_percentage_label.config(text=f"You are {target_value}% in love")  # Mengupdate teks label ke target value
    update_label(current_value + step)  # Memulai animasi label

# Fungsi untuk menghitung persentase kesamaan nama
def calculate_similarity(name1, name2):
    jika name1.lower() == name2.lower():  # Jika kedua nama sama persis
        return 100

    set1 = set(name1.lower())  # Mengubah nama pertama menjadi set karakter
    set2 = set(name2.lower())  # Mengubah nama kedua menjadi set karakter
    common_chars = set1.intersection(set2)  # Karakter yang sama
    common_chars_count = len(common_chars)  # Jumlah karakter yang sama

    len_diff = abs(len(name1) - len(name2))  # Perbedaan panjang nama
    max_len = max(len(name1), len(name2))  # Panjang nama terpanjang

    similarity_percentage = (common_chars_count / max_len) * 50  # Persentase kesamaan karakter
    length_similarity_percentage = ((max_len - len_diff) / max_len) * 30  # Persentase kesamaan panjang
    random_percentage = random.randint(0, 20)  # Tambahan persentase acak

    return int(similarity_percentage + length_similarity_percentage + random_percentage)  # Mengembalikan total persentase

# Fungsi untuk menghitung dan menampilkan persentase cinta
def calculate_love_percentage():
    name1 = entry_1.get()  # Mendapatkan nilai dari input nama pertama
    name2 = entry_2.get()  # Mendapatkan nilai dari input nama kedua

    jika not name1 atau not name2:  # Jika salah satu atau kedua nama tidak diisi
        love_percentage_label.config(text="Please enter both names")  # Menampilkan pesan kesalahan
        return

    percentage = calculate_similarity(name1, name2)  # Menghitung persentase kesamaan
    animate_label(percentage)  # Memulai animasi label
    animate_progress_bar(percentage)  # Memulai animasi progress bar
    animate_hearts(canvas, 20)  # Menambahkan animasi hati saat tombol calculate ditekan

# Fungsi untuk membuat simbol hati
def create_heart(canvas, x, y, size=20):
    return canvas.create_text(x, y, text="❤️", font=("Arial", size), fill="white")  # Membuat teks simbol hati

# Fungsi untuk animasi hati berhamburan
def animate_hearts(canvas, num_hearts=10):
    hearts = [create_heart(canvas, random.randint(20, 340), 480) for _ in range(num_hearts)]  # Membuat simbol hati

    def move_heart(heart):
        x, y = canvas.coords(heart)  # Mendapatkan koordinat simbol hati
        jika y > 0:  # Jika posisi Y lebih besar dari 0
            dx = random.randint(-2, 2)  # Menggerakkan hati secara acak pada sumbu X
            dy = random.randint(-10, -5)  # Menggerakkan hati ke atas pada sumbu Y
            canvas.move(heart, dx, dy)  # Memindahkan simbol hati
            window.after(50, move_heart, heart)  # Mengulangi gerakan setelah 50 milidetik
        else:
            canvas.delete(heart)  # Menghapus simbol hati jika di luar layar

    for heart in hearts:
        move_heart(heart)  # Memulai gerakan untuk setiap simbol hati

# Fungsi untuk memulai layar utama dengan animasi hati berhamburan
def start_main_screen_with_hearts():
    show_main_screen()  # Menampilkan layar utama
    animate_hearts(canvas, 30)  # Menambahkan lebih banyak hati saat memulai main screen

# Membuat jendela utama
window = Tk()
window.geometry("360x480")
window.configure(bg="#FFFFFF")

# Membuat canvas untuk layar sambutan
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=480,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
backgroundPink = PhotoImage(
    file=relative_to_assets("bgPink.png"))
bgPink = canvas.create_image(
    180.0,
    240.0,
    image=backgroundPink
)

subTitle = PhotoImage(
    file=relative_to_assets("subtitle.png"))
subtitle = canvas.create_image(
    180.0,
    458.0,
    image=subTitle
)

welcomeLogoText = PhotoImage(
    file=relative_to_assets("logoText.png"))
logoText = canvas.create_image(
    166.0,
    204.0,
    image=welcomeLogoText
)

welcomeLogoSymbol = PhotoImage(
    file=relative_to_assets("logoSymbol.png"))
logoSymbol = canvas.create_image(
    259.99998193979263,
    141.0,
    image=welcomeLogoSymbol
)

# Tombol untuk memulai layar utama dengan animasi hati berhamburan
buttonStart = PhotoImage(
    file=relative_to_assets("btnStart.png"))
btnStart = Button(
    image=buttonStart,
    borderwidth=0,
    highlightthickness=0,
    command=start_main_screen_with_hearts,
    relief="flat"
)
btnStart.place(
    x=101.0,
    y=307.0,
    width=157.0,
    height=47.0
)

window.resizable(False, False)
window.mainloop()
