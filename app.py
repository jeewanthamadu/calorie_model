from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np

# Load trained model
model = joblib.load("model/calorie_model.pkl")

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Calorie Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # Expecting JSON payload
        df = pd.DataFrame(data)  # Convert to DataFrame
        preds = model.predict(df)
        preds = np.clip(preds, 0, None)  # No negative calories
        return jsonify({"predictions": preds.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
