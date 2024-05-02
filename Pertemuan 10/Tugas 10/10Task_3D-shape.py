import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
import time



# Fungsi untuk menampilkan layar loading dan membuka program utama
def load_and_open():
    # Membuat jendela loading
    loading = tk.Toplevel(root)
    loading.geometry("200x100")
    loading.title("Loading...")
    label = tk.Label(loading, text="Loading...")
    label.pack()

    # Menunggu selama 2 detik untuk efek loading
    loading.update()
    time.sleep(2)

    # Menutup jendela loading
    loading.destroy()

    # Membuka program utama
    open_main_program()

# Fungsi untuk membuka program utama
def open_main_program():
    
    # Variabel global untuk menyimpan sudut putaran saat ini
    current_azim = 0
    
    # Fungsi untuk memutar kubus
    def rotate():
        global current_azim
        current_azim += 20
        ax.view_init(azim=current_azim)
        canvas.draw()
        
    # Membuat frame untuk matplotlib figure
    frame = tk.Frame(root)
    frame.pack(side=tk.TOP, pady=50)

    # Membuat figure dan axes untuk 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Membuat kubus
    Z = np.array([[0, 0, 0],
                  [1, 0, 0],
                  [1, 1, 0],
                  [0, 1, 0],
                  [0, 0, 1],
                  [1, 0, 1],
                  [1, 1, 1],
                  [0, 1, 1]])

    r = [-1,1]

    X, Y = np.meshgrid(r, r)
    # plot vertices
    ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

    # list of sides' polygons of figure
    verts = [[Z[0],Z[1],Z[5],Z[4]], [Z[7],Z[6],Z[2],Z[3]], [Z[0],Z[1],Z[2],Z[3]], 
             [Z[7],Z[6],Z[5],Z[4]], [Z[7],Z[3],Z[0],Z[4]], [Z[1],Z[2],Z[6],Z[5]]]

    # plot sides
    ax.add_collection3d(Poly3DCollection(verts, facecolors='cyan', linewidths=1, edgecolors='r', alpha=.25))

    # Membuat matplotlib canvas dan memasukkannya ke dalam tkinter frame
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Membuat tombol untuk memutar kubus
    button = tk.Button(root, text="Putar Kubus", command=rotate)
    button.pack(side=tk.TOP)

# Membuat jendela tkinter dan memberikan judul
root = tk.Tk()
root.geometry("800x600")
root.title("Membuat gambar 3 Dimensi")

# Membuat tombol untuk membuat kubus
button = tk.Button(root, text="Buat Kubus", command=load_and_open)
button.pack(side=tk.TOP)

root.mainloop()
