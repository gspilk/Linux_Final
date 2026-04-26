'''
app.py is the module to run the backend and frontend locally.
'''
from flask import Flask, current_app, jsonify, request, render_template

app = Flask(__name__)

app.config['task_list'] = []



@app.route('/')
def index():
    '''
    This endpoint renders the frontend.
    '''
    return render_template('webpage.html')


@app.route('/listTasks', methods=['GET'])
def list_task():
    '''
    This endpoint lists all the current tasks.
    '''
    return jsonify(app.config['task_list']), 200


@app.route('/addTask', methods=['POST'])
def add_task():
    '''
    This endpoint adds a task to current list.
    '''
    task = request.json.get('task')
    current_app.config['task_list'].append(task)
    return jsonify({"message": f"Task {task} successfully added!"}), 200


@app.route('/deleteTask', methods=['POST'])
def delete_task():
    '''
    This endpoint deletes a task from the current list.
    '''
    try:
        task_index = request.json.get('task_number')
        deleted_task = current_app.config['task_list'].pop(task_index)
        return jsonify({"message": f"Task {deleted_task} successfully deleted!"}), 200
    except (IndexError, KeyError):
        return jsonify({"message": "Task was not found!"}), 404


@app.route('/updateTask', methods=['POST'])
def update_task():
    '''
    This endpoint updates a task from the current list.
    '''
    try:
        task_index = request.json.get('task_number')
        new_task = request.json.get('new_task')
        current_app.config['task_list'][task_index] = new_task
        return jsonify({"message": f"Task successfully updated to {new_task}!"}), 200
    except (IndexError, KeyError):
        return jsonify({"message": "Task was not found!"}), 404


if __name__ == '__main__':
    app.run()
