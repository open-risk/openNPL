.. openNPL code documentation

EBA NPL Data Models
==============================

The pages in this section document in detail the EBA NPL data models. openNPL implements the core relations (Tables) of the EBA Portfolio Template `EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

Each data model is implemented in a separate file TABLE_NAME.py in the npl_portfolio directory. In addition there is a **Portfolio Model** and a **Portfolio Snapshot Model** implemented in the (models.py) file. These models extend the EBA recommendation to enable and/or improve the usability of the openNPL platform.

.. TODO:: Missing are the following: the **Lease Table** and the **Schedule** tables (Swap cashflows and Historical Repayments)

.. NOTE:: The Relation Tables of the EBA Specification are not implemented as they are redundant in the openNPL database design

.. toctree::
   :maxdepth: 4

   NPL_Portfolio
   NPL_CounterpartyGroup
   NPL_Counterparty
   NPL_Loan
   NPL_PropertyCollateral
   NPL_NonPropertyCollateral
   NPL_ExternalCollection
   NPL_Forbearance
   NPL_Enforcement