from flask import Flask 


'''
Getting The Status of The Task/Job
'''
class Status(object):
    CREATE = 'CREATED'
    DELETED = 'DELETED'
    RUNNING = 'RUNNING'
    STOPPED = 'STOPPED'
    DONE = 'DONE'


