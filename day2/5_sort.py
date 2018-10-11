"""
Сортировка выбором
"""

arr = [0, 3, 24, 2, 3, 7]
length = len(arr)

print("Исходный список: ", arr)

for i in range(length):
    for j in range(length):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Отсортированный: ", arr)
