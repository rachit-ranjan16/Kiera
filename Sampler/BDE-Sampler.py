# resize image to 64*64 to standardize the input for the training data
# from skimage import data
# from matplotlib import pyplot as plt
from skimage import io
from skimage.transform import resize
from scipy import misc
from PIL import Image
import glob
#CURE-TSR/Real_Train/*/*.bmp
i=1
for filename in glob.glob('CURE-TSR/Real_Train/*/*.bmp'): #read all bmp files from all the folders in Real_Train folder
    im= io.imread(filename)
    g=resize(im, (64, 64),mode='reflect') #resize the image to 64*64 size
    saveName='resizeImage/'+ filename[6:]
    print(saveName)
    misc.imsave(saveName, g)
    i=i+1
    #io.imshow(g)
    #plt.show()