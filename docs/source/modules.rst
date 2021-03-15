.. openNPL code documentation

openNPL Data Models
==============================

The next pages document in detail the openNPL data models. openNPL models implement the core relations (Tables) of the EBA Portfolio Template `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

Each data model is implemented in a separate file TABLE_NAME.py in the npl_portfolio directory. In addition there is a **Portfolio Model** and a **Portfolio Snapshot Model** implemented in the (models.py) file. These models extend the EBA recommendation to enable and/or improve the usability of the openNPL platform.

.. TODO:: Missing are the following: the **Lease Table** and the **Schedule** tables (Swap cashflows and Historical Repayments)

.. NOTE:: The Relation Tables of the EBA Specification are not implemented as they are redundant in the openNPL database design

.. toctree::
   :maxdepth: 4

   NPL_Portfolio
   CounterpartyGroup
   Counterparty
   Loan
   PropertyCollateral
   NonPropertyCollateral
   ExternalCollection
   Forbearance
   Enforcement
