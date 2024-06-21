from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter.ttk import Progressbar
import time
import random
import pygame
import threading

# Mengatur jalur output dan aset
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\J. N. Zega\Documents\Code Projects\SPINO\PV-UPJ-2023-2\UAS\App\build\assets\frame0")

# Fungsi untuk mengonversi jalur relatif ke aset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# Fungsi untuk memulai pemutaran musik
def play_background_music():
    pygame.mixer.init()  # Inisialisasi mixer pygame
    pygame.mixer.music.load(relative_to_assets("background_music.mp3"))  # Memuat file musik
    pygame.mixer.music.play(-1)  # Memutar musik secara terus menerus

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

    # Memulai pemutaran musik latar belakang di thread terpisah
    threading.Thread(target=play_background_music, daemon=True).start()

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
    step = 1 if target_value > current_value else -1  # Menentukan arah langkah
    for value in range(current_value, target_value + step, step):
        progress_bar['value'] = value  # Mengupdate nilai progress bar
        window.update()  # Mengupdate tampilan jendela
        time.sleep(0.01)  # Delay untuk menciptakan efek animasi

# Fungsi untuk animasi label persentase cinta
def animate_label(target_value):
    current_value = int(love_percentage_label.cget("text").split('%')[0].split()[-1])  # Mendapatkan nilai saat ini dari label
    step = 1 if target_value > current_value else -1  # Menentukan arah langkah
    def update_label(value):
        love_percentage_label.config(text=f"You are {value}% in love")  # Mengupdate teks label
        if (step == 1 and value < target_value) or (step == -1 and value > target_value):
            window.after(10, update_label, value + step)  # Delay untuk membuat tempo lebih cepat
        else:
            love_percentage_label.config(text=f"You are {target_value}% in love")  # Mengupdate teks label ke target value
    update_label(current_value + step)  # Memulai animasi label

# Fungsi untuk menghitung persentase kesamaan nama
def calculate_similarity(name1, name2):
    if name1.lower() == name2.lower():  # Jika kedua nama sama persis
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

    if not name1 or not name2:  # Jika salah satu atau kedua nama tidak diisi
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
        if y > 0:  # Jika posisi Y lebih besar dari 0
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
