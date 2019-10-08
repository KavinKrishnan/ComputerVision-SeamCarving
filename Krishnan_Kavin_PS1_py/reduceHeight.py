import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam

def reduceHeight(img, energyImage):
    cumulativeEnergyMap = cumulative_minimum_energy_map(energyImage, 'HORIZONTAL')
    seam = np.flip(find_optimal_horizontal_seam(cumulativeEnergyMap))
    height, width = energyImage.shape

    newEnergyImage = np.empty([energyImage.shape[0]-1, energyImage.shape[1]])
    newImage = np.empty([energyImage.shape[0]-1, energyImage.shape[1],3])

    for x in range(0,width):
        newEnergyImage[:,x] = np.delete(energyImage[:,x], seam[x])
        newImage[:,x,:] = np.delete(img[:,x], seam[x], axis=0)

    newImage = newImage.astype(int)
    return (newImage, newEnergyImage)


# energyImage = energy_image('inputPS0Q2.jpg')
# # cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage, 'VERTICAL')
# # cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage, 'HORIZONTAL')
# # optimal = find_optimal_vertical_seam(cumulativeEnergyMap1)
# image, newEnergyImage = reduceHeight('inputPS0Q2.jpg',energyImage)
# plt.imshow(image)
# plt.show()
