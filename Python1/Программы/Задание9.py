# 5.Класс Persona содержит информацию о ФИО человека, дате рождения и адресе человека. Метод подсчитывает количество дней оставшихся до следующего дня рождения. По заданному ФИО человека узнать количество дней оставшихся до следующего дня рождения.

from datetime import datetime, timedelta

class Persona:
    def __init__(self, fio, birth_date, address):
        self.fio = fio
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")
        self.address = address
    
    def days_until_birthday(self):
        today = datetime.now()
        next_birthday = self.birth_date.replace(year=today.year)

        # Если день рождения уже прошел в этом году, берем следующий год
        if next_birthday < today:
            next_birthday = self.birth_date.replace(year=today.year + 1)
        
        days_remaining = (next_birthday - today).days
        return days_remaining

# Пример использования класса
people = [
    Persona("Иванов Иван Иванович", "1990-05-24", "ул. Пушкина, д. 1"),
    Persona("Петров Петр Петрович", "1985-11-02", "ул. Лермонтова, д. 2"),
    Persona("Сидорова Анна Сергеевна", "1993-07-15", "ул. Чехова, д. 3")
]

# Поиск человека по ФИО и вывод количества дней до следующего дня рождения
fio_to_search = input("Введите ФИО для поиска: ")
person_found = None

for person in people:
    if person.fio == fio_to_search:
        person_found = person
        break

if person_found:
    days_left = person_found.days_until_birthday()
    print(f"До следующего дня рождения {fio_to_search} осталось {days_left} дней.")
else:
    print(f"Человек с ФИО {fio_to_search} не найден.")
