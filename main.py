from flask import Flask, render_template, request
import json

import numpy as np
import pandas as pd
from keras_preprocessing.sequence import pad_sequences
import tensorflow as tf
import pickle

with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = tf.keras.models.load_model('best_model.h5')


def predict(text):
    series = pd.Series(text)
    X = pad_sequences(tokenizer.texts_to_sequences(
        series), padding='post', maxlen=25)
    return int(np.argmax(model.predict(X)))


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        text = json.loads(request.data)["data"]
        print(text)

        return json.dumps({"value": predict(text)})

    else:
        return render_template("index.html")


@app.route("/script.js")
def script():
    return render_template("script.js")


if __name__ == "__main__":
    app.run(debug=True)
