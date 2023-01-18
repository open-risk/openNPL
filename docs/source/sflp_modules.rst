.. openNPL code documentation

FM SFPL Data Models
==============================

The next pages document in detail the Agency SFLP data models. openNPL implements the main table `SFLP Template <https://www.openriskmanual.org/wiki/FM_SFLP_Template>`_

To align with the EBA NPL classes, data are split in separate files TABLE_NAME.py in the sflp_portfolio directory. In addition there is a **Portfolio Model** and a **Portfolio Snapshot Model** implemented in the (models.py) file. These models extend the Agency approach to enable and/or improve the usability of the openNPL platform.

.. TODO:: The SFLP data hierarchy is still under development


.. toctree::
   :maxdepth: 4

   SFLP_Portfolio
   SFLP_Counterparty
   SFLP_Loan
   SFLP_PropertyCollateral
   SFLP_Forbearance
   SFLP_Enforcement