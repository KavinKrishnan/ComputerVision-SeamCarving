import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam
from reduceHeight import reduceHeight
import cv2

def reduceWidth(img, energyImage):
    cumulativeEnergyMap = cumulative_minimum_energy_map(energyImage, 'VERTICAL')
    seam = np.flip(find_optimal_vertical_seam(cumulativeEnergyMap))
    height, width = energyImage.shape

    newEnergyImage = np.empty([energyImage.shape[0], energyImage.shape[1]-1])
    newImage = np.empty([energyImage.shape[0], energyImage.shape[1] - 1,3])

    for y in range(0,height):
        newEnergyImage[y,:] = np.delete(energyImage[y], seam[y])
        newImage[y,:,:] = np.delete(img[y], seam[y], axis=0)

    newImage = newImage.astype(int)
    return (newImage, newEnergyImage)


# # # cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage, 'VERTICAL')
# # # cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage, 'HORIZONTAL')
# # # optimal = find_optimal_vertical_seam(cumulativeEnergyMap1)
# # image, newEnergyImage = reduceWidth('inputPS0Q2.jpg',energyImage)
# plt.imshow(resized)
# plt.show()
