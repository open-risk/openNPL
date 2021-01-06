The openNPL platform
=====================

**openNPL** is a Python / Django powered platform for working with detailed (*loan level*) data with a particular emphasis on capturing non-performing loan information.

The source code is available in the Open Risk Repository `Link <https://github.com/open-risk/openNPL.git>`_.

* Author: `Open Risk <http://www.openriskmanagement.com>`_
* License: MIT
* Code Documentation: `Read The Docs <https://opennpl.readthedocs.io/en/latest/>`_
* Domain Documentation: `Open Risk Manual Loan Data <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_
* Development Website: `Github <https://github.com/open-risk/openNPL>`_
* Docker Image: `Docker <https://hub.docker.com/repository/docker/openrisk/opennpl_web>`_
* Training: `Open Risk Academy <https://www.openriskacademy.com/login/index.php>`_
* Discussion: `Gitter <https://gitter.im/open-risk/Lobby>`_

Functionality
-------------
The openNPL platform may be used by a combination of regular financial industry users (portfolio managers, business analysts), data engineers and risk model developers.

Users can use openNPL to:
* Log-in into the application with their credentials
* Inspect the available loan data sets (tables or relations) conforming to the European Banking Authority Template recommendations<
* Insert, Update or Delete loan records (e.g. new counterparty, loan or collateral data)
* Consult the documentation as to the meaning and requirements of each data element


**NB: openNPL is still in active development. The functionality of the platform will be significantly enhanced in future versions. If you have specific requests / ideas please raise them in our github repository**

Architecture
------------
The current *architecture* is summarized:

* openNPL is built on top of the **Python Django framework**
* The non-performing loan template recommendations of the EBA are implemented as distinct models in the database
* Additional models are introduced to bind the data together with relations
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
|         | npl_portfolio |            | DIR: The core python files            |
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
|         | static        |            | DIR: Styling assets                   |
+---------+---------------+------------+---------------------------------------+
|         | templates     |            | DIR: Template customization           |
+---------+---------------+------------+---------------------------------------+


Core Data Models
----------------

- Portfolio (Segments the data into distinct portfolios)
- Portfolio_Snapshot (Segments the data into temporal snapshots / cutoff dates)
- 8 NPL Tables (Implementing the core European Banking Authority NPL template specification)
- User (Inheriting from Django User model)

Installation options
--------------------
The :doc:`/installation` page provides guidance with the current installation options

Getting Started
---------------
The :doc:`/usage` page illustrates (using screenshots) the currently available functionality to help you get started with openNPL