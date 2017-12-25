# Recycling-System
https://warm-beach-37724.herokuapp.com

## Running the application:
**cd into the Recycling-System**:
> $ python manage.py runserver

**Note: Install dependancies before running the commands below:**

## Running the tests:
**cd into the Recycling-System**: 
> $ coverage run --source="." manage.py test
---
## Using django-nose as a test runner:
> $ ./manage.py test _\<appname\>_ --cover-html

**open conver/index.html**:
---
## View the test report:
**cd into the Recycling-System**:
> $ coverage run --source="." manage.py test

> $ coverage report

## Check the PyLint score:
**cd into the Recycling-System**:
> $ pylint --generated-members=objects <appname> <appname> <appname>

## Generate Documentation:
**cd into the Recycling-System/Documentation**:
> $ make html


