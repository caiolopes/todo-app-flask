
import json
from flask import Flask, render_template, jsonify, request


app = Flask('task_app')

def read_tasks():
    with open('tasks.json', 'r') as fp:
        tasks = json.loads(fp)

    return tasks


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
    return jsonify(tasks)
    
    
@app.route('/api/v1/criar', methods=['POST'])
def create_task():
    task = request.get_json()
    if len(tasks) > 0:
        task_id = tasks[-1]['id'] + 1

    tasks.append({
        "id": task_id,
        "name": task["name"],
        "done": False,
    })
    return jsonify(tasks)


#  eh equivalente a isso:
#  func = app.route('/lista')
#  func(list_tasks)


app.run(host="0.0.0.0", debug=True)




