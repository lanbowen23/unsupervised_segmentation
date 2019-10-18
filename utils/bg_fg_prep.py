import matplotlib.image as img
import glob

import numpy as np
from scipy.ndimage import filters, measurements, interpolation
from math import pi
import cv2
import skimage.io
import os

def saliency_detect(image_name, t1=95, t2=105, dest='images'):
    '''

    t1: threshold for foreground hint  
    t2: threshold for background hint
    dest: destination forder name
    '''
    for saliency in glob.glob(image_name):  # output_scaled/*.png
        print(saliency)
        # s = img.imread(saliency)
        image = skimage.io.imread(saliency, 0)
        # print("image shape: ", image.shape)
        # print(image.max())

        image_fg = image.copy()
        image_fg[image > t1] = 255 
        image_fg[image <= t1] = 0
        print(r"output_fg/" + saliency.split('/')[-1])  # [len("images/seg/"):]
        os.makedirs(dest + r"/output_fg/", exist_ok=True)
        skimage.io.imsave(dest + r"/output_fg/" + saliency.split('/')[-1], image_fg)
        
        image_bg = image.copy()
        image_bg[image > t2] = 0
        image_bg[image <= t2] = 255
        print(r"output_bg/" + saliency.split('/')[-1])
        os.makedirs(dest + r"/output_bg/", exist_ok=True)
        skimage.io.imsave(dest + r"/output_bg/" + saliency.split('/')[-1], image_bg)

if __name__ == "__main__":
    saliency_detect