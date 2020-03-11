# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:07:50 2020

@author: Chirag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import tensorflow as tf
import tensorflowjs as tfjs

bring_model = tk.keras.models.load_model("main_model_2e_good.h5")

tfjs.converters.save_keras_model(bring_model, "tensorflow.js model")


