#!venv/bin/python
from flask import Flask, jsonify, request, render_template

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
    return render_template("index.html")
    #return "Hello, World!\n Welcome to this basic To-Do Application built using Flask."

@app.route('/api/v1/tasks')
def all_tasks():
    return render_template("alltasks.html", parent_dict=tasks)

@app.route('/api/v1/tasks/<id>', methods=['GET'])
def get_task(id):
    id = int(id)
    task = [task for task in tasks if task['id'] == id]
    return render_template("task.html", task=task[0])

@app.route('/create', methods=['POST'])
def create_task():
    tasks.append(request.get_json())
    return 'Success!', 200

@app.route('/api/v1/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    id = int(id)
    task = [task for task in tasks if task['id'] == id]
    tasks.remove(task[0])
    return jsonify({'result': True})
    # return render_template("alltasks.html", parent_dict=tasks)

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
