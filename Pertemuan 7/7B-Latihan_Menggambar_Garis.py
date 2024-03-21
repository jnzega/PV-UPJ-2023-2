#LOW LEVEL CODING FOR CREATING POINTS
print("\033c") #To close all
import numpy as np
import matplotlib.pyplot as plt

#The user informs the coordinates of the two points for the line.
x1 = 100
y1 = 200
x2 = 800
y2 = 600

#The user decides the line width
lw = int(10)

#Calculate the half line width
hw = int(lw/2)
# Calculate the slope of the line
m_y = (y2 - y1) / (x2 - x1)

# Define the function to calculate y for a given x
def calculate_y(x):
    return m_y * (x - x1) + y1

def draw_thick_point(x, y, color, thickness):
    for i in range(x-thickness, x+thickness):
        for j in range(y-thickness, y+thickness):
            if((i-x)**2 + (j-y)**2)<thickness**2:
                Gambar[j, i] = color
# Define the function to draw a point
def draw_point(x, y, color):
    for i in range(x-hw, x+hw):
        for j in range(y-hw, y+hw):
            if((i-x)**2 + (j-y)**2)<hw**2:
                Gambar[j, i] = color

#Setting the size of the canvas
row = int(5/7*1080)
col = int(5/7*1920)
print('col, row = ', col, ', ', row)

#Preparing the black canvas
Gambar = np.zeros(shape=(row, col, 3), dtype = np.int16)

# Draw a dotted line between the two points
for x in range(x1, x2, lw*2):  # Step size is twice the line width to create a dotted line
    y = int(calculate_y(x))
    draw_point(x, y, [255, 0, 0])  # Draw a red point

# Menggambar titik tebal pada koordinat awal dan akhir
draw_thick_point(x1, y1, [255, 0, 0], hw*2)  # Menggambar titik merah tebal
draw_thick_point(x2, y2, [255, 0, 0], hw*2)  # Menggambar titik merah tebal

plt.figure()
plt.imshow(Gambar)
plt.show()