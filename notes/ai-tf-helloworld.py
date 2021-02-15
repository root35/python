import tensorflow as tf
import numpy as np
from tensorflow import keras

# Designing the model
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# Building the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Log the model for future visualization in TensorBoard
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs",
                                                      write_graph=True,
                                                      histogram_freq=5)

# Providing the data
xs = np.array([-1.0,  0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# Training the model
model.fit(xs, ys, epochs=500, callbacks=[tensorboard_callback])

# Using the model for prediction
print(model.predict([10.0]))