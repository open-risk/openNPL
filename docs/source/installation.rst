Installation
=======================
You can install and use the openNPL package in any system that supports *python* or *docker*


Installation via Docker
-----------------------
Installation via docker is recommended if you want streamlined and fast setup of an openNPL instance. Scroll further down for :ref:`Manual installation from sources`

Install Docker
~~~~~~~~~~~~~~
A working docker installation is required first! Docker is available for many platforms, follow the installation instructions `here <https://docs.docker.com/engine/install/>`_.

Once the installation is complete, make sure the docker service is running and you can run the hello-world application.

.. code:: bash

    sudo service docker start
    sudo docker run hello-world

Now we are ready for the next step. You can either pull an image from Docker Hub or build a local image:

Pull the openNPL image from Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pull and run the latest image from Docker Hub (This method is recommended if you do not want to mess at all with the source distribution). Start by issuing a docker pull command.

.. note:: If you want to work with a different image check what is available at our `docker hub list <https://hub.docker.com/repository/docker/openrisk/opennpl_web>`_

.. code:: bash

    docker pull openrisk/opennpl_web:0.1.2
    docker run -p 8001:8080 openrisk/opennpl_web:0.1.2

Access the running instance of openNPL by pointing your browser to ``http://localhost:8001`` and login with admin/admin credentials. The API endpoints are accessible at ``http://localhost:8001/api``

Building a local docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alternatively you can build your own *local* docker image. After you fetch the distribution from the github repository (as per manual installation instructions below), in the root directory of the distribution issue:

.. code:: bash

    docker build -t opennpl_web:latest .
    docker run -p 8001:8080 opennpl_web:latest

Again, access the running instance of openNPL by pointing your browser to ``http://localhost:8001`` and login with the default admin/admin credentials


Manual installation from sources
--------------------------------
This path is recommended if you want to dig into and inspect the openNPL code base.

Dependencies / Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: A Linux based system is recommended but with minor tweaks it is in principle also possible to deploy in Windows systems

- openNPL requires a working Python 3 installation (including pip)
- Python >= 3.6
- Django >= 3.0
- The precise python library dependencies are listed in the :doc:`requirements`.txt file.
- Note: The current User Interface (UI) is desktop oriented and might not work properly in smaller mobile screens
- openNPL may work with earlier versions of these packages but this has not been tested
- A linux based system is recommended. Some tweaks are required for Windows but is in principle also possible to deploy there


Procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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

Finally in your favorite browser (e.g. Firefox from Mozilla), enter the url ``http://localhost:8001`` and login with admin/admin credentials.

Note: 8000 is the default port, if that is already in use, you can select an available one:

.. code:: bash

    python3 manage.py runserver localhost:8081


Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~

The above steps are typical Django project installation steps. If you experience trouble at any point, the
`Django online FAQ <https://docs.djangoproject.com/en/3.1/faq/>`_ should help you out.

We welcome your feedback and support, raise a `github ticket <https://github.com/open-risk/openNPL/issues>`_ if you want to report a bug or need a new feature.