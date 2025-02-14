vvod = input("Введите строку: ")
reversed_string = ""
for i in range(len(vvod) - 1, -1, -1):
    reversed_string += vvod[i]  # Добавляем символ в новую строку

print("Наша строка наоборот:", reversed_string)
