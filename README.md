# Описание 

Католог / конструктор коктейлей

## Наименование

DrunkMate

## Предметная область

Коктейльная карта

# Данные

Коктейли, пользователи, ингредиенты, отзывы, картинки, (тэги?)

## Для каждого элемента данных - ограничения

[DrunkDiagram.drawio](https://github.com/Rudovich1/DrunkMate/blob/main/DrunkDiagram.drawio)

## Общие ограничения целостности

### Добавления:

- Создание аккаунта -> создание картинки
- Создание ингредиента  -> создание картинки
- Создание коктейля пользователем -> создание картинки
- Написание отзыва 
- Создание тэга

### Удаления:

- Удаление акканута -> удаление картинки
- Удаление коктейля -> удаление комментариев, удаление картинки
- Удаление ингредиентов -> удаление картинки, удаление коктейлей с этим ингредиентом 
- Удаление отзыва

# Пользовательские роли

- Пользователь
- Модератор

## Для каждой роли - наименование, ответственность, количество пользователей в этой роли

### Пользователь

- `DrunkMate`
- Создание коктейлей, редактирование собственных коктейлей, создание отзывов, редактирование собственных отзывов, создание ингредиентов, управление собственным аккаунтом
- количество ограничено пропускной способностью сервиса

### Модератор

- `DrunkMaster`
- Бог и судья (удаление и редактирование любых сущностей)
- 2 шт

# UI / API 

- WEB интерфейс (пользовательское взаимодействие)
- API HTTP (модерация)

# Технологии разработки
## Язык программирования

- python
- (frontend ...?)

## СУБД

PostgreSQL

# Тестирование

- unit тестирование
- интеграционное тестирование
