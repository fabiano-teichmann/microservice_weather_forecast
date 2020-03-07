from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')


@app.task
def sentence_length(sentence):
    return len(sentence)

