SFPL Portfolio App
==========================================
SFPL Portfolio is a Django app to store Single Family Portfolio Data

Quick start
---------------------
1. Add "portfolio" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'sfpl_portfolio',
]

2. Run ``python manage.py migrate`` to create the sfpl_portfolio models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
