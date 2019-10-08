import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map

def find_optimal_vertical_seam(cumulativeEnergyMap):
    seam = []
    height, width = cumulativeEnergyMap.shape
    tailIndex = np.argmin(cumulativeEnergyMap[-1])
    seam.append(tailIndex)
    x = tailIndex
    for y in range(height-2,-1,-1):
        nextIndex = -1
        if x == 0:
            subIndex = np.argmin([cumulativeEnergyMap[y][x],cumulativeEnergyMap[y][x+1]])
            if subIndex == 0:
                nextIndex = x
            else:
                nextIndex = x+1
        elif x == width-1:
            subIndex = np.argmin([cumulativeEnergyMap[y][x-1], cumulativeEnergyMap[y][x]])
            if subIndex == 0:
                nextIndex = x-1
            else:
                nextIndex = x
        else:
            subIndex = np.argmin([cumulativeEnergyMap[y][x - 1], cumulativeEnergyMap[y][x], cumulativeEnergyMap[y][x+1]])
            if subIndex == 0:
                nextIndex = x - 1
            elif subIndex == 1:
                nextIndex = x
            else:
                nextIndex = x+1

        seam.append(nextIndex)
        x = nextIndex

    return np.array(seam)


# energyImage = energy_image('small.jpg')
# cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage,'VERTICAL')
# cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage,'HORIZONTAL')
# optimal = find_optimal_vertical_seam(cumulativeEnergyMap1)

