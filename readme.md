# Chillax Movies App

## Description

This is a simple Movie application that utilizes stuff.
Please have internet to load CSS and Javascript frameworks!

## Installation

**Installation via requirements.txt**

```shell
$ cd chillax
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *chillax* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 


## Configuration

The *chillax/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.


## Testing 

IMPORTANT UPDATE: Tests do not work when running via 'pytest' command. Please right click on each of the test files in order to run tests. Thanks.

PLEASE NOTE: Please test individual testing files in the "tests/integration" and "tests/unit" folders by right clicking and running tests manually.

BELOW MAY WORK
--------------
Testing requires that file *chillax/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *chillax/tests/data* directory. 

E.g. `TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'ian', 'Documents', 'Python dev', 'COVID-19', 'tests', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):


You can then run tests from within PyCharm.

 
