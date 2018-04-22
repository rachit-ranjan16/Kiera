import celery
import time
from .learn import DeepLearn


@celery.task
def init_learning():
    # # TODO Remove this
    # print("Going to sleep for 10s")
    # time.sleep(10)
    # print("I'm back up")
    #TODO Add Deep Learning Inititalization Code
    dL = DeepLearn()
    dL.init_deep_learning()
