num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
oper = input("Введите арифметическую операцию: ")
if oper == '+':
    result = num1 + num2
elif oper == '-':
    result = num1 - num2
elif oper == '*':
    result = num1 * num2
elif oper == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Делить на ноль нельзя!"
else:
    result = "Это не операция!"
print("Результат:", result)