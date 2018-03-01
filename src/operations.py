from celery import Celery

app = Celery('operations', broker='amqp://mohd:mohd@messageq_test/queue1')

@app.task
def reverse_string(name):
    return name[::-1]