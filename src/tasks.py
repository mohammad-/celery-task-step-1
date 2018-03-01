from celery import Celery

app = Celery('tasks', broker='amqp://user1:somepass@messageq_test/hard_work')

@app.task
def add(a, b):
    return "Sum is ", a+b