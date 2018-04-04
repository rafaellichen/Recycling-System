# Recycling-System CSC 47300 Web Site Design, Fall 2017
Live site: https://warm-beach-37724.herokuapp.com

Slides: https://drive.google.com/drive/folders/1Jtyh39obV1v_us9bhiLv7CBNBeXTJOAu?usp=sharing

## Running the application:
**cd into the Recycling-System**:
> $ python manage.py runserver

**Note: Install dependancies before running the commands below:**

## Running the tests:
**cd into the Recycling-System**: 
> $ coverage run --source="." manage.py test
---
## Using django-nose as a test runner:
```
 $ ./manage.py test <appname> --cover-html
 $ open cover/index.html
```
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


