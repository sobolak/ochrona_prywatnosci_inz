# -*- coding: utf-8 -*-
"""cifar_no_federated.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14vZIEB0M0gTLYGVfFDWG9A3oLmVXsLXT
"""

!pip install --quiet --upgrade tensorflow-federated-nightly
!pip install --quiet --upgrade nest-asyncio
!pip install --quiet --upgrade tb-nightly  

import nest_asyncio
import collections
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_federated as tff
import tensorflow_privacy as tfp
from matplotlib import pyplot as plt

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.cifar100.load_data()

y_train = y_train.reshape(-1,)
y_test = y_test.reshape(-1,)

x_train = x_train/255
x_test = x_test/255

model_normal = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(input_shape=(32,32,3), kernel_size=(2, 2), padding='same', strides=(2,2), filters = 32),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides = (1,1), padding = "same"),
    tf.keras.layers.Conv2D(kernel_size=(2, 2), padding='same', strides=(2,2), filters = 64),
    tf.keras.layers.MaxPooling2D(pool_size=(2,2), strides = (1,1), padding = "same"),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation=tf.nn.relu),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(100, activation=tf.nn.softmax)])

model_normal.summary()

model_normal.compile(loss = 'sparse_categorical_crossentropy',
                     optimizer = 'SGD',
                     metrics = ['accuracy'])

from google.colab import drive
drive.mount('/content/drive')

csv_logger = tf.keras.callbacks.CSVLogger('/content/drive/MyDrive/inz/CIFAR5.csv')

model_normal.fit(x_train, y_train, epochs = 50, callbacks=[csv_logger])
