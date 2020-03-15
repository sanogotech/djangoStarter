# django Start  Python  Django 

 ## Tutorial
 https://www.geeksforgeeks.org/django-tutorial/
 https://www.geeksforgeeks.org/ultimate-guide-git-github/
 
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

## Pre-installed apps
Django provides some pre-installed apps for users. To see pre-installed apps, navigate to djangoprojects –> djangoprojects –> settings.py
In your settings.py file, you will find INSTALLED_APPS. Apps listed in INSTALLED_APPS are provided by Django for developers comfort.

## Create App 'contactmanager'
python manage.py startapp contactmanager

* To consider the app in your project you need to specify your project name in INSTALLED_APPS list as follows in settings.py:

-  Application definition 
INSTALLED_APPS = [ 
	'django.contrib.admin', 
	'django.contrib.auth', 
	'django.contrib.contenttypes', 
	'django.contrib.sessions', 
	'django.contrib.messages', 
	'django.contrib.staticfiles', 
	'contactmanager'
] 


