# CREATING GUI USING TKINTER
import tkinter as tk
# Jalankan kode untuk tiap topik bergantian. Beri tanda # untuk topik yang tidak dijalankan.


root = tk.Tk()

# #1 Widget Dasar
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

# #2 Membuat Canvas
# Kanvasku = tk.Canvas(root, height = 1000, width = 1920)
# Kanvasku.pack()

#3 Membuat Canvas
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 1, relheight = 1)

# #4a Membuat Button di Root
# Tombolku = tk.Button(root, text = "Test Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack()

#4b Membuat Button di Frame
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

#5 Membuat Entry
Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()

root.mainloop()