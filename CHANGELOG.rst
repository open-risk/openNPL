ChangeLog
===========================
PLEASE NOTE THIS IS ONLY A BETA RELEASE. THE OPENNPL API IS STILL UNSTABLE



v0.6.4 (20-06-2024)
-------------------
* Bugs: REST API for both NPL and SFLP templates

v0.6.3 (17-05-2024)
-------------------
* Functionality: Update to 2023 SFLP Template

v0.6.2 (21-09-2023)
-------------------
* Dependencies: Upgrade to Python 3.10

v0.6.1 (03-04-2023)
-------------------
* Functionality: Complete SFLP Template Loading

v0.6.0 (13-03-2023)
-------------------
* Functionality: Almost complete Single Family Loan Performance Templates (SFLP) (except forbearance, enforcement and repayment strings)
* Documentation: SFLP Data Models

v0.5.3 (18-01-2023)
-------------------
* Functionality: Importing Single Family Loan Performance Data (Testing Load Robustness / Performance)

v0.5.2 (05-12-2022)
-------------------
* Functionality: Integrate Agency Single Family Loan Performance Template (Core Design)

v0.5.1 (29-06-2022)
-------------------
* User Interface: Switch to Jazzmin UI

v0.5 (01-03-2022)
------------------
* Dependencies: Upgrade to Python 3.9 and Django 4.0

v0.4 (07-06-2021)
-------------------
* Functionality: Completed POST verbs for all current REST endpoints
* Documentation: Added Swagger/Redoc API documentation endpoints
* Bugs: Remove deprecated NullBooleanField

v0.3.2 (15-02-2021)
-------------------
* Functionality: Added some missing Fields in the counterparty and collateral models
* Deployment: Docker ARM v7 image (for Raspberry Pi)
* Documentation: Docker data initialization documentation (docker deployment does not automatically load the dummy data)
* Bugs: `Fix Issue #1 <https://github.com/open-risk/openNPL/issues/1>`_

v0.3.1 (04-02-2021)
-------------------
* Functionality: Expanded implemented fields / streamlined FK structure
* Structure: Split model choice attributes into separate files for improved readability / maintenance
* Structure: Removed User field from portfolio models (to simplify demo instance setup)
* Documentation: Expanded module documentation (sphinx autodoc for all models)


v0.3 (06-01-2021)
-----------------
* Structure: Refactored globally eba -> npl
* Deployment: Dockerfile adjusted to remove pre-existing sqlite at setup
* Deployment:Dockerfile adjusted to load given fixtures file at end of installation
* Documentation: update

v0.2 (26-09-2020)
-----------------
* Functionality:  Exposes a REST API for all the implemented npl models
* Structure: Reference data (choice elements) in the templates have been converted to textfields

v0.1.1 (12-07-2020)
-------------------
* Deployment: First Dockerized Version

v0.1 (02-07-2020)
-------------------
* Initial Release of openNPL