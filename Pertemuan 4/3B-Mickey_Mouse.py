print("\033c")
#Import libraries
import matplotlib.pyplot as plt
import numpy as np

# Tentukan wilayah (domain) diagram Cartesian dan rasio lebar dan tinggi diagram
x = np.linspace(-3,13,10000)
plt.figure(figsize=(8,6.5))

# Tentukan persamaan matematika yang diinginkan
y = x-x-0
y1 = 5+(25-(x-5)**2)**0.5
y2 = 5-(25-(x-5)**2)**0.5

y3 = 9+(4-(x-11)**2)**0.5
y4 = 9-(4-(x-11)**2)**0.5

y5 = 9+(4-(x + 1)**2)**0.5
y6 = 9-(4-(x + 1)**2)**0.5



plt.plot(x,y, '-k')
plt.plot(x,y1,'-k', label='y1, y2')
plt.plot(x,y2,'-k')
plt.plot(x,y3,'-k', label='y3, y4')
plt.plot(x,y4,'-k')
plt.plot(x,y5,'-k', label='y5, y6')
plt.plot(x,y6,'-k')

plt.legend(loc='upper center')
plt.grid()
plt.show()