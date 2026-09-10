import math

# Membaca deretan angka dari keyboard dan mengonversinya menjadi list of float
s = input("Input a list of numbers: ")
numbers = list(map(float, s.split()))

# Menghitung nilai sine untuk setiap angka dan menampilkan hasilnya
for x in numbers:
    y = math.sin(x)
    print("The sine of " + str(x) + " is " + str(y))