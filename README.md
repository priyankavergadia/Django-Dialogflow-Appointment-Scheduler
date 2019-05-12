# Django Dialogflow Appointment Scheduler 

Django [Dialogflow](https://dialogflow.com) is a web client to chat with Dialogflow agent Appointment Scheduler.


## Table of contents

1. [URLs](#URLs)
2. [Sync your database](#sync-your-database)
3. [Production your BOT](#production-your-bot)
4. [Installation](#installation)
5. [Configuring Webservice](#configuring-webservice)
6. [Deploying on Heroku](#deploying-on-heroku)
7. [Examples](#examples)
8. [Motivation](#motivation)
9. [License](#license)
10. [Contributing](#contributing)

## URLs

You will need to add below steps to your [urls.py](./django_dialogflow/urls.py)

``` Python
urlpatterns = [
    path('chat/', include('chat.urls')),
    path('admin/', admin.site.urls),
]

```

The endpoint expects a JSON request with the following data:

``` Python
{"text": "My input statement"}
```

See detailed example how retrieve end point translated information [app.html](.django_dialogflow/django_dialogflow/templates/app.html)


## Sync your database

In order to persists your data you need to create the necessary ``django_dialogflow`` tables. 

For generating schema migrations, you have to run these steps.

``` Bash
$ python manage.py migrate django_dialogflow
```

## Production your Bot

### Configuring Dialogflow

To comunicate with Dialogflow you need get a [client access token](https://dialogflow.com/docs/reference/agent/#using_access_tokens), 

Then go to [settings.py](./django_dialogflow/settings.py) update your ``client_access_token`` in ``settings.py``

``` Python
# Dialogflow settings
DIALOGFLOW = {
    'client_access_token': 'e5dc21cab6df451c866bf5efacb40178',
}
```

### ALLOWD_HOSTS

Modify Django Allowed hosts to access your application everywhere, to do this modify [settings.py](./django_dialogflow/settings.py) as suggested below

``` Python
ALLOWED_HOSTS = ['A.B.C.D', 'localhost']
```

### CORS_ORIGIN_WHITELIST

Cross-origin resource sharing (CORS) is a mechanism that allows restricted resources (e.g. fonts) on a web page to be requested from another domain outside the domain from which the first resource was served.

To do this modify [settings.py](./django_dialogflow/settings.py) as suggested below

``` Python
CORS_ORIGIN_WHITELIST = (
    'A.B.C.D:9000',
)
```

### Deploy

``` Bash
python manage.py runserver 0.0.0.0:8000
```

Further documentation on Dialogflow can be found here https://dialogflow.com/

## Installation

If you are trying use ``django_dialogflow`` as app,

Then you could install ``django-dialogflow`` either via the Python Package Index (PyPI) or from GitHub source.

To install using pip :

``` Bash
$ pip install django-dialogflow
```

and then add it to your installed apps in your settings.py:

``` Bash
INSTALLED_APPS = (
    ...
    'django_dialogflow',
    ...
)
```


## Configuring Webservice

If you want to host your Django app, then you need to choose a method through which it will be hosted. There are a few free services that you can use to do this such as [Heroku](https://dashboard.heroku.com/) and [PythonAnyWhere](https://www.pythonanywhere.com/details/django_hosting).

Some basic Heroku deployment instrction are found below.

### WSGI

A common method for serving Python web applications involves using a Web Server Gateway Interface (WSGI) package.

Gunicorn is a great choice for a WSGI server. They have detailed documentation and installation instructions on their website.

### Hosting static files

There are numerous ways to host static files for your Django application. One extreemly easy way to do this is by using WhiteNoise, a python package designed to make it possible to serve static files from just about any web application.

## Deploying on Heroku

Here are some of the steps to lauch your Django app with Heroku

### Build your app and run it locally

``` bash
pip install -r requirements.txt
Downloading/unpacking ...
...
Successfully installed Django dj-database-url dj-static django-toolbelt gunicorn psycopg2 static3
Cleaning up...
```

### To run your application locally,

``` bash
heroku local web
11:48:19 web.1  | started with pid 36084
11:48:19 web.1  | 2014-07-17 11:48:19 [36084] [INFO] Starting gunicorn 19.0.0
11:48:19 web.1  | 2014-07-17 11:48:19 [36084] [INFO] Listening at: http://0.0.0.0:5000 (36084)
11:48:19 web.1  | 2014-07-17 11:48:19 [36084] [INFO] Using worker: sync
11:48:19 web.1  | 2014-07-17 11:48:19 [36087] [INFO] Booting worker with pid: 36087
```
Your app should now be avaliable and running on http://localhost:5000/.

### Deploy your application on Heroku

``` Bash
git add .

git commit -m "Added a Procfile."

heroku login
Enter your Heroku credentials.
...

heroku create
Creating intense-falls-9163... done, stack is cedar
http://intense-falls-9163.herokuapp.com/ | git@heroku.com:intense-falls-9163.git
Git remote heroku added

git push heroku master
...
-----> Python app detected
...
-----> Launching... done, v7
       https://intense-falls-9163.herokuapp.com/ deployed to Heroku
```

Much more detailed information can be found here https://devcenter.heroku.com/articles/deploying-python

## Using the development version

You can clone the git repository by doing the following:

``` Bash
$ git clone git://github.com/vkosuri/django-dialogflow.git
```

## Examples

All [examples](./examples) are located here Github repo

## Motivation

https://github.com/gunthercox/django_chatterbot

## LICENSE
Licensed under [MIT](./LICENSE.md)

## Contributing

Development of django_dialogflow happens at Github: http://github.com/vkosuri/django-dialogflow

You are highly encouraged to participate in the development. If you don't like Github (for some reason) you're welcome to send regular patches.