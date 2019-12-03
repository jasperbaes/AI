import numpy as np

# Celcius to Kelvin Traindata
traindata_a = np.array([-200, -90, -40,  14, 32, 46, 59, 72, 100],  dtype=float)
traindata_b    = np.array([73.15, 183.15, 233.15, 287.15,  305.15,  319.15, 332.15, 345.15, 373.15],  dtype=float)
testset = [-50, 0, 50, 100, 150]
 
# Euro to Dollar Traindata
# traindata_a  = np.array([0.1, 0.5, 0.9, 1, 1.5, 10, 25, 101, 1001],  dtype=float)
# traindata_b    = np.array([0.110790, 0.553948, 0.997136, 1.107929,  1.661893,  11.079641, 27.699103, 111.907453, 1109.102581],  dtype=float)
# testset = [-50, 0, 50, 100, 150]