import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np
from configparser import ConfigParser
import os
from celery import shared_task
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D

from utils.sampler import Sampler


LEARNING_RATE = 'learning_rate'
BATCH_SIZE = 'batch_size'
EPOCHS = 'epochs'
label_dict = {1: 'speed_limit',
              2: 'goods_vehicles',
              3: 'no_overtaking',
              4: 'no_stopping',
              5: 'no_parking',
              6: 'stop',
              7: 'bicycle',
              8: 'hump',
              9: 'no_left',
              10: 'no_right',
              11: 'priority_to',
              12: 'no_entry',
              13: 'yield',
              14: 'parking'}

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
        self.model = None
        self.data = None
        self.labels = None
        self.sampler = Sampler()

    # Asynchronous Driver Method
    @shared_task
    def init_deep_learning(self):
        self.process_data()
        self.create_model()
        self.train_model()

    def process_data(self):
        self.data, self.labels = self.sampler.process_images()

    def create_model(self):
        # Layer 1: Conv
        self.model = Sequential()
        self.model.add(Conv2D(32, (5, 5), strides=(1, 1), padding='same',
                           input_shape=self.data.shape[1:]))
        self.model.add(Activation('relu'))
        # Layer 2: Conv
        self.model.add(Conv2D(32, (5, 5), strides=(1, 1)))
        self.model.add(Activation('relu'))
        # Layer 3: MaxPool
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        # Layer 4: Conv
        self.model.add(Conv2D(32, (5, 5), strides=(1, 1)))
        self.model.add(Activation('relu'))
        # Layer 5: Conv
        self.model.add(Conv2D(32, (5, 5), strides=(1, 1)))
        self.model.add(Activation('relu'))
        # Layer 6: MaxPool
        self.model.add(MaxPooling2D(pool_size=(2, 2)))
        self.model.add(Dropout(0.25))
        # Layer 7: Flatten
        self.model.add(Flatten())
        # Layer 8: Dense
        self.model.add(Dense(512))
        self.model.add(Activation('relu'))
        self.model.add(Dropout(0.5))
        # Layer 9: Dense Final Classification
        self.model.add(Dense(num_classes))
        self.model.add(Activation('softmax'))
        self.model.summary()

    def train_model(self):
        # TODO Add Implementation for training
        pass

    def get_accuracy(self):
        return self.score[1]

    def predict(self, idx):
        # TODO Add Implementation for prediction
        pass
        # return self.model.predict(np.array([self.x_train[idx]])).argmax()

