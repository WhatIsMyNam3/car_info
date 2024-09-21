# CarInfo

Веб-приложение для управления информацией об автомобилях.

## Установка

Клонируйте репозиторий

```bash
git clone https://github.com/WhatIsMyNam3/CarInfo.git
cd CarInfo
```
Создайте виртуальное окружение
```bash
python -m venv venv
```
Активируйте виртуальное окружение:
1. На Windows:
```bash
venv\Scripts\activate
```
2. На macOS/Linux:
```bash
source venv/bin/activate
```
Установите зависимости
```bash
pip install -r requirements.txt
```
Создайте файл .env в корневой папке приложения и заполните его

```makefile
SECRET_KEY=
DEBUG= 
```
## Выполнение миграции базы данных
Запустите следующие команды для применения миграций
```bash
python manage.py makemigrations
python manage.py migrate
```
## Запуск сервера разработки
```bash
python manage.py runserver
```
Сервер будет доступен по адресу: http://127.0.0.1:8000/

## Использование API
Для использования API необходимо зарегистрироваться в веб-приложении и получить токен по адресу:
* POST /api/token/ — получение токена для использования API.
---
* GET /api/cars/ — получение списка автомобилей.
* GET /api/cars/<id>/ — получение информации о конкретном автомобиле.
* POST /api/cars/ — создание нового автомобиля.
* PUT /api/cars/<id>/ — обновление информации о автомобиле.
* DELETE /api/cars/<id>/ — удаление автомобиля.
* GET /api/cars/<id>/comments/ — получение комментариев к автомобилю.
* POST /api/cars/<id>/comments/ — добавление нового комментария к автомобилю.






