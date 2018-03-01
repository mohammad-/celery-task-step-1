from celery import Celery

app = Celery('operations', broker='amqp://user1:somepass@messageq_test/hard_work')

@app.task
def reverse_string(name):
    return name[::-1]