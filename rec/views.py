
from django.views import View
from django.http import HttpResponse
import json
import os
from skimage import io
from .learn import DeepLearn
from .tasks import init_learning
# Create your views here.


class Status:

    def __init__(self):
        self.status = 'READY'
        with open('status_info.txt', mode='w+') as f:
            f.close()

    def get_status(self):
        with open('status_info.txt', mode='r+') as f:
            if f.read() == "":
                #TODO Promote to Log
                f.write(self.status)
                f.close()
                return self.status
            else:
                self.status = f.read()
                f.close()
                return self.status

    def put_status(self, status):
        with open('status_info.txt', mode='w') as f:
            f.write(status)


st = Status()


class TSRStatusView(View):
    def get(self, request):
        try:
            response = HttpResponse(json.dumps({'status': st.get_status()}), content_type="application/json")
            return response
        except Exception as e:
            print("Caught Exception %r" % e)
            return HttpResponse(status=500)


class TSRTrainView(View):

    def post(self,request):
        try:
            if st.get_status() == 'IN_PROGRESS':
                return HttpResponse(status=202)
            else:
                init_learning.apply_async()
                st.put_status('IN_PROGRESS')
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


