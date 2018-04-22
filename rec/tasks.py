import celery
import time
from .learn import DeepLearn
from .models import Status



@celery.task
def init_learning():
    dL = DeepLearn()
    print('Initiating Deep Learning')
    # dL.init_deep_learning()
    try:
        dL.init_deep_learning()
        print('Training Completed\nModel Saved')
        print('Updating Status')
        Status(status='COMPLETED').save()

    except Exception as e:
        print("Caught Exception %r" % e)
        Status(status='ERROR').save()
