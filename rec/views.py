from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from enum import Enum
import json
import requests
from .learn import DeepLearn
from .tasks import init_learning
# Create your views here.


class State(Enum):
    # TODO Decide if this has to be moved to utils package
    READY = 1
    IN_PROGRESS = 2
    COMPLETED = 3


state_dict = {
    State.READY: 'READY',
    State.IN_PROGRESS: 'IN_PROGRESS',
    State.COMPLETED: 'COMPLETED'
}

state = State.READY

def get_status(body):
    print(body)

class TSRView(View):

    def __init__(self):
        self.state = State.READY
        self.dL = DeepLearn()

    def get(self, request):
        # TODO Add implementation for returning accuracy of the trained Deep Learning Model
        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse().status_code
        if tokens[2] == 'status':
            response = HttpResponse(json.dumps({'state': state_dict[self.state]}), content_type="application/json")
        elif tokens[2] == 'accuracy':
            response = HttpResponse(json.dumps({'accuracy': self.dL.get_accuracy()}), content_type="application/json")
        response.status_code = 200
        return response


    def post(self, request):
        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse(status=400)
        if tokens[2] == 'train':
            # POST /rec/train Initiate Training if State is READY or COMPLETED
            if self.state in (State.READY, State.COMPLETED):
                # Initiate Training
                self.async = init_learning.apply_async()
                print(self.async.get(on_message=get_status(), propagate=False))
                self.state = State.IN_PROGRESS
                return HttpResponse(status=201)
            elif self.state == State.IN_PROGRESS:
                return HttpResponse(status=202)
        elif tokens[2] == 'predict':
            try:
                r = requests.get(json.load(request.body)['image-url'])

            except Exception:
                return HttpResponse(status=400)

