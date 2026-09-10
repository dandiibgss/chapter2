# Example 2.9 (Modified for Sorting)
def sortarray(xs):
    # Membuat salinan list agar data asli tidak terubah secara langsung
    arr = xs.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Menukar posisi jika elemen kiri lebih besar dari elemen kanan
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

data = [4, 2, 5, 0, 1, 3]
t = sortarray(data)
print(t)