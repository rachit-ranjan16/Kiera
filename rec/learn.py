import time
from configparser import ConfigParser
import os
from celery import shared_task
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten,Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.optimizers import RMSprop,SGD,Adam
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from utils.sampler import Sampler

label_dict = {0: 'speed_limit',
              1: 'goods_vehicles',
              2: 'no_overtaking',
              3: 'no_stopping',
              4: 'no_parking',
              5: 'stop',
              6: 'bicycle',
              7: 'hump',
              8: 'no_left',
              9: 'no_right',
              10: 'priority_to',
              11: 'no_entry',
              12: 'yield',
              13: 'parking'}

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
        # # TODO Remove test code
        # print("Going to sleep for 10s")
        # time.sleep(10)
        # print("Woke up from Sleep")
        # #TODO Uncomment these
        self.process_data()
        self.create_model()
        self.train_model()

    def process_data(self):
        location = self.config['img']['train_data_set_location']
        self.sampler.read_and_process_images(location)
        self.data, self.labels = self.sampler.get_images_and_labels()
        #TODO Add Data Split for Training and Validation Set

    def create_model(self):
        """Creates a Deep Learning Convolutional Neural Net Model"""
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
        self.model.add(Dense(len(label_dict.keys())))
        self.model.add(Activation('softmax'))
        # TODO Remove this print
        print(self.model.summary())

    def train_model(self):
        """Trains Model """
        self.model.compile(loss='categorical_crossentropy',
                           optimizer=SGD(lr=float(self.config['hyperparameters']['learning_rate']),
                                         momentum=float(self.config['hyperparameters']['momentum']),
                                         decay=float(self.config['hyperparameters']['decay']),
                                         nesterov=False),
                           metrics=['accuracy'])
        # Split data and labels into training, validation and test sets
        x_train, x_test, y_train, y_test = train_test_split(self.data, self.labels,
                                                            test_size=float(self.config['hyperparameters']['split']),
                                                            random_state=42)
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,
                                                          test_size=float(self.config['hyperparameters']['split']),
                                                          random_state=42)
        # One Hot Encoding for Output Labels
        y_train = to_categorical(y_train, len(label_dict.keys()))
        y_val = to_categorical(y_val, len(label_dict.keys()))
        y_test = to_categorical(y_test, len(label_dict.keys()))

        # Train
        history = self.model.fit(x_train, y_train,
                                 batch_size=int(self.config['hyperparameters']['batch_size']),
                                 epochs=int(self.config['hyperparameters']['epochs']),
                                 verbose=1,
                                 validation_data=(x_val, y_val))

        self.plot_loss_accuracy(history)
        self.score = self.model.evaluate(x_test, y_test)
        # TODO Remove this
        print("Accuracy %.6f" % self.score[1])

    def plot_loss_accuracy(self, history):
        fig, ax = plt.subplots(1, 2, figsize=(12, 6))
        ax[0].plot(history.history["loss"], 'r-x', label="Train Loss")
        ax[0].plot(history.history["val_loss"], 'b-x', label="Validation Loss")
        ax[0].legend()
        ax[0].set_title('cross_entropy loss')
        ax[0].grid(True)

        ax[1].plot(history.history["acc"], 'r-x', label="Train Accuracy")
        ax[1].plot(history.history["val_acc"], 'b-x', label="Validation Accuracy")
        ax[1].legend()
        ax[1].set_title('accuracy')
        ax[1].grid(True)
        plt.savefig('LossAndAccuracy.png')

    def get_accuracy(self):
        return self.score[1]

    def predict(self, img):
        return label_dict[self.model.predict(self.sampler.process_image(img)).argmax() + 1]


if __name__ == '__main__':
    print("inside main")
    dL = DeepLearn()
    print("after Deeplearn")
    dL.process_data()
    print("after process data")
    dL.create_model()
    print("after create model")
    dL.train_model()
    print("after train model")
