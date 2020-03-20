# python-playground

Learning Python playground

## Good Practices

Here are some good links I found so far:

* The Hitchhiker’s Guide to Python! https://docs.python-guide.org/

## Use pipenv for package and env management

Here is a link that describes setting it up and best practices: [Pipenv: Python Development Workflow for Humans](https://github.com/pypa/pipenv#pipenv-python-development-workflow-for-humans)


Install all dependencies for a project (including dev): ``` $ pipenv install --dev ```

To activate a virtualenv, run ``` $ pipenv shell ```

To exit from the current shell, simply press CTRL+D

Locate the project:

$ pipenv --where
/Users/kennethreitz/Library/Mobile Documents/com~apple~CloudDocs/repos/kr/pipenv/test

Locate the virtualenv:

$ pipenv --venv
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre


Locate the Python interpreter:

$ pipenv --py
/Users/kennethreitz/.local/share/virtualenvs/test-Skyy4vre/bin/python


Install packages:

$ pipenv install

Creating a virtualenv for this project......
No package provided, installing all dependencies.
Virtualenv location: /Users/kennethreitz/.local/share/virtualenvs/test-EJkjoYts
Installing dependencies from Pipfile.lock......

To activate this project's virtualenv, run the following:
```
$ pipenv shell
```
Loading .env environment variables…
Launching subshell in virtual environment. Type 'exit' or 'Ctrl+D' to return.


## Working with .env file

Install the dotenv CLI so you can modify the .env file through the command line:

```
pip install -U "python-dotenv[cli]"
```

The .env file needs to be in the project root folder. Use the [pythond-dotnev](https://pypi.org/project/python-dotenv/) package in your code to read the key/value pairs in your code.

