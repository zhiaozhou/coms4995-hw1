from hw1 import *
from helpers import *
import numpy as np

# Load the data
data_root_path = '/home/daniel/hw1/cifar10-hw1/'
X_train, y_train = get_train_data(data_root_path, limit=10) # this may take a few minutes
X_test = get_images(data_root_path + 'test', limit=10)
print('Data loading done')

# Part 1

layer_dimensions = [X_train.shape[0], 10]  # including the input and output layers
NN = NeuralNetwork(layer_dimensions)
NN.train(X_train, y_train, iters=1000, alpha=0.1, batch_size=10, print_every=50)

y_predicted = NN.predict(X_test)
save_predictions('ans1-uni', y_predicted)

# test if your numpy file has been saved correctly
loaded_y = np.load('ans1-uni.npy')
print(loaded_y.shape)
loaded_y[:10]