## Description
A basic REST API provider.
Uses Flask and Flask-API.

![Build status](https://api.travis-ci.org/bbenzikry/flask-azure-scaffold.svg?branch=master)

In order for the application to run, you must set the following environment variables:

* ENVIRONMENT - PRODUCTION/TEST/DEVELOPMENT



## Development bootstrapping
```bash
git clone https://github.com/bbenzikry/flask-azure-scaffold
cd flask-azure-scaffold
vagrant up
```


## Notes
* When running within an Azure web app context,  
set the WSGI_LOG environment variable to a log file path to help with debugging.


* Use Kudu to browse the directory structure.
