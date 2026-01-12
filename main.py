import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('handwritten_model.keras') # Loading the model

img = cv2.imread('Opera Snapshot_2026-01-12_144050_opera.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (28, 28))
img = np.expand_dims(img, axis=0)

prediction = model.predict(img)
print (f"Number: {np.argmax(prediction)}")


# Second Test