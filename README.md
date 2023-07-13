## Установка и запуск

1. Клонируйте репозиторий:

```bash
$ git clone https://github.com/veeedmochka/ghjk34.git
$ cd ghjk34
```

2. Создайте базу данных:

```bash
CREATE DATABASE ghjk34;
CREATE USER ghjk_user WITH PASSWORD 'password';
ALTER ROLE ghjk_user SET client_encoding TO 'utf8';
ALTER ROLE ghjk_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE ghjk_user SET timezone TO 'Europe/Minsk';
GRANT ALL PRIVILEGES ON DATABASE ghjk34 TO ghjk_user;
\c ghjk34
GRANT ALL ON SCHEMA public TO ghjk_user;
GRANT ALL ON SCHEMA public TO public;
```

3. Добавьте `.env` файл с переменными окружения:

```bash
SECRET_KEY=example
DEBUG=False
DB_NAME=ghjk34
DB_USER=ghjk_user
DB_PASSWORD=password
DB_HOST=127.0.0.1
DB_PORT=5432
```

4. Создайте и активируйте виртуальное окружение:

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

5. Установите необходимые зависимости

```bash
$ pip install -r requirements.txt
```

6. Запустите миграции

```bash
$ python3 manage.py migrate
```

