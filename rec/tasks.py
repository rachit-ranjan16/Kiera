import celery
import time
from .learn import DeepLearn
from .views import Status


@celery.task
def init_learning():
    dL = DeepLearn()
    print('Initiating Deep Learning')
    # dL.init_deep_learning()
    dL.test_save_model()
    print('Training Completed\nModel Saved')
    # TODO Add method in DeepLearn to save model
    print('Updating Status')
    Status.current = 'COMPLETED'
