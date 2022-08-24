# odkl09

Данная инструкция предполагает что на вашем устройстве установлена операционная система Ubuntu 20.04, 
а также следующее программное обеспечение: git, pipenv, python3. 

 <ul>
  <li>
    Открываем терминал и идем в директорию где будет рассполагаться проект. Далее запускаем команду:
  
```
git clone git@github.com:Tsimafei-Khamitsevich/odkl09.git
```
  </li>
  <li>
    Переходим в <b>odkl09</b> директорию и запускаем следующие команды:

```
pipenv shell
pipenv install django
pipenv install psycopg2-binary
```
  </li>
  <li>
    Далее следует установка и настройка Postgresql. Подробное описанние значения этих комманд можно найти в следующей 
    статье https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-20-04.
    
```
sudo apt install postgresql postgresql-contrib
sudo -u postgres psql
CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';
ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC+3';
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
\q
```
  </li>
  <li>
    Запускаем сервер.
    
```
python manage.py runserver
```
  </li>
 </ul> 
 
 
 
