from flask  import Flask
from collections import defaultdict
from status import Status
import uuid
from collections import *

class TaskManager(object):
    def __init__(self):
        self.data = defaultdict()

    def get_task(self):
        with persist(self):
            return self.data.get(id)

    def add_task(self):
        with persist(self):
            self.data[task.id] = task 
    # Stop the Task 
    def stop(self, id):
        with persist(self):
            if id not in self.data.key():
                return None
            else:
                return self.data.pop(id)
    def update(self, task):
        with persist(self):
            self.data[task.id] = task

    def clear_cache(self, key):
        if key is not None:
            return key 
        else:
            key = self.get.data(id) 
            return key[mid+1]

task = TaskManager(task)

class Task(object):
    def __init__(self,id, status, 
            job, result=None, error=None):
        
        self.id = id
        self.result = result 
        self.error = error
        self.job = job
        self.status = status
        
    @staticmethod
    def create_task():
        return Task(id= uuid.uuid4())
    def run_task(self):
        self.status = status.RUNNING
        return worker.task.delay(self.id)

    def update_(self, status):
        self.status = status

    @property
    def task_staus(self):
        return self.status


    def __iter__(self):
        yield 'ID', str(self.id)
        yield 'Status', self.status
        yield 'Error', self.error
        yield 'Job Result', self.result
        yield 'JobDefinition', self.job

    def __str__(self):
        return str(dict(self))





