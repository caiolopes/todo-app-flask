import json
import os
from flask import Flask, render_template, jsonify, request


app = Flask('task_app')

def init_db():
    if not os.path.exists('tasks.json'):
        with open('tasks.json', 'w') as fp:
            json.dump([], fp)


init_db()


def read_tasks():
    with open('tasks.json', 'r') as fp:
        tasks = json.load(fp)

    return tasks
    
def save_tasks(tasks):
    with open('tasks.json', 'w') as fp:
        json.dump(tasks, fp)


@app.route('/')
def menu():
    return render_template('menu.html')


@app.route('/lista')
def list_tasks():
    tasks = read_tasks()

    return render_template('list.html', tasks=tasks)
    
    
@app.route('/api/v1/lista')
def list_tasks_api():
    tasks = read_tasks()

    search_name = request.args.get('nome')
    if search_name:
        search_name = search_name.lower()
        tasks = [task for task in tasks
                if search_name in task['name'].lower()]    

    return jsonify(tasks)


def get_task(task_id):
    tasks = read_tasks()
    
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)
    
    return jsonify({"error": "Not found"})
    
    
def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]

    removed_task = get_task(task_id)
    save_tasks(tasks)
    
    return removed_task


def edit_task(task_id):
    tasks = read_tasks()
    new_task = request.get_json()
    
    new_tasks = []
    for task in tasks:
        if task['id'] == task_id:
            new_tasks.append(new_task)
        else:
            new_tasks.append(task)
    
    save_tasks(new_tasks)
    return jsonify(new_task)


@app.route('/api/v1/tarefa/<int:task_id>',
    methods=['GET', 'DELETE', 'PUT'])
def get_task_api(task_id):
    if request.method == 'GET':
        return get_task(task_id)
        
    if request.method == 'DELETE':
        return delete_task(task_id)
        
    if request.method == 'PUT':
        return edit_task(task_id)
    

@app.route('/api/v1/criar', methods=['POST'])
def create_task():
    tasks = read_tasks()
    task = request.get_json()

    if len(tasks) > 0:
        task_id = tasks[-1]['id'] + 1
    else:
        task_id = 1
    
    new_task = {
        "id": task_id,
        "name": task["name"],
        "done": False,
    }
    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task)
    


app.run(host="0.0.0.0", debug=True)



