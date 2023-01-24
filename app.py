
"""
simple python flask application
"""

##########################################################################
## Imports
##########################################################################

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask.json import jsonify
import numpy as np
import tensorflow as tf

##########################################################################
## Application Setup
##########################################################################

model = tf.keras.models.load_model('./best_model.h5')

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

def prepare_data(row):
    numbers = list(map(int, row.split(',')))
    return np.array(numbers).reshape(1, 28, 28)

def predict_result(img):
    predictions = model.predict(img)
    predicted_label = np.argmax(predictions)
    return predicted_label

app = Flask(__name__)

##########################################################################
## Routes
##########################################################################

@app.route("/")
def home():
    return render_template("home.html")
    

@app.route('/api/classify', methods=['POST'])
def classify_image():
    incoming = request.form.get('query')
    img = prepare_data(incoming)
    res = predict_result(img)
    return jsonify(prediction=class_names[res])

##########################################################################
## Main
##########################################################################

if __name__ == '__main__':
    app.run()