#LOW LEVEL CODING FOR CREATING POINTS
print("\033c") #To close all
import numpy as np
import matplotlib.pyplot as plt

x1 = 100
y1 = 200
x2 = 100
y2 = 1000

lw = int(10)

hw = int(lw/2)

# Calculate the slope of the line
m_x = (x2 - x1) / (y2 - y1)

row = int(5/7*3000)
col = int(5/7*1920)

# Define the function to calculate x for a given y
def calculate_x(y):
    return m_x * (y - y1) + x1

def draw_thick_point(x, y, color, thickness):
    for i in range(x-thickness, x+thickness):
        for j in range(y-thickness, y+thickness):
            if((i-x)**2 + (j-y)**2)<thickness**2:
                Gambar[j, i] = color

def draw_point(x, y, color):
    for i in range(x-hw, x+hw):
        for j in range(y-hw, y+hw):
            if((i-x)**2 + (j-y)**2)<hw**2:
                Gambar[j, i] = color


print('col, row = ', col, ', ', row)

Gambar = np.zeros(shape=(row, col, 3), dtype = np.int16)

for y in range(y1, y2, lw*2):  # Step size is twice the line width to create a dotted line
    x = int(calculate_x(y))
    draw_point(x, y, [255, 0, 0])  # Draw a red point

draw_thick_point(x1, y1, [255, 0, 0], hw*2)
draw_thick_point(x2, y2, [255, 0, 0], hw*2)

plt.figure()
plt.imshow(Gambar)
plt.show()