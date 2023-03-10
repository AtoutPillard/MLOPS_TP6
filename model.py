# -*- coding: utf-8 -*-
"""MLOPS_TP6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16GjbbfjO-2gFSrKIKX7KDb5JwKuB33LQ
"""

from __future__ import absolute_import , division , print_function , unicode_literals

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.callbacks import ModelCheckpoint
from keras.callbacks import EarlyStopping
from keras.models import load_model
from pyparsing import actions

# Import dataset
data = keras.datasets.fashion_mnist
mnist_data = data.load_data ()

( train_images , train_labels ) ,( test_images , test_labels ) = mnist_data

class_names = ["T-shirt/top",
            "Trouser",
            "Pullover",
            "Dress",
            "Coat",
            "Sandal",
            "Shirt",
            "Sneaker",
            "Bag",
            "Ankle boot"]

train_images=train_images/255.0

model = keras.Sequential([
 keras.layers.Flatten(input_shape=train_images[0].shape),
 keras.layers.Dense(128, activation="relu"),
  keras.layers.Dense(128, activation="relu"),
  keras.layers.Dense(64, activation="relu"),
  keras.layers.Dense(32, activation="relu"),
 keras.layers.Dense(10, activation="softmax")  
])
model.summary()

es = EarlyStopping(monitor='val_accuracy', mode='auto', verbose=0, patience=50)
mc = ModelCheckpoint('best_model.h5', monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
history = model.fit(train_images, train_labels, batch_size=128, epochs=20, validation_split=0.2, callbacks=[es, mc])
saved_model = load_model('best_model.h5')

#test accuracy and loss
_, train_acc = saved_model.evaluate(train_images, train_labels, verbose=0)
_, test_acc = saved_model.evaluate(test_images, test_labels, verbose=0)
print('Train: %.4f, Test: %.4f' % (train_acc, test_acc))