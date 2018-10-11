"""
Сортировка пузырьком
"""

arr = [0, 3, 24, 2, 3, 7]
last = len(arr)
current = 0

print("Исходный список: ", arr)

while current < last:
    following = current + 1

    if following == last:
        break

    if arr[current] > arr[following]:
        arr[current], arr[following] = arr[following], arr[current]
        current = current - 1
    else:
        current = current + 1

print("Отсортированный: ", arr)
