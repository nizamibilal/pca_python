#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from matplotlib.patches import FancyArrowPatch
from matplotlib.mlab import PCA

## Read data file 
arr = []
fp = open ("places_number.txt","r")
#read line into array 
for line in fp.readlines():
    # add a new sublist
    arr.append([])
    # loop over the elemets, split by whitespace
    for i in line.split():
        # convert to integer and append to the last
        # element of the list
        arr[-1].append(float(i))

fp.close()
arr = np.array(arr)

#print (np.shape(arr))

#Header and places titles
head = ['Climate', 'HousingCost', 'HlthCare', 'Crime', 'Transp', 'Educ Arts', 'Recreat', 'Econ', 'CaseNum', 'Long', 'Lat', 'Pop', 'StNum']

#++++++++++++++++++++++=
# plot 3 dimentions of the matrix, 
# just change the index of vectors to plot different dimentions

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111,projection = '3d')
#ax.plot(arr[:,0],arr[:,3], marker='o', linestyle='None')
#plt.show()

place_pca = PCA(arr)
print(place_pca.fracs)
#print (place_pca.Y)
#plt.plot(place_pca.Y[:,0],place_pca.Y[:,3], marker='^', linestyle='None')

#plt.plot(place_pca.project(arr[1,:]))
#plt.show()