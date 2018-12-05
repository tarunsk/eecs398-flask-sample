## To-Do List Sample Application with Flask

This appication is inspired and based on the tutorial by [Miguel Grinberg](https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask). It was used as a live demo during a staff lecture of EECS 398 Computing for Computer Scientists, taught at the University of Michigan, Ann Arbor.

The main purpose of this application is to demonstrate how to build a basic RESTful API in Python using [Flask](http://flask.pocoo.org/).

## Setup

### Requirements
This application is written in [Python 3.7.0](https://www.python.org/downloads/) and uses `virtualenv` to manage a virtual environment. To install `virtualenv`:
```
$ pip3 install virtualenv
```


### Setup Instructions
Start by cloning this repository into the desired location and then navigate into the directory. Then setup a virtual
environment:
```
$ python3 -m virtualenv venv
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
