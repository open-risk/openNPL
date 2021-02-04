ChangeLog
===========================
PLEASE NOTE THIS IS ONLY A PLANNING RELEASE.
THE OPENNPL API IS STILL UNSTABLE

v0.3.1 (04-02-2021)
-------------------
* Expanded implemented fields / streamlined FK structure
* Split model choice attributes into separate files for improved readability / maintenance
* Removed User field from portfolio models (to simplify demo instance setup)
* Expanded module documentation (sphinx autodoc for all models)


v0.3 (06-01-2021)
-----------------
* Refactored globally eba -> npl
* Dockerfile adjusted to remove pre-existing sqlite at setup
* Dockerfile adjusted to load given fixtures file at end of installation
* Documentation update

v0.2 (26-09-2020)
-----------------
* New Feature: Exposes a REST API for all the implemented npl models
* Change: Reference data (choice elements) in the templates have been converted to textfields

v0.1.1 (12-07-2020)
-------------------
* First Dockerized Version

v0.1 (02-07-2020)
-------------------
* Initial Release of openNPL