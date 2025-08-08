from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = [
            data.get("ph"),
            data.get("Hardness"),
            data.get("Solids"),
            data.get("Chloramines"),
            data.get("Sulfate"),
            data.get("Conductivity"),
            data.get("Organic_carbon"),
            data.get("Trihalomethanes"),
            data.get("Turbidity"),
        ]
        prediction = model.predict([features])[0]
        result = "Safe" if prediction == 1 else "Not Safe"
        return jsonify({"prediction": result})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
