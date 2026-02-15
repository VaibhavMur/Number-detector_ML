import cv2
import tensorflow as tf
from flask import Flask, request, jsonify
import base64
import io
from PIL import Image, ImageOps
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]
    
    encoded = data.split(",")[1]

    img_bytes = base64.b64decode(encoded)
    img = Image.open(io.BytesIO(img_bytes)).convert("L")  
    img = ImageOps.fit(img, (28, 28), Image.Resampling.LANCZOS)
    img_array = np.array(img)
    img_array = img_array.astype(np.float32) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Convert to numpy
    model = tf.keras.models.load_model('handwritten_model.keras')
    prediction = model.predict(img_array)
    digit = int(np.argmax(prediction))
    
    return jsonify({"prediction": digit})


app.run(port=5000)
