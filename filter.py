from frontend import setThreshold, saveAnimation
import numpy as np

data = np.load('data.npy')
data = data.T
coords, density = data[:,:2],data[:,2]

# density2 = setThreshold(density, coords)
# print(density==density2)

history = np.load('history.npy')
saveAnimation(history, coords)

