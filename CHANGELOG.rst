ChangeLog
===========================
PLEASE NOTE THIS IS ONLY A PLANNING RELEASE.
THE OPENNPL API IS STILL UNSTABLE

v0.5 (01-03-2022)
------------------
* Upgrade to Python 3.9 and Django 4.0

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