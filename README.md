# TrueNorth & Carlos Backend

This repository is home to the TrueNorth & Carlos backend and it's assuming
will be run under MacOS environments.

## Getting Started

### Install Homebrew
Run the script at https://brew.sh to install Homebrew.

### Set up Python development environment

    brew up && brew doctor
    brew install python@3.11 pipenv
    brew link python@3.11

Next, *in a new terminal*, run:

    python -V

Ensure that the version that is printed is in fact Python 3.11.
If it's not, you may need to update your path to prefer Python 3:

    echo 'export PATH=/usr/local/opt/python/libexec/bin:$PATH' >> ~/.zshrc

Finally, finish setup with:

    cd /path/to/loan-backend
    pipenv install --dev

### Set up database
For practical purposes, this project is bundled to a sqlite lightweight database already
configured in the `settings.py` file.
    

### Run development servers
You'll need to start a server to host the backend that serves the API.

    python manage.py runserver

### Admin site
To have better and easier control, an admin site is bundled and can be accessed
by going to (assuming you are running default Django port locally):

```http://localhost:8000/admin```

and log in using ```admin``` & ```truenorth``` for username and password, respectively.