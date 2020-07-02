The openNPL platform
=====================

openNPL is a Python / Django powered platform for working with non-performing loan data.

The source code is available in the Open Risk Repository `Link <https://github.com/open-risk/openNPL.git>`_.

* Author: `Open Risk <http://www.openriskmanagement.com>`_
* License: MIT
* Code Documentation: `Read The Docs <https://opennpl.readthedocs.io/en/latest/>`_
* Data Documentation: `Open Risk Manual <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_
* Training: `Open Risk Academy <https://www.openriskacademy.com/login/index.php>`_
* Development Website: `Github <https://github.com/open-risk/openNPL>`_
* Discussion: Open Risk Gitter Channels

Functionality
-------------
The openNPL platform will typically be used by a combination of regular users, administrators and
developers

Users can use openNPL to:

* Log-in into the application with their credentials</td>
* Inspect the available data sets (tables or relations) that capture the EBA Template recommendations</td>
* Insert, Update or Delete records (e.g. new counterparty or loan data)</td>
* Consult the documentation as to the meaning and requirements of each data element</td>


**NB: openNPL is still in active development. Functionality will be significantly enhanced in future
versions. If you have specific requests / ideas please raise them in our github repository**

Architecture
------------
The following describes the current architecture

* openNPL is built on top of the Python Django framework
* The non-performing loan template recommendations of the EBA are implemented as distinct models in the database
* Additional models are introduced to bind the data together
* The user interface uses built-in Django forms as those are rendered by the Grappelli skin
* The backend database is currently sqlite

File structure
-----------------
The openNPL distribution has the following structure:

+---------+---------------+------------+---------------------------------------+
| Level 1 | Level 2       | Level 3    |  Description                          |
+=========+===============+============+=======================================+
| openNPL |               |            | The root                              |
+---------+---------------+------------+---------------------------------------+
|         | eba_portfolio |            | DIR: The core python files            |
+---------+---------------+------------+---------------------------------------+
|         |               | models.py  | Portfolio level models                |
+---------+---------------+------------+---------------------------------------+
|         |               | loan.py    | The Loan model                        |
+---------+---------------+------------+---------------------------------------+
|         |               | ...        | The other EBA models                  |
+---------+---------------+------------+---------------------------------------+
|         | start         |            | DIR: Templates for the front end      |
+---------+---------------+------------+---------------------------------------+
|         | openNPL       |            | DIR: Application configuration files  |
+---------+---------------+------------+---------------------------------------+
|         | docs          |            | DIR: This documentation               |
+---------+---------------+------------+---------------------------------------+
|         | static        |            | DIR: Styling for the front end        |
+---------+---------------+------------+---------------------------------------+

Core Data Models
----------------

- Portfolio (Segments the data into distinct portfolios)
- Portfolio_Snapshot (Segments the data into temporal snapshots / cutoff dates)
- 8 EBA Tables (Implementing the core EBA template specification)
- User (Inheriting from Django User model)

Installation options
--------------------
The installation page guides with the current installation options

Usage
-----
The usage page illustrates using screenshots the currently available functionality