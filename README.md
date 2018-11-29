# CodeFirst:Girls Deployment Guide
## Introduction
What is deploying? This is a technical word for releasing your software out into the world! Instead of running your Flask webserver on localhost, you'll be able to get the code running on a machine and accessible from anywhere with an internet connection.

## Example Application
This repository contains the config files you'll need to deploy to Heroku. Don't copy and paste yet! We'll do that later. 

Go to [http://damp-meadow-68595.herokuapp.com/](http://damp-meadow-68595.herokuapp.com/) (sorry, the name was generated...) and compare it to the [routes](deploytest.py) and [templates](templates) in this repository. Can you see when each HTML file is used?

## Guide
*Only one person needs to do this per team. If you'd like to share an account, pick a password you can both use!*

1. Go to [heroku.com](https://www.heroku.com/) and create an account
2. Install the [Heroku Command Line Interface](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
3. `cd` to the project folder in your terminal. Make sure you have a git repository pointing to this already, and if not create a repository!
4. Type `heroku login` and follow the instructions
5. Make sure you've pushed all of your changes to your normal git repository.
6. Copy the following files from this repository:
 - [Procfile](Procfile)
 - [runtime.txt](runtime.txt)
 - [uwsgi.ini](uwsgi.ini)
 - Optional: [.gitignore](.gitignore) can you guess what it does?
7. Change the line that starts with `module=` in `uwsgi.ini` to reflect your project. In this example, the filename, and to python this is the **module name** is `deploytest`, and the **app name** is `app`.
8. You can use the [requirements.txt](requirements.txt) in this project, however if you've done a `pip install` for anything else then run `pip freeze > requirements.txt` in your terminal to grab all the packages you've installed, and overwrite this file. This tells the server to install anything extra that it needs from pip.
9. In your main python file, make sure that you don't run the app when you're not executing the file, e.g.
```python
if __name__ == '__main__':
    app.run(debug=True)
# NOT app.run(debug=True) on its own!
```
10. Almost there! Run `git push heroku` in the terminal. This pushes your code to Heroku, which will apply the changes to your (hopefully running) server.

## Push to GitHub, push to Heroku
Every time you make a change, the commands you run will be as follows:
```sh
# the dot means add all changed files
git add .
git commit -m "Your message here"
# push to GitHub
git push
# push to Heroku
git push heroku
```
