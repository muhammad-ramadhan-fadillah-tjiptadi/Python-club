list = [10, 11, 12]
print(list)

# A - Z
fruits = ['mango', 'apple', 'banana']
asc = sorted(fruits)
print("Ascending:", asc)

# Z - A
desc = sorted(fruits, reverse=True)
print("Descending:", desc)

students = [
    {"name": "Asep", "score": 25},
    {"name": "Reza", "score": 22},
    {"name": "Faiq", "score": 28}
]

# Urutan dari score
sorted_by_score = sorted(students, key=lambda x: x["score"])
print(sorted_by_score)

# Urutan dari name
sorted_by_name = sorted(students, key=lambda x: x["name"])
print(sorted_by_name)

# Sorting dengan python
# Bubble sort
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data
angka = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(angka))

# Selection sort
def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]
    return data
angka = [64, 25, 12, 22, 11]
print(selection_sort(angka))

# Study Case
def bubble_sort(nilai_ujian):
    n = len(nilai_ujian)
    for i in range(n):
        for j in range(0, n-i-1):
            if nilai_ujian[j] > nilai_ujian[j+1]:
                nilai_ujian[j], nilai_ujian[j+1] = nilai_ujian[j+1], nilai_ujian[j]
    return nilai_ujian
nilai_ujian = [75, 65, 80, 80, 85, 70, 90]
print(bubble_sort(nilai_ujian))