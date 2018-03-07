from django.shortcuts import render
from django.http import HttpResponse
from enum import Enum
# Create your views here.


class State(Enum):
    # TODO Decide if this has to be moved to utils package
    READY = 1
    IN_PROGRESS = 2
    COMPLETED = 3


state_dict = {
    State.READY: 'READY',
    State.IN_PROGRESS: 'Training in Progress',
    State.COMPLETED: 'Training Completed'
}

state = State.READY


def init(request):
    # TODO Add implementation for Async POST Call
    pass


def status(request):
    if request.method == 'GET':
        response = HttpResponse(state_dict[state], content_type="text/plain")
        response.status_code = 200
        return response
    else:
        return HttpResponse(status=405)


def accuracy(request):
    # TODO Add implementation for returning accuracy of the trained Deep Learning Model
    # TODO Finalize url pattern
    pass


def prediction(request):
    # TODO Add implementation for returning prediction of a given image after running it through the trained model
    # TODO Finalize url pattern
    pass
