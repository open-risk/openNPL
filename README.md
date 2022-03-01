[![Documentation Status](https://readthedocs.org/projects/opennpl/badge/?version=latest)](https://opennpl.readthedocs.io/en/latest/?badge=latest)

# openNPL overview
![openNPL Logo](/docs/source/opennpl-logo.png) openNPL is an open source platform for the management of loan portfolio data with a particular focus on non-performing loans. openNPL implements and builds on the detailed European Banking Authority loan templates for NPL data. It thereby enables the collection and easy management of non-performing loan data according to best-practices. 

The platform is in active development, parties interested in its further development are encouraged to get involved. The project aims to be driven by community needs. We welcome code contributions and feature requests via github.

![Landing](/docs/source/screenshots/landing.png)


## Motivation
Non-Performing loans pose a serious and ongoing challenge that affects many economies. The Covid-19 pandemic will only complicate the management of credit risk and problem loans. Developing tools and methodologies that will reduce the burden and improve the ability to manage problem loans is thus an important objective. For more background and previous work see the [blog post and links therein](https://www.openriskmanagement.com/opennpl-open-source-npl-platform-first-release/).

## Summary of Structure and Functionality

### User Oriented Functionality
openNPL is a *web server application* that works together with a tailored *data schema* and backend database to provide easy access to NPL data adhering to the regulatory recommendations. Running the application creates a web server that can then be accessed by any regular browser to enable interaction with the underlying database and data sets. 

NB: For easy installation and testing, the current (preliminary) release of openNPL uses a portable sqlite database instead of a larger production database server. In future releases the sqlite option will be retained for lightweight (demo) purposes only  

Once the openNPL platform is up and running:

* A user can log-in into the application
* Inspect the available data sets (tables or relations), apply filters etc.
* Insert, Update or Delete records

![Landing](/docs/source/screenshots/filter.png)

### Machine Oriented Functionality
openNPL aims to be at the same time easy to integrate into automated (computer driven) workflows. For this reason it exposes a *REST API* that offers both overviews and granular access to individual loan records.

![Landing](/docs/source/API.png)

*For more detailed description of structure and functionality please refer to the documentation as explained in the next section* 

**WARNING**
The current release is a development version that offers no security features. Do **not** use it with real data unless operating within a secure and controlled environment.

# Documentation
openNPL includes two broad categories of documentation:
* **Platform Documentation** pertaining to the platform itself. This includes both Technical (Code) Documentation
 and Administrator / User Documentation
* **Domain Documentation** covering the required knowledge base around *non-performing loans* and in 
particular the relevant counterparty and loan data that are important for the management of NPL portfolios

## Code and User Documentation
The technical / user documentation is included in this distribution and is hosted online at [readthedocs](http://opennpl.readthedocs.io) 

## Data Documentation
The domain knowledge and detailed data documentation is provided via the **Open Risk Manual**. The following links are good starting points:

* [EBA NPL Templates](https://www.openriskmanual.org/wiki/EBA_NPL_Template)
* [NPL Concepts](https://www.openriskmanual.org/wiki/Category:NPL)

The Open Risk Manual articles further connect the specific NPL knowledge base to more general *credit portfolio* and *risk management* concepts, procedures and overall knowledge bases.

# Installation 
There are several options to install openNPL, check out the details below

## Manual Installation from Source 
Manual installation from the repository source files requires some familiarity with python, django and web applications

### Prerequisites
- openNPL requires a working Python 3 installation (including pip)
- Python >= 3.9
- Django >= 4.0
- The precise python library dependencies are listed in the :doc:`requirements`.txt file.
- Note: The current User Interface (UI) is desktop oriented and might not work properly in smaller mobile screens
- openNPL may work with earlier versions of these packages but this has not been tested
- A linux based system is recommended. Some tweaks are required for Windows but is in principle also possible to deploy there

### Summary of Steps
Conceptually the required steps are as follows:
* Step 1. Clone the openNPL repository from github
* Step 2. Create a virtual environment
* Step 3. Install the dependencies
* Step 4. Create the database
* Step 5. Create an admin user
* Step 6. Load some dummy data
* Step 7. Have fun exploring openNPL!

In summary the required commands are as follows (more details in the documentation)
``` python
git clone https://github.com/open-risk/openNPL
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations npl_portfolio
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
bash loadfixtures.sh
python manage.py runserver
```

## Installation using Docker

* It is also possible to install openNPL using docker. This option may simplify the process for some purposes as it encapsulates all the installation procedures inside a docker container. 
  
At the Docker Hub you can get a ready to run [Docker Image of openNPL](https://hub.docker.com/repository/docker/openrisk/opennpl_web). Alternatively, you can build the Docker image locally from the Dockerfile (instructions are available in the documentation).

# openNPL Community
We welcome your feedback and support, raise a github issue if you want to report a bug or request a new feature. We are glad to help.

- [Contribute on Issues](<https://github.com/open-risk/openNPL/issues>)
- Chat with the community [Open Risk Commons](<https://www.openriskcommons.org/c/open-source/opennpl/13>)
- For customisations, support or any other collaboration, email <info@openrisk.eu>
- Need commercial support? [Contact](https://www.openriskmanagement.com/contact/)

## Credits
* Django
* Grappelli
* European Banking Authority
