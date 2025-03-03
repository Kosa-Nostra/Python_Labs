import re

phone_shablon = r"^(?:\+7|8|7)\d{10}$"

phone_numbers = [
    "+79161234567",  # Лишние цифры
    "89161234567",      # Корректный
    "+7-916-123-45-67", # Корректный (без дефисов)
    "7-916-123-45-67",  # Корректный (без дефисов)
    "9161234567",        # Неполный номер
    "79782364106"
]

# Проверка каждого номера и вывод только соответствующих
for phone in phone_numbers:
    cleaned_phone = phone.replace("-", "").replace(" ", "")
    if re.match(phone_shablon, cleaned_phone):
        print(phone)
