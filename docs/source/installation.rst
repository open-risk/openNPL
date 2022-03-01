Installation
=======================
You can install and use the openNPL package in any system that supports *python* **or** *docker*


Installation via Docker
-----------------------
Installation via docker is recommended as it provides a streamlined and fast setup of an openNPL instance. If you do not want to use docker scroll further down for :ref:`Manual installation from sources`

Install Docker
~~~~~~~~~~~~~~

.. note:: A working docker installation is required! Docker is available for many operating systems and platforms (Windows, MacOS, Linux, running on Intel/AMD or ARM chipsets among others). Follow the installation instructions `here <https://docs.docker.com/engine/install/>`_.

Once the installation is complete, make sure the docker service is running by testing that you can run the docker *'hello-world'* application.

.. code:: bash

    sudo service docker start
    sudo docker run hello-world

Now we are ready for the next step. You can either pull an image from Docker Hub or build a local image:

Pull the openNPL image from Docker Hub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can pull and run the latest image from Docker Hub (This method is recommended if you do not want to mess at all with the source distribution).

.. note:: We are also providing images also for the ARM/v7 architecture (Raspberry Pi). Check the root of our docker hub for what is `currently available <https://hub.docker.com/u/openrisk>`_

Start by issuing a docker pull command:

.. code:: bash

    docker pull openrisk/opennpl_web:latest
    docker run -p 8001:8080 openrisk/opennpl_web:latest

If all went well you have now a running instance of openNPL in your local machine. Access it by pointing your browser to ``http://localhost:8001`` and login with admin/admin credentials.

The API endpoints are accessible at ``http://localhost:8001/api``

.. note:: If you want to work with a different image check what is available at our `docker hub list <https://hub.docker.com/repository/docker/openrisk/opennpl_web>`_

Building a local docker image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Alternatively you can build your own *local* docker image. After you fetch the distribution from the `github repository <https://github.com/open-risk/openNPL>`_ (as per manual installation instructions below), in the root directory of the distribution issue:

.. code:: bash

    cd openNPL
    docker build -t opennpl_web:latest .
    docker run -p 8001:8080 opennpl_web:latest

Again, access the running instance of openNPL by pointing your browser to ``http://localhost:8001`` and login with the default admin/admin credentials


Manual installation from sources
--------------------------------
The manual installation path is recommended if you want to dig into and inspect the openNPL code base or if you want to contribute to openNPL.

Dependencies / Requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: A Linux based system is recommended but with minor tweaks it is in principle also possible to deploy in Windows systems

- openNPL requires a working Python 3 installation (including pip)
- Python >= 3.9
- Django >= 4.0
- The precise python library dependencies are listed in the :doc:`requirements`.txt file.
- openNPL may work with earlier versions of these packages but this has not been tested
- A linux based system is recommended. Some tweaks are required for Windows but is in principle also possible to deploy there

.. note:: The current User Interface (UI) of openNPL is desktop oriented and might not work properly in smaller (mobile) screens

Manual installation procedure
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Step 1. Download the github sources to your preferred directory:

.. code:: bash

    git clone https://github.com/open-risk/openNPL

Step 2. Create a virtualenv. It is advisable to install the platform in a virtualenv so as not to interfere with your system's python distribution

.. code:: bash

    virtualenv -p python3 venv
    source venv/bin/activate

Step 3. Install the required dependencies (The core dependency is Django and its own dependencies, in addition the Grappelli skin as the admin interface)

.. code:: bash

    pip3 install -r requirements.txt

Step 4. Make the required django migrations. The project is setup to use sqlite3. This step will ensure the database has the right tables.

.. code:: bash

    cd openNPL
    python manage.py makemigrations
    python manage.py migrate

Step 5. Create a superuser. Suggestion: Use admin/admin as login/password as a reminder that this instance of openNPL should NOT be used for anything remotely sensitive!

.. code:: bash

    python3 manage.py createsuperuser

Step 6. Collect static files (to ensure the interface will render properly)

.. code:: bash

    python3 manage.py collectstatic --no-input

Step 7. Insert some dummy data (optional). Without this the database will be empty.

.. code:: bash

    bash loadfixtures.sh

Step 8. Run the server. The default port is 8000 but if (by any chance) this port is already used in your computer there will be another assigned. Be sure to note the assigned port and use it instead.

.. code:: bash

    python3 manage.py runserver

Step 9. Login with your browser. Finally in your favorite browser (e.g. Firefox from Mozilla), enter the url ``http://localhost:8001`` and login with admin/admin credentials.

.. note:: 8000 is the default port, if that is already in use, you can select an alternative one as follows:


.. code:: bash

    python3 manage.py runserver localhost:8081


Troubleshooting
~~~~~~~~~~~~~~~~~~~~~~

The above steps are typical Django project installation steps. If you experience trouble at any point, the `Django online FAQ <https://docs.djangoproject.com/en/3.1/faq/>`_ should help you out.

.. Note:: The project uses an sqlite3 database for good reason! If things go pear-shaped with your database simply remove the file and start again.


We welcome your feedback and support. Please raise a `github ticket <https://github.com/open-risk/openNPL/issues>`_ if you want to report a bug or need a new feature. For contributions check our Contribution and Code of Conduct docs.