import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np
from configparser import ConfigParser
import os
from celery import shared_task

LEARNING_RATE = 'learning_rate'
BATCH_SIZE = 'batch_size'
EPOCHS = 'epochs'


# TODO Add Logging

class DeepLearn:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
            os.sep +
            'config' +
            os.sep +
            'appConfig.ini')
        self.score = 0

    # Asynchronous Driver Method
    @shared_task
    def init_deep_learning(self):
        self.process_data()
        self.create_model()
        self.train_model()

    def process_data(self):
        # TODO Call code for processing data
        pass

    def create_model(self):
        # TODO Create Model with configurable parameters
        pass

    def train_model(self):
        # TODO Add Implementation for training
        pass

    def get_accuracy(self):
        return self.score[1]

    def predict(self, idx):
        # TODO Add Implementation for prediction
        pass
        # return self.model.predict(np.array([self.x_train[idx]])).argmax()

