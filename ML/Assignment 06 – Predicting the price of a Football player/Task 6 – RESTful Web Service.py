# Task 6: Deploy Football Player Market Value Model
# RESTful Web Service using Flask

import os
import joblib
import pandas as pd

from flask import Flask, request, jsonify


# Step 1: Create Flask application
app = Flask(__name__)


# Step 2: Load the trained model
folder_path = os.path.dirname(
    os.path.abspath(__file__)
)

model_path = os.path.join(
    folder_path,
    "Task_4_Best_Model.pkl"
)

model = joblib.load(model_path)


# Step 3: Define input features
features = [
    "age",
    "position",
    "club",
    "page_views",
    "fpl_value",
    "fpl_sel",
    "fpl_points",
    "region",
    "new_foreign",
    "big_club",
    "new_signing"
]

numerical_columns = [
    "age",
    "page_views",
    "fpl_value",
    "fpl_sel",
    "fpl_points",
    "region",
    "new_foreign",
    "big_club",
    "new_signing"
]


# Step 4: Create prediction function
def predict_market_value(player_data):

    # Check whether all required features are provided
    for feature in features:

        if feature not in player_data:
            raise ValueError(
                "Missing required feature: " + feature
            )

    # Convert input into a DataFrame
    input_data = pd.DataFrame(
        [player_data]
    )

    # Convert FPL selection percentage into numeric form
    input_data["fpl_sel"] = (
        input_data["fpl_sel"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    # Convert numerical columns
    for column in numerical_columns:

        input_data[column] = pd.to_numeric(
            input_data[column],
            errors="coerce"
        )

    # Check for invalid numerical values
    if input_data[numerical_columns].isnull().any().any():

        raise ValueError(
            "Please provide valid numerical values."
        )

    # Select features in the correct order
    input_data = input_data[features]

    # Generate prediction
    prediction = model.predict(input_data)

    return round(float(prediction[0]), 2)


# Step 5: Home route
@app.route("/", methods=["GET"])
def home():

    return jsonify({
        "message": "Football Player Market Value Prediction API",
        "status": "Running",
        "endpoint": "/predict",
        "method": "POST"
    })


# Step 6: Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Read JSON input
        player_data = request.get_json(silent=True)

        if not isinstance(player_data, dict):

            return jsonify({
                "error": "Please provide player details as JSON."
            }), 400

        # Predict market value
        predicted_value = predict_market_value(
            player_data
        )

        # Return JSON response
        return jsonify({
            "predicted_market_value": predicted_value,
            "currency": "Million Euros"
        })

    except ValueError as error:

        return jsonify({
            "error": str(error)
        }), 400

    except Exception:

        return jsonify({
            "error": "Prediction failed. Check the model and input data."
        }), 500


# Step 7: Run Flask server
if __name__ == "__main__":

    print("\nStarting Football Player Prediction API...")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
