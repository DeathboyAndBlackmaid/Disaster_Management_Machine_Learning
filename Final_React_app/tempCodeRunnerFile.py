
if __name__ == "__main__":
    # Example values for Tilt_Readings, Water_Depth, Seismic_Activity, Coastal_Location
    warnings.filterwarnings('ignore')
    example_data = [[30, 150, 7, 1]] 
    
    # Call the function
    prediction = tsunami_prediction(example_data)
    print(prediction)