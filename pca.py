#!/usr/bin/python
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d


np.random.seed(1) # random seed for consistency

# A reader pointed out that Python 2.7 would raise a
# "ValueError: object of too small depth for desired array".
# This can be avoided by choosing a smaller random seed, e.g. 1
# or by completely omitting this line, since I just used the random seed for
# consistency.

mu_vec1 = np.array([0,0,0])
cov_mat1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

mu_vec2 = np.array([1,1,1])
cov_mat2 = np.array([[1,0,0],[0,1,0],[0,0,1]])
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, 20).T
assert class1_sample.shape == (3,20), "The matrix has not the dimensions 3x20"

#print(class1_sample)
#print(class2_sample)
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
plt.rcParams['legend.fontsize'] = 10   
ax.plot(class1_sample[0,:], class1_sample[1,:], class1_sample[2,:], 'o', markersize=8, color='blue', alpha=0.5, label='class1')
ax.plot(class2_sample[0,:], class2_sample[1,:], class2_sample[2,:], '^', markersize=8, alpha=0.5, color='red', label='class2')

plt.title('Samples for class 1 and class 2')
ax.legend(loc='upper right')

#plt.show()

class3_sample = np.concatenate([class1_sample,class2_sample],1)
assert class3_sample.shape == (3,40), "The matrix doesn't have dimention of 3X40"

#print(class3_sample)

## mean vector for each row

mean_x = np.mean(class3_sample[0,])
mean_y = np.mean(class3_sample[1,])
mean_z = np.mean(class3_sample[2,])
mean_vec = np.array([mean_x,mean_y,mean_z])
print(mean_vec)
#print(mean_y)


#===========================
# scatter matrix
#
#print (range(class3_sample.shape[0]))
for i in range(class3_sample.shape[0])
    
