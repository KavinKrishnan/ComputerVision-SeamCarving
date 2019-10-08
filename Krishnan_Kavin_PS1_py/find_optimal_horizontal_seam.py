import numpy as np
import matplotlib.pyplot as plt
import imageio
from energy_image import energy_image
from cumulative_minimum_energy_map import cumulative_minimum_energy_map

def find_optimal_horizontal_seam(cumulativeEnergyMap):
    seam = []
    height, width = cumulativeEnergyMap.shape
    tailIndex = np.argmin(cumulativeEnergyMap[:,-1])
    seam.append(tailIndex)
    y = tailIndex
    for x in range(width-2,-1,-1):
        nextIndex = -1
        if y == 0:
            subIndex = np.argmin([cumulativeEnergyMap[y][x],cumulativeEnergyMap[y+1][x]])
            if subIndex == 0:
                nextIndex = y
            else:
                nextIndex = y+1
        elif y == height-1:
            subIndex = np.argmin([cumulativeEnergyMap[y-1][x], cumulativeEnergyMap[y][x]])
            if subIndex == 0:
                nextIndex = y-1
            else:
                nextIndex = y
        else:
            subIndex = np.argmin([cumulativeEnergyMap[y-1][x], cumulativeEnergyMap[y][x], cumulativeEnergyMap[y+1][x]])
            if subIndex == 0:
                nextIndex = y - 1
            elif subIndex == 1:
                nextIndex = y
            else:
                nextIndex = y+1

        seam.append(nextIndex)
        y = nextIndex

    return np.array(seam)


# energyImage = energy_image('small.jpg')
# cumulativeEnergyMap1 = cumulative_minimum_energy_map(energyImage,'VERTICAL')
# cumulativeEnergyMap2 = cumulative_minimum_energy_map(energyImage,'HORIZONTAL')
# optimal = find_optimal_horizontal_seam(cumulativeEnergyMap2)