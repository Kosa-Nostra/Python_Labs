# Родительский класс
class Aircraft:
    def __init__(self, brand, speed):
        self.brand = brand  # Марка
        self.speed = speed  # Скорость

    # Метод 1: инфо
    def info(self):
        return f"Марка: {self.brand}, скорость: {self.speed} км/ч"

    # Метод 2: взлет
    def takeoff(self):
        return f"{self.brand} взлетает!"

    # Метод 3: посадка
    def land(self):
        return f"{self.brand} садится."

    # Метод 4: движение
    def move(self):
        return f"{self.brand} движется со скоростью {self.speed} км/ч."

# Дочерний класс
class Airplane(Aircraft):
    def __init__(self, brand, speed, passengers):
        super().__init__(brand, speed)  # Наследуем свойства brand и speed от родителя
        self.passengers = passengers  # Свойство: пассажиры

    # Метод 5 (свой): самолет может выполнять полет
    def fly(self):
        return f"{self.brand} летит на высоте 10,000 метров."

    # Переопределим метод takeoff для самолета
    def takeoff(self):
        return f"{self.brand} взлетает на аэродроме с пассажирами!"

# Создаем объект класса Airplane
airplane = Airplane("Boeing 747", 900, 400)

# Используем методы родительского класса
print(airplane.info())
print(airplane.move())
print(airplane.land())

# Используем метод, добавленный в дочернем классе
print(airplane.fly())

# Используем переопределенный метод takeoff
print(airplane.takeoff())
