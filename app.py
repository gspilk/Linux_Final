from flask import Flask, current_app, jsonify, request

app = Flask(__name__)

app.config['task_list'] = []


@app.route('/listTasks', methods=['GET'])
def list_task():
    return jsonify(app.config['task_list']), 200


@app.route('/addTask', methods=['POST'])
def add_task():
    task = request.json.get('task')
    current_app.config['task_list'].append(task)
    return jsonify({"message": "Task {task} successfully added!"})


@app.route('/deleteTask', methods=['POST'])
def delete_task():
    task_index = request.json.get('task_number')
    current_app.config['task_list'].remove(task_index)
    return jsonify({"message": "Task {task} successfully removed!"})


if __name__ == '__main__':
    app.run()
