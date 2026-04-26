'''
test_app.py is the module tests the api endpoints in app.py
'''
import pytest
from app import app


@pytest.fixture(name="client")
def fixture_client():
    '''
    fixture_client is the fixture for client to store the info about app including task_list.
    '''
    app.config['TESTING'] = True
    app.config['task_list'] = ["First Task"]
    with app.test_client() as api_client:
        yield api_client


def test_valid_list_task_endpoint(client):
    '''
    test_valid_list_task_endpoint is this tests ensures endpoint lists tasks. 
    '''
    response = client.get('/listTasks')
    assert response.status_code == 200
    assert response.json == ["First Task"]


def test_valid_add_task_endpoint(client):
    '''
    test_valid_add_task_endpoint is this tests ensures successfully adds task. 
    '''
    response = client.post('/addTask', json={'task': 'Test Task'})
    assert response.status_code == 200
    assert response.json == {"message": "Task Test Task successfully added!"}
    assert app.config['task_list'] == ["First Task", "Test Task"]


def test_valid_update_task_endpoint(client):
    '''
    test_valid_update_task_endpoint is this tests ensures successfully able to delete a task.
    '''
    response = client.post(
        '/updateTask', json={'task_number': 0, "new_task": "Updated Task"})
    assert response.status_code == 200
    assert response.json == {
        "message": "Task successfully updated to Updated Task!"}
    assert app.config['task_list'] == ["Updated Task"]


def test_invalid_update_task_endpoint(client):
    '''
    test_valid_update_task_endpoint is this tests ensures catching an attempt 
        to update a task that does not exist. 
    '''
    response = client.post(
        '/updateTask', json={'task_number': 2, "new_task": "Updated Task"})
    assert response.status_code == 404
    assert response.json == {
        "message": "Task was not found!"}
    assert app.config['task_list'] == ["First Task"]
