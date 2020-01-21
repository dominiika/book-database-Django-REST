# book-database-Django-REST

See the app at:
https://bookdatabase-djangorest.herokuapp.com/

It is a web application which uses API. It lets the user add books, authors and publishing houses to a database and also edit and delete them.

**Django** version: 2.2.7<br/>
**Django Rest Framework** version: 3.11.0<br/>
**Python** version: 3.6.8


### Installing and Prerequisites

To run the app locally:

1. Create virtualenv and run it:

```
virtualenv venv

source venv/bin/activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Make migrations:

```
python manage.py makemigrations
```

4. Migrate:

```
python manage.py migrate
```

5. Create a superuser:

```
python manage.py createsuperuser
```

6. Finally run the server:

```
python manage.py runserver
```
