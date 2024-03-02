# EducationSystem - Сервис обучения.

[//]: # (![workflow]&#40;https://github.com/artemis1359/foodgram-project-react/actions/workflows/main.yml/badge.svg&#41;)


## Описание проекта
EducationSystem — сервис для предоставление продуктов, доступа к урокам продукта, а также распределения по группам.

## Технологии

- [Python 3.9.6](https://www.python.org/downloads/)
- [Django 4.2.10](https://www.djangoproject.com/)
- [Django Rest Framewok 3.14](https://www.django-rest-framework.org/)
- [SQLite 3.39.5](https://www.sqlite.org/)

 
## Установка проекта на локальный компьютер из репозитория 
 - Клонировать репозиторий `git clone git@github.com:Artemis1359/EducationSystem.git`
 - перейти в директорию с клонированным репозиторием
 - установить виртуальное окружение `python3 -m venv venv`
 - активировать виртуальное окружение `source venv/bin/activate` (Linux/masOS), `source venv/Scripts/activate` (Windows)
 - установить зависимости `pip install -r requirements.txt`
 - выполнить миграции `python3 manage.py migrate`
 - запустить сервер `python3 manage.py runserver`


```http://127.0.0.1:8000/api/v1/``` - api проекта

```http://127.0.0.1:8000/api/v1/products/``` - Продукты (Доступ для всех авторизированных пользователей, дана основная ифнормцаия, включая количество уроков в продукте)

```http://127.0.0.1:8000/api/v1/products/<pk>/``` - Продукт <pk> (Доступ есть у всех авторизованных пользователей, в случае, если товар приобретен добавляется информация об уроках по данному продукту)

```http://127.0.0.1:8000/api/v1/products/<pk>/purchase/``` - Приобретение товара <pk>

```http://127.0.0.1:8000/api/v1/lessons/``` - Уроки, доступ к которым есть у пользователя

```http://127.0.0.1:8000/api/v1/lessons/<pk>/``` - Детальная информация об уроке, только если к нему есть доступ


```http://127.0.0.1:8000/api/v1/groups/``` - Группы (доступ к группам. в которых есть отправитель запроса)

```http://127.0.0.1:8000/api/v1/groups/<pk>/``` - Детальная информация о группе <pk>

```http://127.0.0.1:8000/api/docs/``` - документация проекта



## Автор
Потапов Артем - [GitHub](https://github.com/artemis1359)