from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\J. N. Zega\Documents\Code Projects\SPINO\PV-UPJ-2023-2\UAS\App\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("360x480")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 480,
    width = 360,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
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

buttonStart = PhotoImage(
    file=relative_to_assets("btnStart.png"))
btnStart = Button(
    image=buttonStart,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("btnStart clicked"),
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
