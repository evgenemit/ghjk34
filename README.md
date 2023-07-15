# Установка и запуск

## - Установка с Docker

1. Клонируйте репозиторий:

```bash
$ git clone https://github.com/veeedmochka/ghjk34.git
$ cd ghjk34
```

2. Создайте `.env.docker` файл с переменными окружения:

```bash
SECRET_KEY=example
DEBUG=False
HOST_1=localhost
DB_NAME=ghjk34
DB_USER=ghjk_user
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

3. Запустите `docker-compose`:

```bash
$ docker-compose up
```

## - Обычная установка

1. Клонируйте репозиторий:

```bash
$ cd /var/www
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
HOST_1=localhost
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

5. Установите необходимые зависимости:

```bash
$ pip install -r requirements.txt
```

6. Запустите миграции:

```bash
$ python3 manage.py migrate
```

7. Соберите статические файлы:

```bash
$ python3 manage.py collectstatic
```

8. В каталоге `/etc/systemd/system/` создайте файлы `gunicorn.service` и `gunicorn.socket`:

gunicorn.service:

```bash
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/ghjk34
ExecStart=/var/www/ghjk34/venv/bin/gunicorn --workers 5 --bind unix:/run/gunicorn.sock config.wsgi:application

[Install]
WantedBy=multi-user.target
```

gunicorn.socket:
```bash
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

9. В каталоге `/etc/nginx/sites-available/` создайте файл `ghjk34`:

```bash
server {
    listen 80;
    server_name localhost;

    location /static/ {
        alias /var/www/ghjk34/staticfiles/;
    }

    location / {
        proxy_pass http://unix:/run/gunicorn.sock;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```

10. Создайте символическую ссылку на этот файл в каталоге `/etc/nginx/site-enabled/`:

```bash
$ sudo ln -s /etc/nginx/sites-available/ghjk34 /etc/nginx/sites-enabled/
```

11. Запустите службу gunicorn:

```bash
$ sudo systemctl enable gunicorn
$ sudo systemctl start gunicorn
```

12. Запустите nginx:

```bash
$ sudo service nginx start
```

Теперь приложение доустпно по адресу `http://localhost/`
