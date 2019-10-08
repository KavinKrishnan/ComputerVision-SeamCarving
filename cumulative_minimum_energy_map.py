import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image

def cumulative_minimum_energy_map(energyImage,seamDirection):
    energy_map = np.zeros_like(energyImage)
    height,width = energy_map.shape

    if seamDirection is "VERTICAL":
        energy_map[0] = energyImage[0]
        for y in range(1,height):
            for x in range(0, width):
                minimumElement = []
                if x != 0:
                    minimumElement.append(energy_map[y-1][x-1])
                minimumElement.append(energy_map[y - 1][x])
                if x + 1 < width:
                    minimumElement.append(energy_map[y - 1][x+1])
                energy_map[y][x] = energyImage[y][x] + min(minimumElement)
    elif seamDirection is "HORIZONTAL":
        energy_map[:, 0] = energyImage[:, 0]
        for x in range(1,width):
            for y in range(0, height):
                minimumElement = []
                if y != 0:
                    minimumElement.append(energy_map[y-1][x-1])
                minimumElement.append(energy_map[y][x-1])
                if y + 1 < height:
                    minimumElement.append(energy_map[y+1][x-1])
                energy_map[y][x] = energyImage[y][x] + min(minimumElement)


    return energy_map

# img = imageio.imread('inputSeamCarvingPrague.jpg')
# energyImage = energy_image(img)
# plt.imshow(energyImage)
# plt.show()
# cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage,'VERTICAL')
# plt.imshow(cumulativeEnergyMap1)
# plt.show()
# cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage,'HORIZONTAL')
# plt.imshow(cumulativeEnergyMap2)
# plt.show()
