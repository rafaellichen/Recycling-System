Installation
============

Live Site URL:
--------------

https://warm-beach-37724.herokuapp.com

Running the application:
------------------------

cd into the Recycling-System:

.. code-block:: console

	$ python manage.py runserver

.. note:: 
	Install dependancies before running the commands below:
	.. code-block:: console	
		$ pip install -r requirements.txt


Running the tests:
------------------

cd into the Recycling-System:

.. code-block:: console

	$ coverage run --source="." manage.py test

View the test report:
---------------------

cd into the Recycling-System:

.. code-block:: console

	$ coverage run --source="." manage.py test
	$ coverage report

Check the PyLint score:
-----------------------

cd into the Recycling-System:

.. code-block:: console

	$ pylint --generated-members=objects <appname> <appname> <appname>

Generate Documentation:
-----------------------

cd into the Recycling-System/Documentation:

.. code-block:: console

	$ make html
