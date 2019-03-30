### My First Python Webpage created with DJango

![alt text](https://i.imgur.com/3FbbJ8V.jpg)


#### First Time Codes:

```
Run Powershell as administrator first time
>>> cd C:\
>>> Set-ExecutionPolicy Unrestricted
>>> Y
>>> mkdir code
>>> pip install virtualenv
>>> virtualenv .
>>> ./Scripts/activate
>>> pip install django
>>> pip freeze
>>> mkdir djangoproject
>>> django-admin.py startproject projectname
```


#### To run the localhost:

```
>>> cd C:\code\djangoproject\
>>> ./Scripts/activate
>>> python manage.py runserver
>>> python manage.py migrate   //to remove migrate database errors on console
```

#### Create user for db

```
python manage.py createsuperuser
```
