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
    return jsonify({"message": f"Task {task} successfully added!"}), 200


@app.route('/deleteTask', methods=['POST'])
def delete_task():
    try:
        task_index = request.json.get('task_number')
        deleted_task = current_app.config['task_list'].pop(task_index)
        return jsonify({"message": f"Task {deleted_task} successfully deleted!"}), 200
    except Exception:
        return jsonify({"message": f"Task was not found!"}), 404


if __name__ == '__main__':
    app.run()
