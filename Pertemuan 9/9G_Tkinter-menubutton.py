from tkinter import *
import tkinter
top = Tk()
mb= Menubutton ( top, text="Daftar Barang Belanjaan", relief=RAISED )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()
mb.menu.add_checkbutton (label="Telur", variable=telurVar)
mb.menu.add_checkbutton (label="Kecap", variable=kecapVar)
mb.menu.add_checkbutton (label="Tahu", variable=tahuVar)
mb.pack()
top.mainloop()