NPL Portfolio App
==========================================
NPL Portfolio is a Django app to store NPL Portfolio Data

Quick start
---------------------
1. Add "portfolio" to your INSTALLED_APPS setting like this::

INSTALLED_APPS = [
...
'npl_portfolio',
]

2. Run ``python manage.py migrate`` to create the npl_portfolio models.

3. Start the development server and visit http://127.0.0.1:8000/admin/
