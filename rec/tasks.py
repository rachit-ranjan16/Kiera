import celery
import time
from .learn import DeepLearn



@celery.task
def init_learning():
    dL = DeepLearn()
    print('Initiating Deep Learning')
    # dL.init_deep_learning()
    try:
        dL.init_deep_learning()
        print('Training Completed\nModel Saved')
        # TODO Add method in DeepLearn to save model
        print('Updating Status')
        with open('status_info.txt', mode='w') as f:
            f.write('COMPLETED')
            f.close()
    except Exception as e:
        print("Caught Exception %r" % e)
        with open('status_info.txt', mode='w') as f:
            f.write('ERROR')
            f.close()
