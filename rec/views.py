
from django.views import View
from django.http import HttpResponse
import json
import os
import matplotlib
matplotlib.use('Agg')
from skimage import io
from .learn import DeepLearn
from .tasks import init_learning
from .models import Status
# Create your views here.

Status(status='READY').save()


def get_status():
    return Status.objects.latest('updated').status

class TSRStatusView(View):
    def get(self, request):
        try:
            response = HttpResponse(json.dumps({'status': get_status()}), content_type="application/json")
            return response
        except Exception as e:
            print("Caught Exception %r" % e)
            return HttpResponse(status=500)



class TSRTrainView(View):

    def post(self,request):
        try:
            if get_status() == 'IN_PROGRESS':
                return HttpResponse(status=202)
            else:
                Status(status='IN_PROGRESS').save()
                init_learning.apply_async()
                return HttpResponse(status=201)
        except Exception as e:
            print("Caught Exception %r" % e)
            return HttpResponse(status=500)


class TSRAccuracyView(View):

    def get(self, request):
        try:
            with open('accuracy.txt', mode='r') as f:
                response = HttpResponse(json.dumps({'accuracy': f.read()}), content_type='application/json')
            return response
        except FileNotFoundError:
            response = HttpResponse(json.dumps({'error': 'Model not trained yet'}), content_type='application/json')
            response.status_code = 400
            return response
        except Exception as e:
            print("Caught Exception %r" % e)
            return HttpResponse(status=500)


class TSRPredictionView(View):

    def post(self, request):
        try:
            #TODO Setup external image hosting service and get image from there
            image_url = json.load(request.body)['image-url']
            img = io.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep +
                            'utils' + os.sep + '4.bmp')
            dL = DeepLearn()
            dL.predict(img)
            return HttpResponse(json.dumps({'predicted_class_label': dL.predict()}), content_type="application/json")
        except KeyError:
            return HttpResponse(status=400)
        except Exception as e:
            print("Caught Exception %r" % e)
            return HttpResponse(status=500)


