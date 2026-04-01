import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['task_list'] = ["First Task"]
    with app.test_client() as client:
        yield client


def test_valid_list_task_endpoint(client):
    response = client.get('/listTasks')
    assert response.status_code == 200


def test_valid_add_task_endpoint(client):
    response = client.post('/addTask', json={'task': 'Test Task'})
    assert response.status_code == 200
    assert response.json == {"message": "Task Test Task successfully added!"}


def test_valid_delete_task_endpoint(client):
    response = client.post('/deleteTask', json={'task_number': 0})
    assert response.status_code == 200
    assert response.json == {
        "message": "Task First Task successfully deleted!"}


def test_invalid_delete_task_endpoint(client):
    response = client.post('/deleteTask', json={'task_number': 2})
    assert response.status_code == 404
    assert response.json == {
        "message": "Task was not found!"}
