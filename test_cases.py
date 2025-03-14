import random


def generate_test(n, x_range, k_range, alarm_range):
    # n: количество будильников
    # x_range: диапазон для x (например, (1, 10**9))
    # k_range: диапазон для k (например, (1, 10**9))
    # alarm_range: диапазон для alarms (например, (1, 10**9))

    x = random.randint(*x_range)
    k = random.randint(*k_range)
    alarms = [random.randint(*alarm_range) for _ in range(n)]

    # Формируем строку входных данных: первая строка - n, x, k, затем n чисел через пробел
    test_input = f"{n} {x} {k}\n" + " ".join(map(str, alarms)) + "\n"
    return test_input


# Пример генерации теста:
n = 10 ** 5
test_input = generate_test(n, (1, 10 ** 9), (1, 10 ** 9), (1, 10 ** 9))
with open("test_case.txt", "w") as f:
    f.write(test_input)
print("Тестовый пример сгенерирован в файл test_case.txt")
