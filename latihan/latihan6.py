import numpy as np
import matplotlib.pyplot as plt

# Membuat array nilai x dari -5 sampai 5 dengan 100 titik
x = np.linspace(-5, 5, 100)

# Menghitung nilai y untuk masing-masing fungsi matematika
y1 = 3 * x + 4
y2 = 2 * (x**2) + 1
y3 = (x**3) + 9

# Plot setiap fungsi dengan warna dan label yang berbeda
plt.plot(x, y1, color='blue', label='y = 3x + 4')
plt.plot(x, y2, color='red', label='y = 2x^2 + 1')
plt.plot(x, y3, color='green', label='y = x^3 + 9')

# Menambahkan judul, label sumbu, dan legenda
plt.title('Plot Multiple Math Functions')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Menampilkan grafik
plt.show()