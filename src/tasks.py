from celery import Celery

app = Celery('tasks', broker='amqp://mohd:mohd@messageq_test/queue1')

@app.task
def add(a, b):
    return "Sum is ", a+b