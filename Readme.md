# Тестовое задание
***
### Содержание
- [1. Продуктовый Магазин](#1продуктовый-магазин)
    - [1.1 Установка и запуск](#11-установка-и-запуск)
    - [1.2 Аутентификация](#12-аутентификация)
    - [1.3 Категории и продукты](#13-категории-и-продукты)
        - [1.3.1 Категории](#131-категории)
        - [1.3.2 Подкатегории](#132-подкатегории)
        - [1.3.3 Продукты](#133-продукты)
        - [1.3.4 Фильтрация и поиск](#134-фильтрация-и-поиск)
        - [1.3.5 Примеры](#135-примеры)
    - [1.4 Корзина](#14-корзина)
        - [1.4.1 Получить содержимое корзины](#141-получить-содержимое-корзины)
        - [1.4.2 Добавить товар](#142-добавить-товар)
        - [1.4.3 Обновить количество](#143-обновить-количество)
        - [1.4.4 Удалить товар](#144-удалить-товар)
        - [1.4.5 Очистить корзину](#145-очистить-корзину)
- [2. Генератор последовательностей](#2-генератор-последовательностей)
    - [2.1 Запуск](#21-запуск)

***

# 1.Продуктовый магазин

REST API для продуктового магазина, реализованный на Django REST Framework. Включает модели категорий, подкатегорий, продуктов, изображений и корзины с поддержкой фильтрации, поиска, пагинации и JWT-аутентификации.

***

## 1.1 Установка и запуск
#### - копируйте репозиторий
```
git clone https://github.com/goqwertys/grocery_store.git
cd grocery_store
```
#### - Установите зависимости
```
pip install -r requirements.txt
```

#### - Создайте файл `.env` с конфигурациями по образцу `.env.sample`.
```
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=your_db_name
DB_USER=db_user
DB_PASSWORD=secret_password
DB_HOST=localhost
DB_PORT=
```

#### - Примените миграции
```
python manage.py migrate
```


#### - Создайте суперпользователя
```
python manage.py createsuperuser
```

#### - Запустите сервер
```
python manage.py runserver
```
#### - Загрузите данные из фикстур:
```
python manage.py loaddata categories.json subcategories.json products.json product_images.json
```
***

## 1.2 Аутентификация

JWT-аутентификация через `simplejwt`
Получение токенов:
```
POST /api/token/
{
  "username": "user",
  "password": "secretpassword"
}
```
```
POST /api/token/refresh/
{
  "refresh": "..."
}
```
Добавляйте `Authorization: Bearer <access_token>` в заголовки для защищённых запросов.

***

## 1.3 Категории и продукты

#### 1.3.1 Категории
```
GET /api/categories/
GET /api/categories/<slug>/
```
#### 1.3.2 Подкатегории
```
GET /api/subcategories/
GET /api/subcategories/<slug>/
```
#### 1.3.3 Продукты
```
GET /api/products/
GET /api/products/<slug>/
```
### 1.3.4 Фильтрация и поиск:

| Параметр       |  Тип   | Описание                                 |
|----------------|:------:|------------------------------------------|
| `search`       | string | Поиск по названию (нечёткое совпадение)  |
| `category`     | string | Slug категории (например, fruits)        |
| `subcategory`  | string | Slug подкатегории (например, berries)    |
| `ordering`     | string | `price`, `-price`, `name`, `-name`       |

#### 1.3.5 Примеры:
```
GET /api/products/?search=яблоко
GET /api/products/?category=fruits&subcategory=berries
GET /api/products/?ordering=-price
```
***
## 1.4 Корзина
###  1.4.1 Получить содержимое корзины:
```
GET /api/cart/
```
### 1.4.2 Добавить товар
```
POST /api/cart/add/
```
##### Тело запроса:
```
{
  "product": 1,
  "quantity": 2
}
```
##### Ответ:
```
{ "status": "Product added to cart" }
```
##### Ошибка (обязательные поля не переданы):
```
{
  "product": ["This field is required."],
  "quantity": ["This field is required."]
}
```
### 1.4.3 Обновить количество
```
PATCH /api/cart/update_item/
```
#### Тело запроса:
```
{
  "product": 1,
  "quantity": 5
}
```
#### Ответ:
```
{ "status": "Quantity updated" }
```
### 1.4.4 Удалить товар
```
DELETE /api/cart/remove/
```
#### Тело запроса:
```
{ "product": 1 }
```
#### Ответ:
```
{ "status": "Item removed" }
```
### 1.4.5 Очистить корзину:
```
DELETE /api/cart/clear/
```
#### Ответ:
```
{ "status": "Cart cleared" }
```
***

# 2. Генератор последовательностей
Программа, которая выводит n первых элементов последовательности `122333444455555...` (Число повторяется столько раз, чему оно равно) 
## 2.1 Запуск
```
python sequence_generator/sequence.py 
```