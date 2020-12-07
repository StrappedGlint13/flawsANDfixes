# Installation guide

This is a guide for install and run the application in your computer. Remember, that it is full of vulnerabilities, hence it's at your own responsibility to use it! This installation guide assumes that you have Python (3.5 or later) and Django installed. If not, [here](https://cybersecuritybase.mooc.fi/installation-guide) you can check installation instructions. 

## Clone the app to your computer 

Clone the app from Github to your local folder with the command:

`git clone git@github.com:StrappedGlint13/flawsANDfixes.git`

## Use the app

Go to your folder where you cloned the app. Then go to first "app"-folder. There is a file named "manage.py". Run:

`python3 manage.py runserver`

You can use test/admin user to login with:

### Admin user:
-   Username: admin
-   Password: 123456789

### test user:
-   Username: test
-   Password: test

With admin user you can check the votes results by setting url directly:

`http://127.0.0.1:8000/polls/1/results/`

