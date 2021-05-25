import tensorflow as tf
print(tf.__version__)
import numpy as np
np.set_printoptions(linewidth=200)
import matplotlib.pyplot as plt

# Loading the data

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
print(type(training_images), ' ', training_images.shape)        # <class 'numpy.ndarray'>   (60000, 28, 28)
print(type(training_images[0]), ' ', training_images[0].shape)  # <class 'numpy.ndarray'>   (28, 28)

plt.imshow(training_images[0])
print(training_labels[0])
print(training_images[0])

# Normalizing the data: set all values between 0 and 1 (originally 0-255)
training_images = training_images / 255.0
test_images = test_images / 255.0

# Designing the model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
print(model)
print(dir(model))

# Building the model
model.compile(optimizer = tf.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Log the model for future visualization in TensorBoard
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs",
                                                      write_graph=True,
                                                      histogram_freq=5)

# Training the model
model.fit(training_images, training_labels, epochs=5, callbacks=[tensorboard_callback])

# Testing the model
model.evaluate(test_images, test_labels)