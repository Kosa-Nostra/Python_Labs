primer = input("Введите математический пример: ")
if '+' in primer:
    num1, num2 = primer.split('+')
    result = float(num1) + float(num2)
    print("Результат:", result)
elif '-' in primer:
    num1, num2 = primer.split('-')
    result = float(num1) - float(num2)
    print("Результат:", result)
elif '*' in primer:
    num1, num2 = primer.split('*')
    result = float(num1) * float(num2)
    print("Результат:", result)
elif '/' in primer:
    num1, num2 = primer.split('/')
    if float(num2) == 0:
        print("Делить на ноль нельзя!")
    else:
        result = float(num1) / float(num2)
        print("Результат:", result)
else:
    print("Неправильное выражение")
