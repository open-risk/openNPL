Loading Sample Data
==============================
A new openNPL instance will have no data. To get a feel for the platform it is advisable to load some of the datasets included in the distribution.


Here is how to do this for a docker based / local installation:


Loading Data into local instance
---------------------------------
Inside your virtualenv issue

.. code:: bash

    bash loadfixtures.sh


.. note:: You can select any of the json files available within the fixtures directory, just edit the shell script.


Loading Data into a Docker instance
------------------------------------
In a docker based installation simply execute the above inside your container:

.. code:: bash

    docker exec -it 106bdb7e103f python3 manage.py loaddata --format=json ./npl_portfolio/fixtures/npl_portfolio.json