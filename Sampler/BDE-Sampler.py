# resize image to 64*64 to standardize the input for the training data
# from skimage import data
# from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import resize
from scipy import misc
#from PIL import Image
import glob
import os
from configparser import ConfigParser
#CURE-TSR/Real_Train/*/*.bmp
FRAME_SIZE = 'frame_size'
DEEP_LEARNING = 'DeepLearning'


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

    def process_images(self, location):
        i = 1
        for filename in glob.glob(location): #read all bmp files from all the folders in Real_Train folder
            im = io.imread(filename)
            img_size = self.config.get('%s' % DEEP_LEARNING, '%s' % FRAME_SIZE)
            g = resize(im, (img_size, img_size), mode='reflect') #resize the image to 64*64 size
            saveName = 'resizeImage/' + filename[6:]
            print(saveName)
            misc.imsave(saveName, g)
            i = i+1
            #io.imshow(g)
            #plt.show()