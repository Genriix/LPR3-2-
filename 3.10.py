cities = ['Воркута', 'Инта', 'Печёра', 'Ухта']  # Создаём список
print(cities)  # Выводим на экран

print(cities[3])  # Выводим конкретное значение

message = "Я живу в " + cities[0] + "."  # Вводим переменную, куда добавляем сообщение и значение из списка

cities.append('Сыктывкар')  # Добавляем в конец списка город
print(cities)

cities.remove('Воркута')  # Убираем поределённое значение
print(cities)

cities.sort()  # Осртируем в алф. порядке
print(cities)

cities.reverse()  # Перемешиваем список
print(cities)

print(len(cities))  # Считаем кол-во городов
