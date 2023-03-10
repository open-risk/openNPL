.. openNPL code documentation

==============================
FM SFPL Data Models
==============================

The pages in this hierarchy document in detail the US Agency Single Family Loan Performance data models. openNPL implements the main table as shown here: `SFLP Template <https://www.openriskmanual.org/wiki/FM_SFLP_Template>`_

Aligned with the approach for the EBA NPL classes, data models are split in separate files following the TABLE_NAME.py convention in the sflp_portfolio directory.

.. note:: The Agency Single Family Loan Performance Template does not explicitly segment data attributes into Counterparty, Loan etc. The assignment into tables (models) in openNPL is based on the interpretation and main function of different data fields

In addition, there is a **Portfolio Model** and a **Portfolio Snapshot Model** implemented in the (models.py) file. These models extend the Agency schema to enable and/or improve the usability of the openNPL platform.

.. TODO:: The SFLP credit data hierarchy is still under development

.. toctree::
   :maxdepth: 1

   SFLP_Portfolio
   SFLP_PortfolioSnapshot
   SFLP_Counterparty
   SFLP_CounterpartyState
   SFLP_Loan
   SFLP_LoanState
   SFLP_PropertyCollateral
   SFLP_PropertyCollateralState
   SFLP_Forbearance
   SFLP_Enforcement