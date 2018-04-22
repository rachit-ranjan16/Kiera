import celery
import time


@celery.task
def init_learning(dL):
    # # TODO Remove this
    # print("Going to sleep for 10s")
    # time.sleep(10)
    # print("I'm back up")
    #TODO Add Deep Learning Inititalization Code
    dL.init_deep_learning()
