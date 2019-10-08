import numpy as np
import matplotlib.pyplot as plt
import imageio

def energy_image(img):
    grayImage = np.dot(img[...,:3], [0.2989, 0.587, 0.114])
    dImagedy = np.gradient(grayImage, axis=0)
    dImagedx = np.gradient(grayImage, axis=1)
    energy = np.abs(dImagedx) + np.abs(dImagedy)
    return energy

# img = imageio.imread('small.jpg')
# energyImage = energy_image(img)
# print(energyImage)