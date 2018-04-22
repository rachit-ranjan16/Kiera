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


class TSRStatusView(View):
    #TODO Fix Status
    def get(self, request):
        #TODO Remove this
        return HttpResponse(status=202)

        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse().status_code
        if tokens[2] == 'status':
            response = HttpResponse(json.dumps({'status': state_dict[self.state]}), content_type="application/json")
            return response
        else:
            return HttpResponse(status=400)

        return HttpResponse(status=500)


class TSRAccuracyView(View):

    def get(self, request):
        #TODO Remove this
        return HttpResponse(status=202)

        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse().status_code
        if tokens[2] == 'accuracy':
            response = HttpResponse(json.dumps({'accuracy': self.dL.get_accuracy()}), content_type="application/json")
            return response
        else:
            return HttpResponse(status=400)

        return HttpResponse(status=500)


class TSRTrainView(View):

    def post(self, request):
        tokens = request.path.split('/')
        if len(tokens) > 3:
            return HttpResponse(status=400)
        if tokens[2] == 'train':
            # POST /rec/train Initiate Training if State is READY or COMPLETED
            if self.state in (State.READY, State.COMPLETED):
                # Initiate Training
                init_learning.apply_async()
                # print(self.async.get(on_message=get_status(), propagate=False))
                self.state = State.IN_PROGRESS
                return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

        return HttpResponse(status=500)


class TSRPredictionView(View):

    def post(self, request):
        #TODO Remove this
        return HttpResponse(status=202)