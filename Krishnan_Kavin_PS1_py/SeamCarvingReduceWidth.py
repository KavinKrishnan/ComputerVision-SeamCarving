import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from reduceWidth import reduceWidth

image1 = 'outputReduceWidthPrague.png'
img = imageio.imread('inputSeamCarvingPrague.jpg')
energyImage = energy_image(img)

for i in range(0,100):
    img, energyImage = reduceWidth(img,energyImage)

img = img.astype(np.uint8)
imageio.imwrite(image1, img)

image2 = 'outputReduceWidthMall.png'
img = imageio.imread('inputSeamCarvingMall.jpg')
energyImage = energy_image(img)

for i in range(0,100):
    img, energyImage = reduceWidth(img,energyImage)

img = img.astype(np.uint8)
imageio.imwrite(image2, img)



