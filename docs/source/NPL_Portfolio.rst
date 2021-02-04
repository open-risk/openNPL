Portfolio Data Models
============================

openNPL models implement the core relations (Tables) of the EBA Portfolio Template
`EBA Templates <https://www.openriskmanual.org/wiki/EBA_NPL_Template>`_

Each model is implemented in a separate file TABLE_NAME.py in the npl_portfolio directory. In addition there is a Portfolio model and a Portfolio_Snapshot model in this (models.py) file.

.. TODO:: Missing are the following: the Lease Table and the Schedule tables (Swap cashflows and Historical Repayments)

.. NOTE:: The Relation Tables of the EBA Specification are not implemented



.. automodule:: npl_portfolio.models
   :members:
   :undoc-members:
   :noindex:

   .. automethod:: npl_portfolio.models.Portfolio

   .. automethod:: npl_portfolio.models.PortfolioSnapshot