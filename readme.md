Для запуска приложения используйте переменную

FLASK_APP=microblog.py

затем 

flask run

Возможно использовать команду flask shell для отладки приложения

Ссылка на урок https://habr.com/ru/post/346346/

Миграции базы данных

После того как описана структура базы в models.py пишем в консоли:
flask db init - для создания БД
flask db migrate - создает, подготавливает миграцию базы
flask db upgrade - вносит изменения в саму базу

Для поддержки sqllite удаления колонок и таблиц нужно в __init__.py добавить render_as_batch=True в функцию migrate = Migrate(app,db,render_as_batch=True)