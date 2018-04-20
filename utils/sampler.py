# resize image to 64*64 to standardize the input for the training data
# from skimage import data
# from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import resize
from scipy import misc
import numpy as np
import glob
import os
from configparser import ConfigParser

class Sampler:
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
            os.sep +
            'config' +
            os.sep +
            'appConfig.ini')
        self.score = 0

    def read_and_process_images(self, location):
        output_labels = []
        input_data = []
        for filename in glob.glob(location):
            im = io.imread(filename)
            img_size = int(self.config['img']['frame_size'])
            g = resize(im, (img_size, img_size), mode='reflect')
            save_name = 'resizeImage/' + filename.split('/')[2]
            output_labels.apend(int(filename.split('/')[2].split('_')[1]))
            input_data.append(g)
            misc.imsave(save_name, g)
        return np.array(input_data), np.array(output_labels)

    def process_image(self, im):
        img_size = int(self.config['img']['frame_size'])
        return np.array(resize(im, (img_size, img_size), mode='reflect'))
