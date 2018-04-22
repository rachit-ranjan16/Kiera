import celery
import time
from .learn import DeepLearn


@celery.task
def init_learning():
    #TODO Add Deep Learning Inititalization Code
    dL = DeepLearn()
    dL.init_deep_learning()
    #TODO Add Implementation to save Model and Statistics
    # TODO Add Status Update for Async Task
