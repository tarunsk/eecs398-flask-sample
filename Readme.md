## To-Do List Sample Application with Flask

This appication is inspired and based on the tutorial by [Miguel Grinberg](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask). It was used as a live demo during a staff lecture of EECS 398 Computing for Computer Scientists, taught at the University of Michigan, Ann Arbor in Winter 2018.

The main purpose of this application is to demonstrate how to build a basic RESTful API in Python using [Flask](http://flask.pocoo.org/).

This branch holds the starter code that was provided to the students. You may access the finished project [here](https://github.com/tarunsk/eecs398-flask-sample/tree/master).

## Setup

### Requirements
This application is written in [Python 2.7.13](https://www.python.org/downloads/) and uses `virtualenv` to manage a virtual environment. To install `virtualenv`:
```
$ pip install virtualenv
```


### Setup Instructions
Start by cloning this repository into the desired location and then navigate into the directory. Then setup a virtual
environment:
```
$ virtualenv venv
```

Activate the virtual environment:
```
$ . venv/bin/activate
```

Install Flask:
```
$ pip install Flask
```

## Running Locally
By default this application will run on `0.0.0.0:5000`. To start a local instance:
```
$ ./app.py
```
