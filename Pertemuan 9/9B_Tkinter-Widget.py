import tkinter as tk

root = tk.Tk()

# ============== Membuat Widget Dasar ==============
# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

# ============== Membuat Canvas Dasar ==============
# Kanvasku = tk.Canvas(root, height = 1080, width = 1920)
# Kanvasku.pack()

# ============= Membuat Canvas Lanjutan =============
Frameku = tk.Frame(root, bg = 'blue')
Frameku.place(relwidth = 0.8, relheight = 0.8)

root.mainloop()

# ============= Membuat Button in Root =============
# Tombolku = tk.Button(root, text = "Test Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack()

# ============ Membuat Button in Frame ============
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

# ================== Membuat Entry ==================
Tombolku = Entryku = tk.Entry(Framku, bg = 'green')
Entryku.pack()

root.mainloop()