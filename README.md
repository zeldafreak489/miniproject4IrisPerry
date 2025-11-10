### INF601 - Advanced Programming in Python
### Iris Perry
### Mini Project 4
 
 
# Django Habit Tracker
 
A simple web application to track daily habits, record completions, and visualize progress. Users can register, log in, and manage their personal habits.
 
## Description
 
This project is a Django-based habit tracker that allows users to create, view, and track habits. The goal of this application is to help users monitor daily routines and stay accountable to their personal goals.
 
## Getting Started
 
### Dependencies
 
* Python 3.13+
* Django 5.2.8
* SQLite (default with Django)
* Bootstrap 5
* Recommended OS: Windows

To install dependencies, run:

```bash
pip install -r requirements.txt
```
 
### Installing
 
1. Clone or download the project from GitHub.
2. Ensure the folder structure is intact:
```bash
habittracker/
├── habits/
│   ├── migrations/
│   ├── templates/habits/
│   └── admin.py
├── habit_tracker_project/
│   └── settings.py
├── manage.py
└── requirements.txt
```
3. No additional modifications are required. SQLite is used as the default database.
 
### Executing program

1. Change directory to habittracker:
```bash
cd habittracker
``` 
2. Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```
3. Create a superuser to access the admin:
```bash
python manage.py createsuperuser
```
4. Run the development server:
```bash
python manage.py runserver
```
5. Open a browser and go to: http://127.0.0.1:8000/
* Register a new user or login using the superuser account.
* Use the habit list page to add, edit, and track habits.
 
## Help
 
If you encounter common issues:
* To reset the database:
```bash
rm db.sqlite3
```
* To create another superuser:
```bash
python manage.py createsuperuser
```
 
## Authors
 
Iris Perry
 
## Version History
 
* 0.1
    * Initial Release
 
## Acknowledgments

* [Django Documentation](https://docs.djangoproject.com/en/5.2/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)