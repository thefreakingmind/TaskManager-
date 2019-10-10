from flask import Flask
from taskmanager import TaskManager 
from taskmanager  import Task 
import logging
from celery import * 

app = Flask(__name__)
log = logging.create_logger(app)

taskworker = TaskManager(task)

''' 
The Code to Create The Complete Task Management System
Replacing the Existing one.
'''

@app.route('/task', methods['POST'])
def create_task():
    task = Task.create_task()
    taskworker.add_task(task)
    log.infor("Task Created")
    return str(task.id), 201

@app.route('/task/<task_id>', methods=['GET', 'PUT', 'DELETE'])
def task(task_id):
    try:
        id = uuid.UUID(task_id)
    except Exception as e:
        log.error(e)
        return "Error",  400
    task = taskworker.get_task(id)
    if task is None:
        return "Task Does not Exist", 404
    if request.method == 'GET':
        return str(task)
    if request.method == 'PUT':
        task.run_task()
        task.update_task(task)
        return '', 202
    if request.method == 'DELETE':
        latest_status = task.status
        task.delete_task(task.id)
        return latest_status, 200 

@app.task()
def task(task_id):
    task = task_dao.get_task(uuid.UUID(task_id))
    log.info("Task Running Started")
    task.result()
    print("Task Completed Successfully")
    task.delete()
    print("Task Stopped")

