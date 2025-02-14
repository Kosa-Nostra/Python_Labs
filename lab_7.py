def recurs(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a

    # Рекурсия: складываем a b раз
    return a + recurs(a, b - 1)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

result = recurs(num1, num2)
print("Произведение:", result)
