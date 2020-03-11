# To convert your keras model into tensorflow.js model which is suitable to use with javascript.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import tensorflow as tf
import tensorflowjs as tfjs

bring_model = tk.keras.models.load_model("... Your Model ...")

tfjs.converters.save_keras_model(bring_model, "tensorflow.js model")

