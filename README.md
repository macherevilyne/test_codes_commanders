Проект Users and Orders
для запуска проекта вам понадобится:
1. Установить все зависимости командой pip install -r requirements.txt
2. Настроить подключение к PostgreSQL например с помощью DBeaver
3. Выполнить миграции командой python manage.py makemigrations, а так же python manage.py migrate
4. Создать суперпользователя python manage.py createsuperuser
О проекте:
Веб приложение хранит информацию о пользователях и заказах. Через главную страницу можно попасть на страницу API, где
можно получать информацию о пользователях и заказах, создавать новые записи в БД, а также изменять записи
Либо на страницу API можно попасть перейдя по адресу http://127.0.0.1:8000/api/
База данных подключена PostgreSQL
Проект использует Swagger для автоматической генерации и визуализации документации API, можно перейти по адресу
http://127.0.0.1:8000/swagger/

Приложение упаковано в Docker, для взаимодействия приложения django и базы данных Postgres используется docker-compose
