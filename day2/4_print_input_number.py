"""
Считывает введённое пятизначное число
и каждую его цифру выводит в новой строке
"""

message = 'Введите пятизначное число'

while True:
    input_value = input(f'{message}: ')

    try:
        input_value = int(input_value)

        if not (0 < (input_value // 10000) < 10):
            print('[Ошибка]: Число должно быть пятизначным.')
        else:
            break

    except ValueError as er:
        print("[Ошибка]: Введённое значение не является числом.")

    message = "Попробуйте ещё раз"

input_value = str(input_value)
count = 1

for i in input_value:
    print(f'{count} цифра: {i}')
    count = count + 1
