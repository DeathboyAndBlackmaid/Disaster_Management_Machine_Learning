import json
from earthquake_model import predict_earthquake
from flood_model import predict_flood_occurrence
from landslide_model import predict_landslide_occurrence
from tsunami_model import tsunami_prediction
from wildfire_model import predict_wildfire_occurrence

"""
Script to predict natural disasters using pre-trained models.

Author: Paidi Akileswar

Packages:
- earthquake_model: Module containing functions for earthquake prediction.
- flood_model: Module containing functions for flood prediction.
- landslide_model: Module containing functions for landslide prediction.
- tsunami_model: Module containing functions for tsunami prediction.
- wildfire_model: Module containing functions for wildfire prediction.

Usage:
- Make predictions for various natural disasters using data obtained from APIs.
- Store predictions in a JSON file.

"""

# Given data from APIs

# Magnitude,Depth,Distance_to_Fault,Population_Density,Building_Density   
earthquake_data = [[55, 310, 6, 32, 75]]


# Precipitation, River_Discharge, River_Stage, Weather_Forecast, Soil_Moisture
rainfall_data = [[10, 80, 25, 5000, 1]]


# Soil_Drift, Rainfall, Slope_Angle, Temperature
soil_drift_data = [[7.5, 80, 25, 35]]


# Temperature, Humidity, Wind_Speed, Rainfall, Dryness_Index
temperature_data = [[30, 20, 10, 50, 101]]


# Tilt_Readings, Water_Depth, Seismic_Activity, Coastal_Location
tilt_data = [[30, 150, 7, 1]]

try:
    print("Predicting earthquake...")
    earthquake_prediction = predict_earthquake(earthquake_data)
    print("Earthquake prediction completed.")
except Exception as e:
    print("Error predicting earthquake:", e)
    earthquake_prediction = "error"
print("===========> COMPLETED <===============\n\n")


try:
    print("Predicting flood...")
    flood_prediction = predict_flood_occurrence(rainfall_data)  # Using rainfall data for flood prediction
    print("Flood prediction completed.")
except Exception as e:
    print("Error predicting flood:", e)
    flood_prediction = "error"
print("===========> COMPLETED <===============\n\n")


try:
    print("Predicting landslide...")
    landslide_prediction = predict_landslide_occurrence(soil_drift_data)
    print("Landslide prediction completed.")
except Exception as e:
    print("Error predicting landslide:", e)
    landslide_prediction = "error"
print("===========> COMPLETED <===============\n\n")


try:
    print("Predicting tsunami...")
    tsunami_prediction_result = tsunami_prediction(tilt_data)
    print("Tsunami prediction completed.")
except Exception as e:
    print("Error predicting tsunami:", e)
    tsunami_prediction_result = "error"
print("===========> COMPLETED <===============\n\n")

try:
    print("Predicting wildfire...")
    wildfire_prediction = predict_wildfire_occurrence(temperature_data)
    print("Wildfire prediction completed.")
except Exception as e:
    print("Error predicting wildfire:", e)
    wildfire_prediction = "error"
print("===========> COMPLETED <===============\n\n")

# Convert predictions to JSON format
predictions = {
    'flood': {'reading': f'{rainfall_data[0][0]}mm', 'prediction': 'yes' if flood_prediction == 1 else 'no'},
    'earthquake': {'reading': f'{earthquake_data[0][0]}', 'prediction': 'yes' if earthquake_prediction == 1 else 'no'},
    'landslide': {'reading': f'{soil_drift_data[0][2]}', 'prediction': 'yes' if landslide_prediction == 1 else 'no'},
    'tsunami': {'reading': f'{tilt_data[0][2]}', 'prediction': 'yes' if tsunami_prediction_result == 1 else 'no'},
    'wildfire': {'reading': f'{temperature_data[0][0]}C', 'prediction': 'yes' if wildfire_prediction == 1 else 'no'}
}

# Save predictions to a JSON file
with open('predictions.json', 'w') as json_file:
    json.dump(predictions, json_file)

print("Predictions saved to predictions.json")
