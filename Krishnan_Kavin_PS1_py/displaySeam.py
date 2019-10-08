import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map
from find_optimal_vertical_seam import find_optimal_vertical_seam
from find_optimal_horizontal_seam import find_optimal_horizontal_seam

def displaySeam(image, seam, type):
    img = imageio.imread(image)
    plt.imshow(img)

    if type is "VERTICAL":
        x = np.flip(seam)
        y = np.arange(img.shape[0])
        plt.plot(x,y,'m-')
    elif type is "HORIZONTAL":
        y = np.flip(seam)
        x = np.arange(img.shape[1])
        plt.plot(x,y,'m-')

    plt.show()

# img = imageio.imread('inputSeamCarvingPrague.jpg')
# energyImage = energy_image(img)
# cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage,'VERTICAL')
# cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage,'HORIZONTAL')
# optimal = find_optimal_vertical_seam(cumulativeEnergyMap1)
# displaySeam('inputSeamCarvingPrague.jpg',optimal,'VERTICAL')
# optimal = find_optimal_horizontal_seam(cumulativeEnergyMap2)
# displaySeam('inputSeamCarvingPrague.jpg',optimal,'HORIZONTAL')

