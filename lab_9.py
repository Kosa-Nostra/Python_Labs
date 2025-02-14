import string
import os

# Функция для подсчета знаков препинания в строке
def count_punctuation(line):
    punctuation_count = {punct: 0 for punct in string.punctuation}  # Словарь для подсчета каждого знака
    total_punctuation = 0

    # Пройдем по каждому символу строки и считаем знаки препинания
    for char in line:
        if char in string.punctuation:
            punctuation_count[char] += 1
            total_punctuation += 1

    return total_punctuation, punctuation_count


file_name = "/Users/kossa/Desktop/Lab_9.txt"

# Проверяем, существует ли файл
if os.path.exists(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        total_lines = 0  # Счётчик строк в файле
        total_punctuation = 0  # Общее количество знаков препинания

        # Чтение построчно
        for line in file:
            total_lines += 1
            line = line.strip()  # Убираем лишние пробелы и символы новой строки
            line_punctuation, punctuation_count = count_punctuation(line)
            total_punctuation += line_punctuation

            # Вывод информации по каждой строке
            print(f"Строка {total_lines}: {line}")
            print(f"Общее количество знаков препинания: {line_punctuation}")
            for punct, count in punctuation_count.items():
                if count > 0:
                    print(f"  '{punct}': {count}")

        print("\nОбщее количество строк в файле:", total_lines)
        print("Общее количество знаков препинания:", total_punctuation)
else:
    print(f"Ошибка: файл {file_name} не найден.")
