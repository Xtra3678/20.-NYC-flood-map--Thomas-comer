# Name:  T.J. Comer
# Email: thomas.comer82@hunter
# Date:  October 17 2022
# Takes elevation data of NYC and displays a flood map showing 6ft flooding in yellow and 20 ft flooding in grey


#Import the libraries for arrays and displaying images:
import numpy as np
import matplotlib.pyplot as plt


#Read in the data to an array, called elevations:
elevations = np.loadtxt('elevationsNYC.txt')

#Take the shape (dimensions) of the elevations
#  and add another dimension to hold the 3 color channels:
mapShape = elevations.shape + (3,)

#Create a blank image that's all zeros:
floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            #Below sea level
           floodMap[row,col,2] = 1.0     #Set the blue channel to 100%
        elif elevations[row,col] <= 6:
            #Below the storm surge of Hurricane Sandy (flooding likely)
           floodMap[row,col,0] = 1.0     #Set the red channel to 100%
           floodMap[row,col,1] = 1.0   #Set the green channel to 100%
        elif elevations[row,col] <= 20:
            #Above the storm surge of Hurricane Sandy, but below a 20 ft danger floodline (flooding unlikely)
           floodMap[row,col,0] = 0.5     #Set the red channel to 100%
           floodMap[row,col,1] = 0.5   #Set the green channel to 100%
           floodMap[row,col,2] = 0.5   #Set the green channel to 100%
        else:
            #Above the 20 foot storm surge and didn't flood
            floodMap[row,col,1] = 1.0   #Set the green channel to 100%

#Load the flood map image into matplotlib.pyplot:
plt.imshow(floodMap)

#Save the image:
plt.imsave('floodMap.png', floodMap)
