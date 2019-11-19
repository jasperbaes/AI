import train_data as data
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import Dense, Dropout
import os
from termcolor import colored
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def train_keras():
    print("Training dataset...")

    model = tf.keras.Sequential()
    model.add(Dense(units=1, input_shape=[1]))
    model.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1), metrics=['accuracy'])
    model.fit(data.traindata_a, data.traindata_b, epochs=9000, verbose=False)

    print("Calculating {} predictions by {} inputs... ".format(len(data.testset), len(data.traindata_a)))

    for cel in data.testset:
        answer = model.predict([cel])[0][0]
        print("[{}] ({}, {})".format(colored('+', 'green'), cel, answer))

    print("Layer weights: {} * {}".format(model.get_weights()[0][0][0], model.get_weights()[1][0]))

if __name__ == "__main__":
    try:
        train_keras()
    except:
        print("{} : Something went wrong here... Sure the training data is correct?".format(colored('WARNING', 'red')))
    