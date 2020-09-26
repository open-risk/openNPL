Getting Started
==============================
The openNPL platform offers a lot of functionality. Here we break down some of the main workflows for
those just getting started. More will follow as the platform develops!

* An online available demo will be available soon for those who don't want to go through the local installation step
* For more in depth studies on using python for credit portfolio management check-out: `Open Risk Academy <https://www.openriskacademy.com/login/index.php>`_
* For Non-performing loan domain knowledge check out: `Open Risk Manual <https://www.openriskmanual.org/wiki/Category:NPL>`_


The landing page
---------------------

If everything went well with the installation, upon pointing your browser to localhost:8000 (or whatever port you
are using) you will meet the landing page

.. image:: ./screenshots/landing.png

Login
-----
To login in, point your browser to localhost:8000/admin (currently only the admin user is enabled)

This will get you to the login page.

.. image:: ./screenshots/login.png

If you used the default credentials for openNPL you login using

-   **Login:** admin
-   **Password:** admin

Admin Interface
---------------
After successful login you will get to the admin interface which offers access to all the datasets

.. image:: ./screenshots/admin.png

The interface provides access to
* administrative functions like creating users and groups
* a history log of activities that have been performed
* user functions like inspecting and working with NPL data

Lets click first on an important data model under the EBA portfolio collection: Counterparties. This gets us
to a list of (randomly generated) counterparties that have been inserted into the database during the
installation process

Counterparty Data
-----------------

.. image:: ./screenshots/counterparty.png

Some key functionalities available in this view are (in summary)
* viewing (sorting) counterparty data (meaning obligor or borrower data, e.g. company or individual person data)
* NB: the view selects only some illustrative fields out of the many recorded in the database
* adding new records
* deleting new records

Lets click into any counterparty row to take a closer look:

.. image:: ./screenshots/counterparty_detail.png

All the available EBA counterparty fields are available in this view to inspect and potentially change. If
any field is unclear, clicking on the Documentation link underneath takes you to the Open Risk Manual for
the explanation. For example if we click on Annual Revenue we will get to the corresponding page that
explains the meaning and requirements for this data point

.. image:: ./screenshots/manual.png

We can go back to the overview of all data by clicking on the breadcrumb (EBA Portfolio) or pointing the
browser to http://localhost:8001/admin/eba_portfolio/

Lets take a look now at another important data model, namely the loan data. Loans is one of the main
financial products documented in the templates (others being leases and swaps)

Loan Data
----------

.. image:: ./screenshots/loan.png

The layout is similar to what we have seen before. A selection of fields is visible in the overview and
clicking through we get access to further data, e.g. which counterparty actually holds to the loan.

In the upper right corner we have the functionality for filtering the dataset. Clicking on the menu allows
selecting the desired filter to narrow down the portfolio

.. image:: ./screenshots/filter.png

As one final example lets go back to the main list and select the Property Collateral data (in the EBA
templates collateral is segmented along property and non-property classes)

Property Collateral Data
------------------------

The, by now familiar, table display of the stored collateral data should show up:

.. image:: ./screenshots/collateral.png

Lets try now something more adventurous. Lets try to add some data! (Click on the add data button on
the upper right side of the page). You should see a form with many empty fields:

.. image:: ./screenshots/adding.png

Depending on the nature of the field you can either enter text, numbers or select entries from drop-down
menus. Whenever there is doubt, the documentation link is as before one click away!