Installation
=======================
You can install and use the openNPL package in any system that supports python

Dependencies / Requirements
---------------------------
- openNPL requires a working Python 3 installation (including pip)
- Python >= 3.6
- Django >= 3.0
- The precise python library dependencies are listed in the requirements.txt file.
- The current User Interface (UI) is desktop oriented and will not work properly via mobile
- openNPL may work with earlier versions of these packages but this has not been tested.
- For installation via docker a working docker installation is required


Manual installation from sources
--------------------------------

A Linux based system is recommended but just minor tweaks are required for Windows and it is
in principle also possible to deploy there

Download the github sources to your preferred directory:

.. code:: bash

    git clone https://github.com/open-risk/openNPL

It is advisable to install the platform in a virtualenv so as not to interfere with your system's python distribution

.. code:: bash

    virtualenv -p python3 venv
    source venv/bin/activate

Install the dependencies (basically Django and its own dependencies and in addition Grappelli as
the admin interface)

.. code:: bash

    pip3 install -r requirements.txt

Make the required migrations. The project is setup to use sqlite. This step will ensure the database
has the right tables.

.. code:: bash

    cd INSTALLATION_DIRECTORY
    python manage.py makemigrations
    python manage.py migrate

Create a superuser. Use admin/admin as login/password as a reminder that this instance of openNPL should
NOT be used for anything remotely sensitive!

.. code:: bash

    python3 manage.py createsuperuser

Collect static files (to ensure the interface will render properly)

.. code:: bash

    python3 manage.py collectstatic --no-input

Insert some dummy data (optional)

.. code:: bash

    bash loadfixtures.sh

Run the server. The default port is 8000 but if (by any chance) this port is already used in your computer there will be
another assigned. Be sure to note that and use it instead.

.. code:: bash

    python3 manage.py runserver

Finally in your favorite browser (e.g. Firefox from Mozilla), enter the url ``http://localhost:8000``


Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~

The above steps are typical Django project installation steps. If you experience trouble at any point, the
Django online FAQ should help you out.

We welcome your feedback and support, raise a github ticket if you want to report a bug or need new feature.


Docker Installation
-------------------
Running openNPL via docker is an alternative option that simplifies the manual process (but a working docker installation is required!)

docker pull docker pull openrisk/opennpl:0.1