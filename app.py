from flask import Flask, request
import numpy as np
# import pickle
import tensorflow as tf

app = Flask(__name__)

# Load the trained model
# with open("model.pkl", "rb") as f:
#     model = pickle.load(f)

model = tf.keras.models.load_model("model.h5")

@app.route("/classify", methods=["POST"])
def classify():
    # Read the data from the request
    data = request.get_json()
    pixels = np.array(data["pixels"]).reshape(1, -1)

    # Use the model to make a prediction
    pred = int(np.round(model.predict(pixels)[0][0]))

    # Return the result as a JSON response
    return {"class": str(pred)}

if __name__ == "main":
    app.run()
