from flask import Flask, request, jsonify
import numpy as np, pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/predict", methods=["POST"])
def predict():
    d = request.json
    X = np.array([[d["age"], d["bmi"], d["bp"], d["glucose"], d["heart_rate"]]])
    return jsonify({"risk": int(model.predict(X)[0])})

app.run(port=5000)
