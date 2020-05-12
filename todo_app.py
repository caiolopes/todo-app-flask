from flask import Flask, render_template


app = Flask('task_app')

tasks = [
    {
        "name": "Passear com meu cachorro",
        "done": False
    },
    {
        "name": "Fazer o almoço de amanhã",
        "done": True
    },
    {
        "name": "Estudar para a prova do módulo 3",
        "done": False
    },
]

@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/lista')
def list_tasks():
    return 'Lista de tarefas'


#  eh equivalente a isso:
#  func = app.route('/lista')
#  func(list_tasks)


app.run(host="0.0.0.0", debug=True)





