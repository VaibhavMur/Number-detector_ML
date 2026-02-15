import os
import matplotlib.pyplot as plt
import tensorflow as tf


mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the images to [0, 1] range
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

model = tf.keras.models.Sequential() # Calling the Sequential model
model.add(tf.keras.layers.Flatten(input_shape = (28, 28))) # Flattening the 2D images to 1D vectors
model.add(tf.keras.layers.Dense(128, activation = 'relu')) # First hidden layer with ReLU activation. RELU stands for Rectified Linear Unit
model.add(tf.keras.layers.Dense(128, activation = 'relu')) # Second hidden layer with ReLU activation. RELU stands for Rectified Linear Unit
model.add(tf.keras.layers.Dense(10, activation = 'softmax')) # Output layer with Softmax activation. Softmax makes sure the outputs add up to 1, so they can be interpreted as probabilities/confidence

model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])

model.fit(x_train, y_train, epochs = 200) # Training the model for 50 epochs

model.save('handwritten_model.keras') # Saving the model