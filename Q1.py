import numpy as np
from sklearn.svm import SVC
from matplotlib import pyplot as plt
from matplotlib import cm
# Part (a)
# Generate 2-class data that are just barely separable
# each class is generated y a normal distribution
np.random.seed(314) # control the seed for reproducibility
n_samples = np.array([50,50]) # generate 50 samples per class
c1_mean = np.array([0.2,2.8]).T # mean vector of class 1
c2_mean = np.array([2,-3]).T # mean vector of class 2
c1_cov = np.array([[3,1],[1,2]]) # covariance matrix of class 1
c2_cov = np.array([[2,1],[1,3]]) # covariance matrix of class 2
c1_samples = np.random.multivariate_normal(c1_mean, c1_cov, n_samples[0])
c2_samples = np.random.multivariate_normal(c2_mean, c2_cov, n_samples[1])
X = np.vstack((c1_samples, c2_samples)) # data matrix
y = np.hstack((np.ones(n_samples[0]), -1*np.ones(n_samples[1]))) # class labels

# scatter plot of the data
# set font size
plt.rcParams.update({'font.size': 16})
plt.figure(figsize=(8,6))
plt.scatter(c1_samples[:,0], c1_samples[:,1], marker='o', color='b', label='Class 1')
plt.scatter(c2_samples[:,0], c2_samples[:,1], marker='o', color='r', label='Class 2')
plt.title('Generated 2-Class Data')
plt.xlabel('X_1')
plt.ylabel('X_2')
plt.legend()
plt.grid()
plt.show()