import celery
import time
from .views import TSRView


@celery.task
def init_learning():
    # TSRView.dL
    # TODO Remove this
    print("Going to sleep for 10s")
    time.sleep(10)
    print("I'm back up")
    #TODO Add Deep Learning Inititalization Code