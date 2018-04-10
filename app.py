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
    return redirect(url_for("all_tasks"))

@app.route('/api/v1/tasks')
def all_tasks():
    return render_template("alltasks.html", parent_dict=tasks)

@app.route('/api/v1/tasks/<id>', methods=['GET'])
def get_task(id):
    id = int(id)
    task = [task for task in tasks if task['id'] == id]
    return render_template("task.html", task=task[0])

@app.route('/api/v1/create', methods=['GET','POST'])
def create_task():
    task = {
            'id': tasks[-1]['id'] + 1,
            'title': request.form.get("title"),
            'Priority': request.form.get("Priority"),
            'completed': request.form.get("completed")
            }
    tasks.append(task)
    return render_template("alltasks.html", parent_dict=tasks)

@app.route('/api/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    id = int(id)
    task = [task for task in tasks if task['id'] == id]
    tasks.remove(task[0])
    return render_template("alltasks.html", parent_dict=tasks)

@app.route('/api/v1/tasks/<id>', methods=['PUT'])
def update_task(id):
    id = int(id)
    task = [task for task in tasks if task['id'] == id]
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['Priority'] = request.json.get('Priority', task[0]['Priority'])
    task[0]['completed'] = request.json.get('completed', task[0]['completed'])
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
