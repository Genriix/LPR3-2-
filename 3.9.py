spisok = ['name1', 'Petya', 'Gg']  # Создаем список с гостями
spisok.insert(0, 'Natasha')  # Добавляем еще гостей
spisok.insert(1, 'Olya')  # Добавляем еще гостей
spisok.append('Anton')  # Добавляем еще гостей
message_0 = 'К сожалению, ко мне могут придти только два гостя'  # Пишем сообщение
print(message_0)  # Выводим сообщение на экран

not_going0 = spisok.pop(0)
not_going1 = spisok.pop(1)
not_going2 = spisok.pop(2)
not_going3 = spisok.pop(2)

message0 = 'Не приходи, ' + not_going0
message1 = 'Не приходи, ' + not_going1
message2 = 'Не приходи, ' + not_going2
message3 = 'Не приходи, ' + not_going3

print(message0)
print(message1)
print(message2)
print(message3)
print(spisok)
print(len(spisok))  # СМОТРИМ КОЛИЧЕСТВО ГОСТЕЙ ПО СПИСКУ
