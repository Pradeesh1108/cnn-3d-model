from tensorflow.keras.datasets import mnist
import numpy as np

def load_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train[..., np.newaxis] / 255.0
    x_test = x_test[..., np.newaxis] / 255.0
    return x_train[:2000], x_test[:100], y_train[:2000], y_test[:100]
