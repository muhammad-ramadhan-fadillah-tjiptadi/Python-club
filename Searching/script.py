# Data adalah array/list yang ingin dicari
# Target adalah nilai yang ingin ditemukan didalam list
# Searching dengan python
# Linear Search = cek data satu per satu dan menghasilkan output index
def linear_search (data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Binary Search
angka = [10, 20, 30, 40, 50]
print(linear_search(angka, 30))

def binary_search(data, target):
    low, high = 0, len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

angka = [10, 20, 30, 40, 50]
print(binary_search(angka, 40)) # Output: 3

# Study Case
# Linear search
def linear_search (data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

nilai_ujian = [65,70,80,85,90,95]
print(linear_search(nilai_ujian, 95))

# Binary Search
def binary_search(data, target):
    low, high = 0, len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search(nilai_ujian, 85))