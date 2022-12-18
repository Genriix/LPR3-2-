spisok = ['Аня', 'Пётр', 'Василий']  # Создаем переменую со списком гостей
spisok.insert(0, 'Наталья')  # С помощью метода insert добавляем Наташу в начало списка
spisok.insert(3, 'Ольга')  # С помощью метода insert добавляем Олю в середину списка
spisok.append('Антон')  # С помощью метода append добавляем Антона в конец списка
F_message = "Привет, "
L_message = ", приходи в гости!"
message_0 = F_message + spisok[0] + L_message  # Приглашаем новых гостей на чай
message_1 = F_message + spisok[1] + L_message  # Приглашаем новых гостей на чай
message_2 = F_message + spisok[2] + L_message  # Приглашаем новых гостей на чай
message_3 = F_message + spisok[3] + L_message  # Приглашаем новых гостей на чай
message_4 = F_message + spisok[4] + L_message  # Приглашаем новых гостей на чай
message_5 = F_message + spisok[5] + L_message  # Приглашаем новых гостей на чай
print(message_0)  # Выводим новые приглашения на экран
print(message_1)  # Выводим новые приглашения на экран
print(message_2)  # Выводим новые приглашения на экран
print(message_3)  # Выводим новые приглашения на экран
print(message_4)  # Выводим новые приглашения на экран
print(message_5)  # Выводим новые приглашения на экран
