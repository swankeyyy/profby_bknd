# Project Name: Profby Backend

## Описание
Backend часть для проекта prof.by, который призван помочь любому желающему ощутить себя в новой профессии. Фронденд часть выполнена с помощью React, база данных реализована на PostgreSQL

## Возможности
- Реализована панель администратора с возомжностью добавки нового контента
- База данных Postgres
- Реализованы все адреса для подгрузки динамического контена из API во фронтенд часть

## Установка
1. Скопировать репозиторий:
    ```bash
    git clone https://github.com/yourusername/profby_bknd.git
    ```
2. Перейти в проект:
    ```bash
    cd profby_bknd
    ```
3. Запустить проект в докере:
    ```bash
    docker-compose up --build
    ```
4. Перейти в контейнер и выполнить миграции:
    ```
    docker-compose exec web /bin/sh
    alembic upgrade heads
    ```
    
## Использование
1. Сервер автоматически запустится после запуска доке-контейнеров.
2. Документация доступна по адресу `http://localhost:8000/`.
3. Админ панель доступна по адресу `http://localhost:8000/admin`

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, please contact swankyyy@gmail.com.

