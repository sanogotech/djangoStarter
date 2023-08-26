# django Start  Python  Django 

## Vidéos Django 

* https://youtu.be/Bn0k9DDYBZM?si=IiAk8WkNn4g4UrYm
 ## Tutorial
 https://www.geeksforgeeks.org/django-tutorial/
 https://www.geeksforgeeks.org/ultimate-guide-git-github/

 https://docs.djangoproject.com/fr/3.0/intro/tutorial01/

 https://developer.mozilla.org/fr/docs/Learn/Server-side/Django/Home_page
 
 * One should be using Django for web development in the following cases:
- For developing a Web Application or API Backend
- For Rapid Development of some web application
- Deploying the application Fast and Scaling it according to your needs
- A Perfect ORM for working with database instead of database queries
- To develop a secure single page application for either retrieveing data or posting data

## Install  Django
- create folder "djangoprojects"
-  cd djangoprojects
- create  .gitignore  (with myenv folder)
- pip install virtualenv
- python -m venv  myenv
- cd myenv/Scripts/activate.bat
- return to 'djangoprojects' root
- (myenv) pip install django

## Start a project
- django-admin startproject crmproject
- cd crmproject

## Start the server
- python manage.py runserver

- http://localhost:8000/

[Home Django Project ](http://url/to/img.png)

## Pre-installed apps
Django provides some pre-installed apps for users. To see pre-installed apps, navigate to crmproject –> crmproject –> settings.py
In your settings.py file, you will find INSTALLED_APPS. Apps listed in INSTALLED_APPS are provided by Django for developers comfort.

## Create App 'contactmanager'
python manage.py startapp contactmanager


*  crmproject -> crmproject -> urls.py and add below code in the header


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   # / defaut application path : order/loading localhost:8000
   path('', include("contactmanager.urls")), 
   #  path('contactmanager/', include("contactmanager.urls")), 
   path('admin/', admin.site.urls),
]

## Create first View

* In the  contactmanager/views.py 

------------
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


------------

* Create  contactmanager/urls.py and  add :

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]


# Restart  Project/Application

python manage.py runserver

- Hello World Message from 'contactmanager'
