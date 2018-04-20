from celery import shared_task
import time

@shared_task
def init_learning(dl):
    # TODO Remove this
    print("Going to sleep for 10s")
    time.sleep(10);
    print("I'm back up")
    #TODO Add Deep Learning Inititalization Code