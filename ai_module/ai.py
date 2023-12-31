import pandas as pd
from joblib import load


class WateringPredictor:
    def __init__(self):
        #importing the os module
        import os

        #to get the current working directory
        directory = os.getcwd()

        print(directory)
        self.model = load('model/svm_model.joblib')
        self.scaler = load('model/scaler.joblib')

    def generate_prediction(self, data):
        print(data)
        thing_id = data["thing_id"]
        print(data)
        df = pd.DataFrame.from_dict(data, orient="index").T
        df = df[["temperature", "light", "airHumidity", "humidity"]]
        df = self.scaler.transform(df)
        prediction = self.model.predict(df)
        print("Prediction:", prediction[0])
        plant_good_condition = prediction[0] == 1
        reasons = []
        if not plant_good_condition:
            original_temperature = data['temperature']
            original_humidity = data['humidity']
            original_airHumidity = data['airHumidity']
            original_light = data['light']

            if not (20 <= original_temperature <= 25):
                reasons.append("Temperature is not in the acceptable range. (20-25)")
            if not (65 <= original_airHumidity <= 75):
                reasons.append("Air Humidity is not in the acceptable range. (65-75)")
            if not (83 <= original_humidity <= 93):
                reasons.append("Humidity is not in the acceptable range. (83-93)")
        return {
            "thing_id": thing_id,
            "need_watering": not plant_good_condition,
            "reasons": reasons
        }
