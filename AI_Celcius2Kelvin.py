import tensorflow as tf
import numpy as np
import os
from termcolor import colored
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Input with outcome
celcius_q = np.array([-200, -90, -40,  14, 32, 46, 59, 72, 100],  dtype=float)
kelvin_a    = np.array([73.15, 183.15, 233.15, 287.15,  305.15,  319.15, 332.15, 345.15, 373.15],  dtype=float)
celcius_testset = [-50, 0, 50, 100, 150]

print("Calculating {} predictions by {} inputs... ".format(len(celcius_testset), len(celcius_q)))

l0 = tf.keras.layers.Dense(units=1, input_shape=[1])
model = tf.keras.Sequential([l0])

model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
history = model.fit(celcius_q, kelvin_a, epochs=9000, verbose=False)

for cel in celcius_testset:
    print("[{}] ({}, {})".format(colored('+', 'green'), cel, model.predict([cel])[0][0]))
print("Layer weights: {} and {}".format(l0.get_weights()[0][0][0], l0.get_weights()[1][0]))
