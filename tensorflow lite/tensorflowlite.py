# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 20:36:31 2020

@author: Chirag
"""

import tensorflow as tf

bring_model = tf.keras.models.load_model("sld_model.h5")

# Convert the Keras model.
converter = tf.lite.TFLiteConverter.from_keras_model(bring_model)
tflite_model = converter.convert()
open("converted_sld_model.tflite", "wb").write(tflite_model)