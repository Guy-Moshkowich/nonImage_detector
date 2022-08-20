import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage.io import imshow, imread
from skimage.color import rgb2gray
from skimage import img_as_ubyte, img_as_float
from skimage.exposure import histogram, cumulative_distribution
from skimage import io
from os import listdir
from os.path import isfile, join
from skimage import exposure
import os
import datetime


def main():
    plt.figure(num=None, figsize=(8, 6), dpi=80)
    mypath = './data/'
    for f in listdir(mypath):
        if isfile(join(mypath, f)):
            file_path = mypath + f
            image = io.imread(file_path)
            image_grey = img_as_ubyte(rgb2gray(image))
            image_grey = exposure.adjust_log(image_grey, 1)
            freq, bins = histogram(image_grey)
            number_of_zeros_bins = 0
            for a in freq:
                if a/freq.sum() < 0.001:
                    number_of_zeros_bins += 1
            print('number_of_zeros_bins: ', number_of_zeros_bins)
            if number_of_zeros_bins > 100:
                os.rename(file_path, os.path.splitext(file_path)[0] + '.jpg')
                dt_epoch = datetime.datetime.now().timestamp()
                os.utime(file_path, (dt_epoch, dt_epoch))
                # plt.imshow(image_grey)
                # plt.show()
            # plt.figure(num=None, figsize=(8, 6), dpi=100, facecolor='white')
            # plt.step(bins, freq/freq.sum())
            # plt.xlabel('intensity value', fontsize = 12)
            # plt.ylabel('fraction of pixels', fontsize = 12);
            # plt.show()

if __name__ == '__main__':
    main()