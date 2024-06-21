from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\J. N. Zega\Documents\Code Projects\SPINO\PV-UPJ-2023-2\UAS\Main Screen\build\assets\frame0")


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
    image=textBoxSub2
)

canvas.create_text(
    106.0,
    196.0,
    anchor="nw",
    text="You are 100% in love",
    fill="#FFFFFF",
    font=("MontserratRoman Light", 13 * -1)
)

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

calculateButton = PhotoImage(
    file=relative_to_assets("calculateBtn.png"))
calculateBtn = Button(
    image=calculateButton,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("calculateBtn clicked"),
    relief="flat"
)
calculateBtn.place(
    x=101.0,
    y=307.0,
    width=157.0,
    height=47.0
)

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

barProgress = PhotoImage(
    file=relative_to_assets("barProgressImg.png"))
barProgressImg = canvas.create_image(
    179.0,
    246.0,
    image=barProgress
)

loveSymbol = PhotoImage(
    file=relative_to_assets("loveSymbolImg.png"))
loveSymbolImg = canvas.create_image(
    179.0,
    155.0,
    image=loveSymbol
)
window.resizable(False, False)
window.mainloop()
