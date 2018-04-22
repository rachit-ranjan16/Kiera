
from django.views import View
from django.http import HttpResponse
import json
import requests
from .learn import DeepLearn
from .tasks import init_learning
# Create your views here.

class Status:
    current = 'READY'


class TSRStatusView(View):
    #TODO Fix this
    def get(self, request):
        try:
            response = HttpResponse(json.dumps({'status': Status.current}), content_type="application/json")
            return response
        except Exception as e:
            print("Caught Exception %r" % e.with_traceback())
            return HttpResponse(status=500)


class TSRTrainView(View):

    def post(self,request):
        try:
            if Status.current == 'IN_PROGRESS':
                return HttpResponse(status=202)
            else:
                init_learning.apply_async()
                Status.current = 'IN_PROGRESS'
        except Exception as e:
            print("Caught Exception %r" % e.with_traceback())
            return HttpResponse(status=500)

class TSRAccuracyView(View):

    def get(self, request):
        #TODO Fix this
        try:
            response = HttpResponse(json.dumps({'accuracy': 0.00}), content_type="application/json")
            return response
            return response
        except Exception as e:
            print("Caught Exception %r" % e.with_traceback())
            return HttpResponse(status=500)


class TSRPredictionView(View):
    #TODO Load deep learning model and get predictions
    #TODO Extract image from the image-url passed
    def post(self, request):
        try:
            return HttpResponse(status=202)

        except Exception as e:
            print("Caught Exception %r" % e.with_traceback())
            return HttpResponse(status=500)


