import tkinter as tk

root = tk.Tk()

# # latihan-1: Membuat widget dasar
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

# # Latihan 2: Membuat Canvas
# Kanvasku = tk.Canvas(root, height=1000, width = 1920)
# Kanvasku.pack()

# Latihan 3: Membuat Canvas
Frameku = tk.Frame(root, bg ='blue')
Frameku.place(relwidth = 0.8, relheight=0.8)

# # Latihan 4a: Membuat Button Di Root
# Tombolku = tk.Button(root, text = "Test Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack()

# Latihan 4b: Membuat Button Di Frame
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

#Latihan 5: Membuat Entry
Entryku = tk.Entry(Frameku, bg='green')
Entry.pack()

root.mainloop()