# To convert your Keras model .h5 to tf.lite form.

import tensorflow as tf

bring_model = tf.keras.models.load_model("... Your Model ...")

# Convert the Keras model.
converter = tf.lite.TFLiteConverter.from_keras_model(bring_model)
tflite_model = converter.convert()
open("converted_sld_model.tflite", "wb").write(tflite_model)
