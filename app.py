#!venv/bin/python
from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Prepare staff lecture',
        'Priority': 10,
        'completed': False
    },
    {
        'id': 2,
        'title': 'Complete 281 Project',
        'Priority': 8,
        'completed': False
    }
]

@app.route('/')
def index():
    # TODO: Redirect to all_tasks
    return

@app.route('/create')
def create():
    # TODO: Redirect to form to create a task
    return

@app.route('/api/v1/tasks')
def all_tasks():
    # TODO: Retrieve all tasks
    return

@app.route('/api/v1/tasks/<id>', methods=['GET'])
def get_task(id):
    return

@app.route('/api/v1/create', methods=['GET','POST'])
def create_task():
    # TODO: Create event and append to dictionary
    return

@app.route('/api/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    # TODO: Remove a task with the specified ID
    return

@app.route('/api/v1/tasks/<id>', methods=['PUT'])
def update_task(id):
    # TODO: Update a task with the specified ID
    return

@app.route('/api/v1/tasks/<id>', methods=['POST'])
def mark_complete(id):
    # TODO: Wrapper for DELETE
    return

if __name__ == '__main__':
    app.run(debug=True)
