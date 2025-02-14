def menu():
    print("Выберите операцию:")
    print("1. Добавить элемент в конец списка")
    print("2. Добавить элемент на определенную позицию")
    print("3. Удалить элемент по индексу")
    print("4. Удалить элемент по значению")
    print("5. Размер списка")
    print("6. Сортировать список по возрастанию")
    print("7. Сортировать список по убыванию")
    print("8. Вывести список")
    print("9. Выйти")

def main():
    lst = []
    while True:
        menu()
        choice = input("Введите номер операции: ")

        if choice == '1':  # Добавить элемент в конец
            element = input("Введите элемент для добавления: ")
            lst.append(element)

        elif choice == '2':  
            index = int(input("Введите индекс для вставки: "))
            element = input("Введите элемент для вставки: ")
            lst.insert(index, element)

        elif choice == '3':
            index = int(input("Введите индекс для удаления: "))
            if 0 <= index < len(lst):
                del lst[index]
            else:
                print("Неверный индекс.")

        elif choice == '4':
            element = input("Введите элемент для удаления: ")
            if element in lst:
                lst.remove(element)
            else:
                print("Элемент не найден.")

        elif choice == '5':
            print(f"Размер списка: {len(lst)}")

        elif choice == '6':
            lst.sort()
            print("Список отсортирован по возрастанию.")

        elif choice == '7':
            lst.sort(reverse=True)
            print("Список отсортирован по убыванию.")

        elif choice == '8':
            print("Список:", lst)

        elif choice == '9':  # Выход
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
