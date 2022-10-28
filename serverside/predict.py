import joblib
import pandas as pd
from ml.training import MODEL_PATH, FILE_PATH, split_data
import numpy as np


SCHEMA = [
    'Alcohol', 'Malic', 'Ash',
    'Alcalinity', 'Magnesium', 'Phenols', 'Flavanoids',
    'Nonflavanoids', 'Proanthocyanins', 'Color', 'Hue', 'Dilution',
    'Proline'
]


def read_model():
    mdl = joblib.load(MODEL_PATH)
    return mdl


def pre_process_input(data: dict) -> np.array:
    data_list = []
    for item in SCHEMA:
        data_list.append(data[item])
    return np.array([data_list])


def post_process_result(result: np.array) -> int:
    return round(result[0])


if __name__ == "__main__":
    model = read_model()
    test_data = {
        'Alcohol': 12.17, 'Malic': 1.45, 'Ash': 2.53, 'Alcalinity': 19.0,
        'Magnesium': 104.0, 'Phenols': 1.89, 'Flavanoids': 1.75,
        'Nonflavanoids': 0.45, 'Proanthocyanins': 1.03, 'Color': 2.95,
        'Hue': 1.45, 'Dilution': 2.23, 'Proline': 355.0
    }
    processed_data = pre_process_input(test_data)
    result = model.predict(processed_data)
    result = post_process_result(result)


