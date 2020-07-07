
___
## Setting up django
### 1 - Clone this repository
### 2 - CD to 01_django_base directory - run `pipenv install django==2.0.0` and `pipenv shell` - then run `python manage.py runserver` - you should have a simple django 'hello world' app running

___
## Installing Zappa and deploying dev
### 1 - run `pip install zappa` and `zappa init`
### You will be asked for some basic details and which AWS CLI profile to use for deployments
### 2 - Once configuration is complete, you will have a zappa_settings.json with some basic configuration for your lambda envs - run `zappa deploy ENV` (default env is `dev`) - you should have a running deployment in a short moment.
### You should get an URL in the output, which if opened should complain that HTTP_HOST header is dissalowed at `/` - this is the default security behaviour of Django. To workaround it, we need to allow the header in django.
### 3 - In your config folder, edit "settings.py" and add the lambda URL to `ALLOWED_HOSTS` (full *base* url e.g. `er709uyw7j.execute-api.eu-west-1.amazonaws.com`)
### 4 - once that is done, run `zappa update ENV` and once the deployment is complete, you should have the application up and running.

___
## Setting up Dynaconf
### 1 - `pip install dynaconf`
### 2 - `export DJANGO_SETTINGS_MODULE=yourapp.settings` e.g. config.settings. then run `dynaconf init`
### This should create a settings.toml, but a fair few formats can be used (in our example - .yaml)
### The settings file can be used to set any kind of config, but the more usefull case can be having the conf in redis - in which case you can have the settings update without redeploying, setting only the app env and the rest be controlled through the external key/value store (including secrets in e.g. vault)

___
## Setting up multiple environments
### 1 - Edit zappa_settings.json and add other envs as needed, changing bucket/profile/project name etc.
### 2 - Same as in first stage, just run `zappa deploy ENV` e.g. stage and update allowed hosts and run `zappa update ENV`
### Its as easy as that to run different envs.