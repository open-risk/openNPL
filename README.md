# openNPL overview
openNPL is an open source platform for the management of non-performing loans. 
It implements detailed European Banking Authority loan templates for NPL data enabling
the collection and easy management of loan data according to best-practices 

![Landing](/docs/source/screenshots/landing.png)

The project aims to be driven by community needs. We welcome code contributions and feature 
requests via github.

## Motivation
Non-Performing loans is a serious and ongoing issue that affects many economies. Developing
tools and methodologies that will reduce the burden and improve the ability to manage problem
loans is thus an important objective. For more background and previous work 
see the [blog post and links therein](https://www.openriskmanagement.com/opennpl-open-source-npl-platform-first-release/).

## Structure and Functionality Summary
openNPL is a *web application* that works together with a tailored data schema to provide easy access
to NPL data adhering to the regulatory recommendation. Running the application creates a *server* that
can then be accessed via any regular browser. For easy installation and testing the current release uses
an sqlite database instead of a production database.  Once the platform is up and running:

* A user can log-in into the application
* Inspect the available data sets (tables or relations), apply filters etc.
* Insert, Update or Delete records

![Landing](/docs/source/screenshots/filter.png)

*For more detailed description of structure and functionality please refer to the documentation as
explained in the next section* 

**WARNING**
The current release is a development version that offers no security features. Do **not** use it with real
data unless in a secure environment.

# Documentation
openNPL includes two broad categories of documentation:
* **Platform Documentation** pertaining to the platform itself. This includes both Technical (Code) Documentation
 and Administrator / User Documentation
* **Domain Documentation** covering the required knowledge base around *non-performing loans* and in 
particular the relevant counterparty and loan data that are important for the management of NPL portfolios

## Code and User Documentation
The technical / user documentation is included in this distribution and is hosted online at
[readthedocs](http://opennpl.readthedocs.io) 

## Data Documentation
The domain knowledge and detailed data documentation is provided via the Open Risk Manual. The following
are good starting points:

* [EBA NPL Templates](https://www.openriskmanual.org/wiki/EBA_NPL_Template)
* [NPL Concepts](https://www.openriskmanual.org/wiki/Category:NPL)

The Open Risk Manual articles further connect the specific NPL knowledge base to the more general 
*credit portfolio* and *risk management* knowledge base

# Installation 
There are several options, check out the details below

## Manual Installation from Source 
Manual installation requires some familiarity with python, django and web applications

### Prerequisites
* a working python installation (3.6 or higher)
* a linux based system is recommended. some tweaks are required for Windows but is in principle also possible to deploy there

### Steps
* Step 1. Clone the openNPL repository from github
* Step 2. Create a virtual environment
* Step 3. Install the dependencies
* Step 4. Create the database
* Step 5. Create an admin user
* Step 6. Load some dummy data
* Step 7. Have fun exploring openNPL!

In summary (more details in the documentation)
``` python
git clone https://github.com/open-risk/openNPL
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
bash loadfixtures.sh
python manage.py runserver
```

## Installation using Docker

* coming soon in a docker near you

# Trying out openNPL online

A demo (will be) available [here](https://www.opennpl.com/). Demo credentials for openNPL:
- **Login:** admin
- **Password:** admin

# openNPL Community
We welcome your feedback and support, raise a github issue if you want to report a bug or request new 
feature. We are glad to help.

- [Contribute on Issues](<https://github.com/open-riks/openNPL/issues>)
- Follow [Open Risk](<https://twitter.com/openriskmanagement>) on Linkedin
- Chat with community [Gitter](<https://gitter.im/open-risk/Lobby>)
- For customisations, support or other collaboration, email <info@openrisk.eu>
- Need additional commercial support? [Contact](https://www.openriskmanagement.com/contact/)

## Credits

* Django
* Grappelli
* European Banking Authority