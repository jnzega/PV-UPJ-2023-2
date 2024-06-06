from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from tkinter.filedialog import askopenfilename
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\J. N. Zega\Downloads\build\assets\frame0")

data = None

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_file():
    global data
    filename = askopenfilename(filetypes=[('CSV Files', '*.csv')])  # hanya memperbolehkan file .csv
    data = pd.read_csv(filename)  # baca file csv
    print(f'File yang dipilih: {filename}')
    
def show_regression():
    global data
    if data is None:
        print("Tidak ada data")
        return

    # asumsikan kolom pertama adalah variabel independen dan kolom kedua adalah variabel dependen
    X = data.iloc[:, 0].values.reshape(-1, 1)
    Y = data.iloc[:, 1].values.reshape(-1, 1)

    # buat model regresi linear
    model = LinearRegression()
    model.fit(X, Y)

    # tampilkan grafik
    plt.scatter(X, Y)
    plt.plot(X, model.predict(X), color='red')
    plt.show()

window = Tk()

window.geometry("1080x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    14.0,
    14.0,
    1064.0,
    611.0,
    fill="#B5B5B5",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_file,
    relief="flat"
)
button_1.place(
    x=231.0,
    y=635.0,
    width=215.0,
    height=62.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=show_regression,
    relief="flat"
)
button_2.place(
    x=634.0,
    y=635.0,
    width=215.0,
    height=62.0
)
window.resizable(False, False)
window.mainloop()
